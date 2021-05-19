import os

def getMeta():
    moduleDir = os.path.realpath(os.path.join(os.path.dirname(__file__)))

    about = {}
    with open(os.path.join(moduleDir, "__about__.py")) as f:
        exec (f.read(), about)

    return about
