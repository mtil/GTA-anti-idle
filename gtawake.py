from pywinauto.application import Application
from pywinauto.findwindows import find_window

import time

def limitOn():

    # app = Application().connect(process=(GTA_PID))
    hello = find_window(best_match='Grand Theft Auto V')
    app = Application().connect(handle=hello)
    win = app.window(title='Grand Theft Auto V')

    win.SetFocus()
    time.sleep(10)
    win.TypeKeys('{w down}')
    win.TypeKeys('{d down}')

    win.TypeKeys('{w up}')
    win.TypeKeys('{d up}')

    print('Walking Forward')


isRunning = True

while True:

    limitOn()
    time.sleep(1)
