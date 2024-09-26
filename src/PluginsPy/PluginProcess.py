import threading
import multiprocessing

def runPlugin(**kwargs):
    print("runPlugin")

    print(kwargs)

class PluginProcess(threading.Thread):

    def __init__(self, kwargs):
        super().__init__()
        self.kwargs = kwargs

    def run(self):
        print("PluginProcess running")

        p = multiprocessing.Process(target=runPlugin, kwargs=self.kwargs)
        p.start()
        p.join()
