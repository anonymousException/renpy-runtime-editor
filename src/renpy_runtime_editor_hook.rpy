init python:
    import tempfile
    import inspect
    import io
    import json
    import time
    renpy_runtime_editor_hook_file_name = tempfile.gettempdir()+'/'+'renpy_runtime_editor'+'_hooked.json'
    reload_check_file_name = 'renpy_runtime_editor.reload'
    my_old_lookup = renpy.ast.Translate.lookup
    my_old_reload_script = renpy.reload_script
    my_old_show_screen = renpy.show_screen
    my_old_hide_screen = renpy.hide_screen

    def get_translation_identifier():
        """
        :doc: translation_functions

        Returns the translation identifier for the current statement.
        """

        ctx = renpy.game.contexts[-1]
        return ctx.translate_identifier or ctx.deferred_translate_identifier

    def reload():
        if os.path.isfile(reload_check_file_name):
            os.remove(reload_check_file_name)
            try:
                os.remove(renpy_runtime_editor_hook_file_name)
            except Exception:
                pass
            renpy.reload_script()

    config.interact_callbacks.append(reload)

    def listen_reload(wait):
        while(True):
            if os.path.isfile(reload_check_file_name):
                renpy.restart_interaction()
            time.sleep(wait)
    renpy.invoke_in_thread(listen_reload, 1)

    def my_hide_screen(tag, layer=None):
        if tag == 'director':
            renpy.ast.Translate.lookup = my_lookup
        my_old_hide_screen()

    def my_show_screen(_screen_name, *_args, **kwargs):
        if _screen_name == 'director':
            renpy.ast.Translate.lookup = my_old_lookup
        my_old_show_screen(_screen_name, *_args, **kwargs)

    renpy.show_screen = my_show_screen

    def my_reload_script():
        renpy.config.skipping = None
        renpy.ast.Translate.lookup = my_old_lookup
        reload_action = renpy.exports.curried_call_in_new_context("_save_reload_game")
        reload_action()
        renpy.ast.Translate.lookup = my_lookup

    renpy.reload_script = my_reload_script

    def my_lookup(self):
        ori_language = renpy.game.preferences.language 
        renpy.game.preferences.language = None
        ori_rv = my_old_lookup(self)
        renpy.game.preferences.language = ori_language
        rv = my_old_lookup(self)
        d = renpy.get_filename_line()
        if os.path.isfile(renpy_runtime_editor_hook_file_name) and os.path.getsize(renpy_runtime_editor_hook_file_name):
            f = io.open(renpy_runtime_editor_hook_file_name, 'r', encoding='utf-8')
            loaded_data = json.load(f)
            f.close()
            loaded_data[self.identifier] = {"ori_what":ori_rv.what,"what":rv.what,"lookup_lan":renpy.game.preferences.language,"file_name":d[0],"line_number":d[1]}
            with io.open(renpy_runtime_editor_hook_file_name,'w',encoding="utf-8") as outfile:
                outfile.write(unicode(json.dumps(loaded_data, ensure_ascii=False)))
            f.close()
        else:
            dic = dict()
            dic[self.identifier] = {"ori_what":ori_rv.what,"what":rv.what,"lookup_lan":renpy.game.preferences.language,"file_name":d[0],"line_number":d[1]}
            with io.open(renpy_runtime_editor_hook_file_name,'w',encoding="utf-8") as outfile:
                outfile.write(unicode(json.dumps(dic, ensure_ascii=False)))
        return rv

    renpy.ast.Translate.lookup = my_lookup


    def my_hook(event, **kwargs):
        if event == "begin":
            d = renpy.get_filename_line()
            e = inspect.currentframe().f_back.f_locals

            if os.path.isfile(renpy_runtime_editor_hook_file_name) and os.path.getsize(renpy_runtime_editor_hook_file_name):
                f = io.open(renpy_runtime_editor_hook_file_name, 'r', encoding='utf-8')
                loaded_data = json.load(f)
                f.close()
                cur_id = get_translation_identifier()
                if cur_id not in loaded_data.keys():
                    return
                item = loaded_data[cur_id]
                if 'who' not in loaded_data.keys():
                    loaded_data['who'] = [e.get("who")]
                item['who']=e.get("who")
                loaded_data['cur_id'] = cur_id
                global hook_last_translate_id
                if hook_last_translate_id is not None and hook_last_translate_id != cur_id and hook_last_translate_id in loaded_data.keys():
                    loaded_data.pop(hook_last_translate_id)
                hook_last_translate_id = cur_id
                with io.open(renpy_runtime_editor_hook_file_name,'w',encoding="utf-8") as outfile:
                    outfile.write(unicode(json.dumps(loaded_data, ensure_ascii=False)))
            else:
                pass
                

    config.all_character_callbacks.append(my_hook)
define hook_last_translate_id = None
define config.developer = True