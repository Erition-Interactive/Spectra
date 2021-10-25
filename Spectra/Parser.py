from . import ExecuteManager
import json, os

Actions = []
Actions_path = os.path.dirname(os.path.abspath(__file__)) + "/Data/Actions.json"

with open(Actions_path, encoding='utf-8') as f:
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