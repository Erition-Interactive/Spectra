from . import Parser
from . import AudioListen

import asyncio
import time
import json, requests


debug = 0
mode = 0
InputParser = Parser.Parser()


async def GetNewVersion():
    response = requests.get('https://erition-interactive.github.io/Spectra/Spectra/Data/Config.json')
    print(response.text)


async def AutoUpdate():
    OldConfig = []
    NewConfig = []

    with open('Data/Config.json') as f:
        OldConfig = json.load(f)


class Assistant(object):
    def __init__(self, debug = False, mode = 1, autoupdate=True):
        print("Spectra 1.0")
        
        if debug:
            print("[Assistant.py] Debug is Active! Mode = {}".format(mode))

    def Read(self, data):
        args = InputParser.Parse(data)

    def Start(self):
        print("Spectra ready")
        #asyncio.run(AudioListen.Listen())
        print(AudioListen.Listen())
