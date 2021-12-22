import inspect
from os import walk

def getFiles(path) :
    for (dirpath, dirnames, filenames) in walk(path) :
        dirpath = dirpath
        dirnames = dirnames
        filenames = filenames
        return filenames

    return []

def getPluginFiles(dirpath):
    return getFiles(dirpath)

def getClassMethods(clazz):
    methods = dict()
    for item in dir(clazz):
        if item.startswith("_"):
            continue

        method = getattr(clazz, item)
        methods[item] = [str(method.__doc__).strip()] 
    
    return methods

def addRun(clazz):

    @classmethod
    def run(clazz, kwargs):
        """
        使用装饰的方法给Plugin进行统一添加该方法，便于统一修改
        """

        print(">>> enter plugin run method")
        # print("cmd line args: " + str(kwargs))
        if len(inspect.signature(getattr(clazz, "__init__")).parameters) == 2: 
            obj = clazz(kwargs)
        else:
            obj = clazz()

        invert_op = getattr(obj, "start", None)
        if callable(invert_op):
            print(">>> enter plugin start method")
            if len(inspect.signature(invert_op).parameters) > 0:
                invert_op(kwargs)
            else:
                invert_op()
            print("<<< end plugin start method")
        print("<<< end plugin run method")

    # print(">>> start add plugin run method")
    setattr(clazz, 'run', run)
    # print(dir(clazz))
    # items = getClassMethods(clazz)
    # for item in items:
    #     if item == "run":
    #         print(item + ": " + items[item][0])
    # print("<<< end add plugin run method")

    return clazz

if __name__ == "__main__" :
    print("main")
