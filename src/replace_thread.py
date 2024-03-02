import threading

replace_threads = []
class replaceThread(threading.Thread):
    def __init__(self, threadID, p, come,to):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.p = p
        self.come = come
        self.to = to

    def run(self):
        if self.come is None:
            return
        try:
            self.replace_single(self.p, self.come, self.to)
        except Exception as e:
            pass

    def replace_single(self,p,come,to):
        #print(p,come,to)
        f = open(p, 'r',encoding='utf-8')
        content = f.read()
        f.close()
        replaced_content = content.replace(come, to)
        f = open(p, 'w',encoding='utf-8')
        f.write(replaced_content)
        f.close()