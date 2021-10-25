from . import Parser
from . import AudioListen

import asyncio
import time


debug = 0
mode = 0
InputParser = Parser.Parser()


class Assistant(object):
    def __init__(self, debug = False, mode = 1):
        print("Spectra 1.0")
        
        if debug:
            print("[Assistant.py] Debug is Active! Mode = {}".format(mode))

    def Read(self, data):
        args = InputParser.Parse(data)

    def Start(self):
        print("Spectra ready")
        #asyncio.run(AudioListen.Listen())
        print(AudioListen.Listen())
