import pyttsx3
import speech_recognition as sr
from . import ExecuteManager
from . import Parser

Parse = Parser.Parser()
Execute = ExecuteManager.Execute(debug=True)



def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=1) #настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: {query.lower()}')
        parsed = Parse.Parse(data=text)
        Execute.Exec(action=parsed[0], data=parsed[1])
        
    except Exception as E:
        print('AudioListener error: {}'.format(E))

    while True:
        record_volume()
#async def Listen():
def Listen():
    print("Listen")
    record_volume()