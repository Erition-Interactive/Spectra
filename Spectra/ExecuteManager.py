
class Execute:
    def __init__(self, debug = False, mode = 1):
        if debug:
            print("Debug is Active! Mode = {}".format(mode))

    def Echo(self, text):
        print("Spectra: {}".format(text))