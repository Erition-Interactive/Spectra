import os, time, datetime

global debug

class AssistantAI(object):
    def __init__(self, debug = False):
        print("Spectra 1.0")

        if debug:
            print("Debug is Active!")
    def Start(self):
        print("Spectra ready")