import _thread
import io
import json
import os.path
import shutil
import subprocess
import sys
import tempfile
import time
import psutil
import hashlib
from PySide6.QtCore import Signal, QThread, Qt, QPoint
from PySide6.QtGui import QIcon, QTextCursor, QMouseEvent, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog, QLineEdit, QVBoxLayout, QTextEdit, \
    QPushButton, QListWidget, QListWidgetItem, QLabel

from copyright_form import MyCopyrightForm
from replace_thread import replaceThread, replace_threads
from runtime import Ui_runtimeDialog
from ui import Ui_MainWindow
from my_log import log_print, log_path

combobox_dic = dict()

rpy_file_name = 'renpy_runtime_editor_hook.rpy'
json_path = tempfile.gettempdir() + '/' + 'renpy_runtime_editor_hooked.json'
reload_check_file_name = 'renpy_runtime_editor.reload'
reload_check_file_path = None
current_work_directory = None
last_data = None

def compare_files(file1, file2):
    hash1 = hashlib.md5()
    with open(file1, 'rb') as f1:
        for chunk in iter(lambda: f1.read(4096), b''):
            hash1.update(chunk)

    hash2 = hashlib.md5()
    with open(file2, 'rb') as f2:
        for chunk in iter(lambda: f2.read(4096), b''):
            hash2.update(chunk)

    return hash1.digest() == hash2.digest()


def replace_line(file_path, line_number, to_replace,replace_to):
    with open(file_path, 'r',encoding='utf-8') as file:
        lines = file.readlines()
    new_line = lines[line_number-1].replace(to_replace,replace_to)
    del lines[line_number-1]
    lines.insert(line_number-1, new_line + '\n')
    with open(file_path, 'w',encoding='utf-8') as file:
        file.writelines(lines)

def get_from_last_data(key):
    global last_data
    try:
        js = json.loads(last_data)
        if 'cur_id' in js.keys():
            cur_id = js['cur_id']
            if cur_id in js.keys():
                cur_id = js[cur_id]
                if key in cur_id.keys():
                    return cur_id[key]
    except Exception:
        pass
class MyListWidget(QListWidget):

    right_clicked = Signal()
    left_clicked = Signal()
    double_clicked = Signal()

    def __init__(self):
        super(MyListWidget, self).__init__()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.type() == QMouseEvent.MouseButtonPress:
            pos = QCursor.pos() - self.mapToGlobal(QPoint(0, 0))
            self.setCurrentRow(self.indexAt(pos).row())

            if event.button() == Qt.RightButton:
                self.right_clicked.emit()
                self.takeItem(self.currentRow())

            elif event.button() == Qt.LeftButton:
                self.left_clicked.emit()
                item = self.currentItem()
                if item is None:
                    return
                data = item.data(Qt.UserRole)
                dialog = MyInputDialog(self)
                dialog.setWindowTitle('Input Dialog')
                dialog.text_edit.setText(data['text'])
                key = None
                if 'ori_what' in data.keys():
                    dialog.text_edit_ori.setText(data['ori_what'])
                    key = 'ori_what'
                if 'what' in data.keys():
                    dialog.text_edit_ori.setText(data['what'])
                    key = 'what'
                if 'who' in data.keys():
                    dialog.text_edit_ori.setText(data['who'])
                    key = 'who'

                if key is None:
                    return

                if dialog.exec():
                    text = dialog.getText()
                    data['text'] = text
                    item.setData(Qt.UserRole, data)
                    item.setText(data[key] + '-->' + text)
                    if data[key] == text:
                        self.takeItem(self.currentRow())

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:

        pos = QCursor.pos() - self.mapToGlobal(QPoint(0, 0))
        self.setCurrentRow(self.indexAt(pos).row())

        if event.button() == Qt.MouseButton.LeftButton:
            self.double_clicked.emit()




class MyInputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.text_edit_ori = QTextEdit()
        self.text_edit_ori.setReadOnly(True)
        self.text_edit = QTextEdit()
        layout.addWidget(self.label1)
        layout.addWidget(self.text_edit_ori)
        layout.addWidget(self.label2)
        layout.addWidget(self.text_edit)


        button = QPushButton('OK')
        button.clicked.connect(self.accept)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setMinimumWidth(1000)

    def getText(self):
        return self.text_edit.toPlainText()


class MyRuntimeForm(QDialog, Ui_runtimeDialog):
    def __init__(self, parent=None):
        super(MyRuntimeForm, self).__init__(parent)
        self.setupUi(self)
        self.is_end = False
        _thread.start_new_thread(self.update_log, ())
        self.whoEditButton.clicked.connect(self.who_edit_click)
        self.oriWhatEditButton.clicked.connect(self.ori_what_edit_click)
        self.currentWhatEditButton.clicked.connect(self.current_what_edit_click)
        self.list_widget = MyListWidget()
        self.verticalLayout.addWidget(self.list_widget)
        self.reloadButton.clicked.connect(self.reload_scirpts)
        self.autoReloadCheckBox.setChecked(True)
        self.replaceButton.clicked.connect(self.replace_scirpts)
        self.versionLabel.setStyleSheet("color:grey")
        self.copyrightLabel.setStyleSheet("color:grey")

    def closeEvent(self, event):
        self.is_end = True

    def replace_scirpts(self):
        def getItem(name,e):
            if name in e.data(Qt.UserRole).keys():
                return e.data(Qt.UserRole)[name]

        count = self.list_widget.count()
        if count == 0:
            return
        global current_work_directory
        cnt = 0
        for i in range(count):
            e = self.list_widget.item(i)
            if e is not None and e.data(Qt.UserRole) is not None:
                what = getItem('what',e)
                ori_what = getItem('ori_what', e)
                who = getItem('who', e)
                text = getItem('text', e)
                file_name = getItem('file_name', e)
                line_number = getItem('line_number', e)
                lookup_lan = getItem('lookup_lan', e)
                if text is None or file_name is None or lookup_lan is None or line_number is None:
                    continue
                file_name = current_work_directory+'/'+file_name
                is_file_name_to_tl = False
                if file_name.startswith('game/tl/'):
                    tl_target = file_name
                    path, filename = os.path.split(file_name)
                    game_target = path + '/../../'+filename
                    is_file_name_to_tl = True
                else:
                    game_target = file_name
                    path, filename = os.path.split(file_name)
                    tl_target = path + '/tl/' + lookup_lan + '/' + filename

                if os.path.isfile(game_target):
                    if ori_what is not None:
                        replace_line(game_target, line_number, ori_what, text)

                is_tl_target_replaced = False
                if os.path.isfile(tl_target):
                    if is_file_name_to_tl:
                        if who is not None:
                            replace_line(tl_target, line_number,who,text)
                        if what is not None:
                            replace_line(tl_target, line_number,what,text)
                        is_tl_target_replaced = True
                    else:
                        try:
                            f = open(tl_target, 'r',encoding='utf-8')
                            content = f.read()
                            replaced_content = content
                            f.close()
                            if who is not None:
                                replaced_content = content.replace(who,text)
                            if what is not None:
                                replaced_content = content.replace(what,text)
                            f = open(tl_target, 'w',encoding='utf-8')
                            f.write(replaced_content)
                            f.close()
                            if replaced_content != content:
                                is_tl_target_replaced = True
                        except Exception:
                            pass

                if not is_tl_target_replaced:
                    tl_dir = os.path.dirname(tl_target)
                    paths = os.walk(tl_dir, topdown=False)
                    for path, dir_lst, file_lst in paths:
                        for file_name in file_lst:
                            i = os.path.join(path, file_name)
                            if not file_name.endswith("rpy"):
                                continue
                            come = None
                            to = text
                            if who is not None:
                                come = who
                            if what is not None:
                                come = what
                            t = replaceThread(cnt, i, come,text)
                            t.start()
                            replace_threads.append(t)
                            cnt = cnt + 1

        if len(replace_threads) > 0:
            open('replacing', "w")
            self.replaceButton.setText('replacing...')
            self.replaceButton.setDisabled(True)
            _thread.start_new_thread(self.replace_threads_over, ())

        self.list_widget.clear()

        if self.autoReloadCheckBox.isChecked():
            self.reload_scirpts()

    @staticmethod
    def replace_threads_over():
        for t in replace_threads:
            t.join()
        if os.path.isfile('replacing'):
            os.remove('replacing')

    def reload_scirpts(self):
        try:
            global reload_check_file_path
            io.open(reload_check_file_path, 'w', encoding='utf-8')
        except Exception:
            pass
        try:
            os.remove(json_path)
        except Exception:
            pass
        self.oriWhatTextEdit.setText('')
        self.currentWhatTextEdit.setText('')
        self.wholineEdit.setText('')

    def current_what_edit_click(self):
        dialog = MyInputDialog(self)
        dialog.label1.setText('ori_what')
        dialog.label2.setText('edit_what')
        dialog.setWindowTitle('Input Dialog')
        dialog.text_edit.setText(self.currentWhatTextEdit.toPlainText())
        dialog.text_edit.setFocus()
        dialog.text_edit.selectAll()
        dic = dict()
        what = get_from_last_data('what')
        lookup_lan = get_from_last_data('lookup_lan')
        file_name = get_from_last_data('file_name')
        line_number = get_from_last_data('line_number')
        if what is not None:
            dic['what'] = what
            dic['lookup_lan'] = lookup_lan
            dic['file_name'] = file_name
            dic['line_number'] = line_number
            item = QListWidgetItem()
            dialog.text_edit_ori.setText(dic['what'])
            is_item_exist = False
            count = self.list_widget.count()
            for i in range(count):
                e = self.list_widget.item(i)
                if e is not None and e.data(Qt.UserRole) is not None and 'what' in e.data(Qt.UserRole).keys():
                    if e.data(Qt.UserRole)['what'] != dic['what']:
                        continue
                    else:
                        is_item_exist = True
                        self.list_widget.takeItem(i)
                        break

            if dialog.exec():
                text = dialog.getText()
                dic['text'] = text
                item.setText(dic['what'] + '-->' + text)
                item.setData(Qt.UserRole, dic)
                if not (self.currentWhatTextEdit.toPlainText() == text and is_item_exist or text == dic['what']):
                    self.list_widget.addItem(item)
                self.currentWhatTextEdit.setText(text)


    def ori_what_edit_click(self):
        dialog = MyInputDialog(self)
        dialog.label1.setText('ori_what')
        dialog.label2.setText('edit_what')
        dialog.setWindowTitle('Input Dialog')
        dialog.text_edit.setText(self.oriWhatTextEdit.toPlainText())
        dialog.text_edit.setFocus()
        dialog.text_edit.selectAll()
        dic = dict()
        ori_what = get_from_last_data('ori_what')
        lookup_lan = get_from_last_data('lookup_lan')
        file_name = get_from_last_data('file_name')
        line_number = get_from_last_data('line_number')
        if ori_what is not None:
            dic['ori_what'] = ori_what
            dic['lookup_lan'] = lookup_lan
            dic['file_name'] = file_name
            dic['line_number'] = line_number
            item = QListWidgetItem()
            dialog.text_edit_ori.setText(dic['ori_what'])
            is_item_exist = False
            count = self.list_widget.count()
            for i in range(count):
                e = self.list_widget.item(i)
                if e is not None and e.data(Qt.UserRole) is not None and 'ori_what' in e.data(Qt.UserRole).keys():
                    if e.data(Qt.UserRole)['ori_what'] != dic['ori_what']:
                        continue
                    else:
                        is_item_exist = True
                        self.list_widget.takeItem(i)
                        break

            if dialog.exec():
                text = dialog.getText()
                dic['text'] = text
                item.setText(dic['ori_what'] + '-->' + text)
                item.setData(Qt.UserRole, dic)
                if not (self.oriWhatTextEdit.toPlainText() == text and is_item_exist or text == dic['ori_what']):
                    self.list_widget.addItem(item)
                self.oriWhatTextEdit.setText(text)


    def who_edit_click(self):
        dialog = MyInputDialog(self)
        dialog.label1.setText('ori_who')
        dialog.label2.setText('edit_who')
        dialog.setWindowTitle('Input Dialog')
        dialog.text_edit.setText(self.wholineEdit.text())
        dialog.text_edit.setFocus()
        dialog.text_edit.selectAll()
        dic = dict()
        who = get_from_last_data('who')
        lookup_lan = get_from_last_data('lookup_lan')
        file_name = get_from_last_data('file_name')
        line_number = get_from_last_data('line_number')
        if who is not None:
            dic['who'] = who
            dic['lookup_lan'] = lookup_lan
            dic['file_name'] = file_name
            dic['line_number'] = line_number
            item = QListWidgetItem()
            dialog.text_edit_ori.setText(dic['who'])
            is_item_exist = False
            count = self.list_widget.count()
            for i in range(count):
                e = self.list_widget.item(i)
                if e is not None and e.data(Qt.UserRole) is None and 'who' in e.data(Qt.UserRole).keys():
                    if e.data(Qt.UserRole)['who'] != dic['who']:
                        continue
                    else:
                        is_item_exist = True
                        self.list_widget.takeItem(i)
                        break

            if dialog.exec():
                text = dialog.getText()
                dic['text'] = text
                item.setText(dic['who'] + '-->' + text)
                item.setData(Qt.UserRole, dic)
                if not (self.wholineEdit.text() == text and is_item_exist or text == dic['who']):
                    self.list_widget.addItem(item)
                self.wholineEdit.setText(text)


    def update_log(self):
        thread = self.UpdateThread()
        thread.update_sig.connect(self.update_progress)
        while True:
            if self.is_end:
                return
            thread.start()
            time.sleep(0.1)

    def update_progress(self, data):
        if os.path.isfile('replacing'):
            self.replaceButton.setText('replacing...')
            self.replaceButton.setDisabled(True)
        else:
            self.replaceButton.setText('Replace to file(s)')
            self.replaceButton.setEnabled(True)

        global last_data
        if data != last_data:
            last_data = data
            try:
                js = json.loads(data)
                if 'cur_id' in js.keys():
                    cur_id = js['cur_id']
                    if cur_id in js.keys():
                        cur_id = js[cur_id]
                        if 'who' in cur_id.keys():
                            self.wholineEdit.setText(cur_id['who'])
                        if 'ori_what' in cur_id.keys():
                            self.oriWhatTextEdit.setText(cur_id['ori_what'])
                            self.oriWhatTextEdit.moveCursor(QTextCursor.End)
                        if 'what' in cur_id.keys():
                            self.currentWhatTextEdit.setText(cur_id['what'])
                            self.currentWhatTextEdit.moveCursor(QTextCursor.End)
            except Exception:
                pass

    class UpdateThread(QThread):
        update_sig = Signal(str)

        def __init__(self):
            super().__init__()

        def __del__(self):
            self.wait()

        def run(self):
            if os.path.isfile(json_path):
                try:
                    f = io.open(json_path, 'r+', encoding='utf-8')
                    read = f.read()
                    f.close()
                    self.update_sig.emit(read)
                except Exception:
                    pass


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('main.ico'))
        self.onlyCheckBox.setChecked(True)
        self.refreshCheckBox.setChecked(True)
        self.init_combobox()
        self.refreshButton.clicked.connect(self.init_combobox)
        self.startButton.clicked.connect(self.start)
        self.onlyCheckBox.stateChanged.connect(self.onlycheckbox_changed)
        self.versionLabel.setStyleSheet("color:grey")
        self.copyrightLabel.setStyleSheet("color:grey")
        self.actioncopyright.triggered.connect(lambda: self.show_copyright_form())
        self.logButton.clicked.connect(self.open_log_file)

    def open_log_file(self):
        subprocess.Popen('notepad ' + log_path)

    def show_copyright_form(self):
        copyright_form = MyCopyrightForm(parent=self)
        copyright_form.exec()


    def onlycheckbox_changed(self,state):
        self.init_combobox()

    def start(self):
        if self.processComboBox.currentIndex() < 0:
            return
        dic = combobox_dic[self.processComboBox.currentIndex()]
        cwd = dic['cwd']
        if 'dir' in dic.keys():
            cwd = dic['dir']
        global reload_check_file_path
        global current_work_directory
        current_work_directory = cwd
        reload_check_file_path = cwd + '/' + reload_check_file_name
        if not os.path.isfile(cwd + '/game/' + rpy_file_name + 'c') or not compare_files(cwd + '/game/' + rpy_file_name,rpy_file_name):
            shutil.copyfile(rpy_file_name, cwd + '/game/' + rpy_file_name)
            p = psutil.Process(dic['pid'])
            p = reboot_process(p,cwd)

        runtime_form = MyRuntimeForm(parent=self)
        self.hide()
        if os.path.isfile(json_path):
            try:
                os.remove(json_path)
            except Exception:
                pass
        global last_data
        last_data = None
        runtime_form.exec()
        self.show()
        if self.refreshCheckBox.isChecked():
            self.init_combobox()

    def init_combobox(self):
        combobox_dic.clear()
        self.processComboBox.clear()
        l = get_all_process(not self.onlyCheckBox.isChecked())
        for i, e in enumerate(l):
            combobox_dic[i] = e
            if 'dir' in e.keys():
                self.processComboBox.addItem(e['name'] + '\t' + e['dir'])
            else:
                self.processComboBox.addItem(e['name'])


