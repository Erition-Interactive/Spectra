import speech_recognition as sr

#async def Listen():
def Listen():
    print("Listen")
    i = sr.Recognizer()
    with sr.Microphone() as source: # with sr.Microphone(device_index = 0) as source:
        audio = i.listen(source) 
        text = i.recognize_google(audio, language="ru-RU") # .lower() --> маленькие буквы
        return text