class Execute:
    def __init__(self, debug = False, mode = 1):
        if debug:
            print("[ExecuteManager.py] Debug is Active! Mode = {}".format(mode))

    def Echo(self, text):
        print("Spectra: {}".format(text))
    
    def Exec(self, action, data):
        pass