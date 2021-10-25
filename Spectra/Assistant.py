from . import Parser
from . import AudioListen

from github import Github
import asyncio
import time
import json, requests, os


debug = 0
mode = 0
Config_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/Config.json"


async def GetNewVersion():
    response = requests.get('https://erition-interactive.github.io/Spectra/Spectra/Data/Config.json')
    return response.text


def AutoUpdate():
    OldConfig = []
    NewConfig = []

    with open(Config_path) as f:
        OldConfig = json.load(f)
    NewConfig = json.loads(asyncio.run(GetNewVersion()))
    if OldConfig['Version'] != NewConfig['Version']:
        print("Нужна обнова...")
        g = Github()
        repo = g.get_repo("Erition-Interactive/Spectra")
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                print(file_content)
    


class Assistant(object):
    def __init__(self, debug = False, mode = 1, autoupdate=True):
        print("Spectra 1.0")
        
        if debug:
            print("[Assistant.py] Debug is Active! Mode = {}".format(mode))
        if autoupdate:
            AutoUpdate()

    def Read(self, data):
        args = InputParser.Parse(data)

    def Start(self):
        print("Spectra ready")
        #asyncio.run(AudioListen.Listen())
        print(AudioListen.Listen())
