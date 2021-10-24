from . import ExecuteManager

debug = 0
mode = 0
TaskExec = ExecuteManager.Execute()

class Assistant(object):
    def __init__(self, debug = False, mode = 1):
        print("Spectra 1.0")
        TaskExec = ExecuteManager.Execute(debug = debug, mode = mode)
        
        if debug:
            print("Debug is Active! Mode = {}".format(mode))

    def Read(self, data):
        TaskExec.Echo(text = data)

    def Start(self):
        print("Spectra ready")
        while True:
            Assistant.Read(self, data = input())

    