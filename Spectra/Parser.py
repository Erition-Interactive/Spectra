from . import ExecuteManager
import json

Actions = []

with open('Data/Actions.json') as f:
    Actions = json.load(f)


Execute = ExecuteManager.Execute(debug=True)


class Parser(object):
    def __init__(self):
        pass
    
    def Parse(self, data):
        for i in Actions:
            for x in i['examples']:
                if x.lower() in data:
                    return [i['responses'], None]
        return ["null", None]