from . import ExecuteManager
from . import Parser

debug = 0
mode = 0
TaskExec = ExecuteManager.Execute()
InputParser = Parser.Parser()
class Assistant(object):
    def __init__(self, debug = False, mode = 1):
        print("Spectra 1.0")
        TaskExec = ExecuteManager.Execute(debug = debug, mode = mode)
        
        if debug:
            print("Debug is Active! Mode = {}".format(mode))

    def Read(self, data):
        args = InputParser.Parse(data)
        print(args)
        TaskExec.Exec(action = args['Action'], data = ['Data'])

    def Start(self):
        print("Spectra ready")
        while True:
            Assistant.Read(self, data = input())

    