Actions = [
    {
        "examples": ["привет", "здравствуй", "добрый день",
            "hello", "good morning"],
        "responses": "greeting"
    },
    {
        "examples": ["пока", "до свидания", "увидимся", "до встречи",
            "goodbye", "bye", "see you soon"],
        "responses": "quit"
    },
    {
        "examples": ["найди в гугл",
            "search on google", "google", "find on google"],
        "responses": "search_google"
    }
]

class Parser(object):
    def __init__(self):
        pass
    
    def Parse(self, data):
        InputData = data.strip().split(" ")
        print(InputData)
        for i in Actions:
            if i['examples'] in InputData:
                print(i['responses'])
                return {
                    'Action': i['responses'], 
                    'Data': InputData.pop(0)
                    }