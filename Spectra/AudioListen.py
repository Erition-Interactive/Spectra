import pyttsx3
import speech_recognition as sr
from . import ExecuteManager

Execute = ExecuteManager.Execute(debug=True)

Actions = [
    {
        "examples": ["привет", "здравствуй", "добрый день",
            "hello", "good morning"],
        "responses": "print('Ну привет')"
    },
    {
        "examples": ["пока", "до свидания", "увидимся", "до встречи",
            "goodbye", "bye", "see you soon"],
        "responses": "exit()"
    },
    {
        "examples": ["найди в гугл",
            "search on google", "google", "find on google"],
        "responses": "print('Гугл тебе заблокировали? Сам ищи')"
    }
]

def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=2) #настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: {query.lower()}')
        for i in Actions:
            for x in i['examples']:
                if x.lower() in text:
                    Execute.Exec(action=i['responses'], data=None)
                    break
    except Exception as E:
        print('AudioListener error: {}'.format(E))

    while True:
        record_volume()
#async def Listen():
def Listen():
    print("Listen")
    record_volume()