def reboot_process(p,cwd):
    p.kill()
    p = subprocess.Popen(p.cmdline(),cwd=cwd)
    return p


def get_all_process(is_get_all=False):
    pids = psutil.pids()
    l = []
    for pid in pids:
        try:
            p = psutil.Process(pid)
            if is_get_all:
                try:
                    dic = dict()
                    dic['pid'] = pid
                    dic['cwd'] = p.cwd()
                    if len(p.cmdline()) > 2 and os.path.isdir(p.cmdline()[2]) and os.path.isdir(
                            p.cmdline()[2] + '/game'):
                        dic['dir'] = p.cmdline()[2]
                    dic['name'] = p.name()
                    dic['exe'] = p.exe()
                    l.append(dic)
                except Exception:
                    pass
            else:
                if 'pythonw.exe' == p.name().lower():
                    try:
                        if len(p.cmdline()) > 2 and os.path.isdir(p.cmdline()[2]) and os.path.isdir(
                                p.cmdline()[2] + '/game'):
                            dic = dict()
                            dic['pid'] = pid
                            dic['cwd'] = p.cwd()
                            dic['dir'] = p.cmdline()[2]
                            dic['name'] = p.name()
                            dic['exe'] = p.exe()
                            l.append(dic)
                    except Exception:
                        pass
                try:
                    name, ext = os.path.splitext(p.exe())
                    # print(name)
                    if os.path.isfile((name + '.py')) and os.path.isdir(p.cwd() + '/' + 'game') and os.path.isdir(
                            p.cwd() + '/' + 'renpy'):
                        dic = dict()
                        dic['pid'] = pid
                        dic['name'] = p.name()
                        dic['cwd'] = p.cwd()
                        dic['exe'] = p.exe()
                        l.append(dic)
                except Exception:
                    pass
        except Exception:
            pass

    return l

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec())
