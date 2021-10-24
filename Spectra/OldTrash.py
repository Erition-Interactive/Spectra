import pyttsx3
from translate import Translator
import os
import sys
import time
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr
from input import lol
def exe():
   # os.system("cls")

    greeting_out = ['Привет', 'И тебе привет','Здравствуй','Хай','Здарова', 'Салют', 'И тебе здравствуй']

    try: 
        print ('Скажите что-нибудь...')
        i = sr.Recognizer()
        with sr.Microphone() as source: # with sr.Microphone(device_index = 0) as source:
         audio = i.listen(source) 
        text = i.recognize_google(audio, language="ru-RU") # .lower() --> маленькие буквы
        print ('Вы: ' + text)
        
        file = open('C://Users//egork//name.txt', 'w')
        file.write(text)
        file.close()

        if 'маша' in text:

            if 'стоп' in text:
                print ('маша: как скажете')
                engine = pyttsx3.init()
                engine.say ('Как скажете')
                engine.runAndWait()
                os.abort() # sys.exit()

            if 'найди' in text or 'ищи' in text:
                zapros = text.replace ('найди', '')
                zapros = zapros.replace ('маша', '')
                zapros = zapros.replace ('ищи', '')
                zapros = zapros.replace ('мне', '')
                zapros = zapros.replace ('давай', '')
                zapros = zapros.replace ('пожалуйста', '') 
                zapros = zapros.replace ('нам', '')
                zapros = zapros.strip ()            
                print ('Маша: уже ищу...')
                engine = pyttsx3.init()
                engine.say ('Уже ищу')
                engine.runAndWait()  
                print (zapros)
                webbrowser.open('https://www.google.com/search?ei=iAnOX9LOMOnyqwG7ko6gBw&q=' + zapros + '&oq=' + zapros + '&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyBAgAEEMyAggAMgIIADIECAAQQzIFCAAQsQNQgfjUAlj0-dQCYOKB1QJoAXABeACAAd4DiAHeA5IBAzQtMZgBAKABAaoBB2d3cy13aXqwAQDAAQE&sclient=psy-ab&ved=0ahUKEwjSsu6H2rvtAhVp-SoKHTuJA3QQ4dUDCA0&uact=5')
                time.sleep(1)
                print ('Маша: вот что мне удалось найти по вашему запросу:')
                engine = pyttsx3.init()
                engine.say ('Вот что мне удалось найти по вашему запросу')
                engine.runAndWait() 

            if 'что такое' in text or 'кто такой' in text:
                wiki = text.replace ('маша', '')
                wiki = wiki.replace ('мне', '')
                wiki = wiki.replace ('скажи', '')
                wiki = wiki.replace ('пожалуйста', '')
                wiki = wiki.replace ('нам', '')
                wiki = wiki.replace ('что такое', '')
                wiki = wiki.replace ('кто такой', '')
                wiki = wiki.strip ()
                print ('Маша: Секундочку...')
                webbrowser.open('https://www.google.com/search?ei=iAnOX9LOMOnyqwG7ko6gBw&q=' + wiki + '&oq=' + wiki + '&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyBAgAEEMyAggAMgIIADIECAAQQzIFCAAQsQNQgfjUAlj0-dQCYOKB1QJoAXABeACAAd4DiAHeA5IBAzQtMZgBAKABAaoBB2d3cy13aXqwAQDAAQE&sclient=psy-ab&ved=0ahUKEwjSsu6H2rvtAhVp-SoKHTuJA3QQ4dUDCA0&uact=5')
                time.sleep(1)
                result = wikipedia.summary(wiki)
                print ('Маша:' + result)
                engine = pyttsx3.init()
                engine.say (result)
                engine.runAndWait()    

            if 'открой' in text:   
            
                if 'новости'  in text:
                    time.sleep(1)
                    print ('Маша: Уже открываю...')
                    engine = pyttsx3.init()
                    engine.say ('Eже открываю')
                    engine.runAndWait()
                    webbrowser.open ('https://yandex.ru/news?msid=1634412135.39619.82815.551379&mlid=1634411690.glob_225&utm_source=morda_desktop&utm_medium=topnews_news')

            if text in greeting_in:
                i = random.choice(greeting_out)
                print ('Маша: ' + farewell)
                engine = pyttsx3.init()
                engine.say (farewell)
                engine.runAndWait()

            if 'английский' in text or 'английскии'in text:
                tran = text.replace ('маша', '')
                tran = tran.replace ('переведи', '')
                tran = tran.replace ('давай', '')
                tran = tran.replace ('пожалуйста', '')
                tran = tran.replace ('на английский', '')
                tran = tran.replace ('нам', '')
                tran = tran.replace ('по английски', '')
                tran = tran.replace ('мне', '')
                tran = tran.replace ('как будет', '')
                tran = tran.replace ('по английски', '')
                tran = tran.replace ('на английском', '')
                tran = tran.strip()
                translation = Translator (from_lang = "ru", to_lang = "en")
                result = translation.translate (tran)
                print ('Маша: уже перевожу...')
                engine = pyttsx3.init()
                engine.say ('Уже перевожу')
                engine.runAndWait()            
                time.sleep(1)
                print ('RU --> EN')
                print (tran + ' --> ' + result)
                engine = pyttsx3.init()
                engine.say ('Маша: на английском языке ' + tran + ' будет: ' + result)
                engine.runAndWait() 
        
            if 'фильм' in text: 
                print ('lol')
                film = text.replace ('включи', '')
                film = film.replace ('фильм', '')
                film = film.replace ('давай', '') 
                film = film.replace ('пожалуйста', '') 
                film = film.replace ('маша', '')
                film = film.strip ()
                time.sleep(1)
                print (film)
                print ('Маша: уже включаю...')
                engine = pyttsx3.init()
                engine.say ('Уже включаю')
                engine.runAndWait() 
                os.startfile(F"C://users//egork//{film}.txt")


            #file = open('C://Users//egork//name..txt', 'r')
           # res = file.read()
           # file.close()





    except:
    	exe()

while True:
    exe()