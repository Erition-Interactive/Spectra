import pyttsx3
import selenium
import wikipedia  
import os
import time
from translate import Translator
import webbrowser
import subprocess
import datetime
import random
import sys
import datetime
from playsound import *
import speech_recognition as sr



#years_old = ['К счатью или к сожалению, но я этого пока не знаю', 'К счатью или к сожалению я этого не знаю.', 'Между прочим спрашивать у дамы про ее возраст неприлично.']

name_out = ['Да да, я вас слушаю','Я тут, говорите','Я вас слушаю, говорите']



greeting_in = ['привет', 'здравйствуйте','здравствуй','хай','здарова', 'салют', 'добрый день', 'добрый вечер', 'доброе утро', 'приветики', 'привет спектра', 'спектра привет']

greeting_out = ['Привет', 'И тебе привет','Здравствуй','Хай','Здарова', 'Салют', 'И тебе здравствуй']



farewell_in = ['пока', 'досвидос', 'удачи','до свидания','всего хорошего','до встречи', 'до скорой встречи', 'еще увидимся', 'увидимся', 'всего наилучшего', 'все давай', 'все давай пока', 'давай пока', 'бывай', 'прощай', 'увидимя', 'еще увидимся']

farewell_out = ['Пока','Удачи','До свидания','Всего хорошего','До встречи', 'До скорой встречи', 'Еще увидимся', 'Увидимся', 'Всего наилучшего']



apology_in = ['прошу прощения', 'извини', 'прости', 'извини пожалуйста', 'прости пожалуйста', 'извини меня пожалуйста', 'прости прости пожалуйста', 'сорян', 'извините']

apology_out = ['Вы не в чем не виноваты', 'Вам незачем извиняться', 'Вам незачто извиняться']



holiday_in = ['у меня сегодня праздник', 'у меня сегодня говодщина', 'у нас сегодня годовщина', 'у меня сегодня день рождения']



affairs_in = ['как у тебя дела', 'как твои дела', 'как твои дела', 'как поживаешь', 'как жизнь', 'как дела']

affairs_out = ['У меня все отлично а у вас как','У меня все прекрасно, а как ваши дела','У меня все хорошо, а как у вас','Все супер','Все прекрасно','Все отлично', 'Мои дела хорошо, а как ваши', 'Все прекрасно']




time_in = ['сколько сейчас времени', 'какой сейчас час', 'сколько времени', 'какое сейчас время']

date_in = ['какой сегодня день', 'какое сегодня число', 'какая сейчас дата']

month_in = ['какой сейчас месяц', 'какой сейчас идет месяц', 'какой сейчас по счету месяц', 'какой сейчас идет по счету месяц', 'какой сейчас месяц года']

year_in = ['какой сейчас год', 'какй сейчас на дворе год', 'какойй сейчас идет год']


now = datetime.datetime.now()

wikipedia.set_lang("ru")
    

def exe():


    print (' ')
    print ('Как вы хотите обратиться к голосовому ассистенту?')
    print ('1. Написать')
    print ('2. Сказать')

    x = int(input())



    if x == 2:

        try:

            print ('Скажите что-нибудь...')


            r = sr.Recognizer()

            with sr.Microphone(device_index = 0) as source:

             audio = r.listen(source) 

            text = r.recognize_google(audio, language="ru-RU").lower()


            print (text)




        except:

            print ('Ошибка. Речь не была распопзнана. Попробуйте еще раз.')
            print (' ')
            print ('Скажите что-нибудь...')


            r = sr.Recognizer()

            with sr.Microphone(device_index = 0) as source:

             audio = r.listen(source) 

            text = r.recognize_google(audio, language="ru-RU").lower()

            print (text)
            

        if 'что такое' in text or 'кто такой' in text:
            wiki = text.replace ('спектра', '')
            wiki = wiki.replace ('мне', '')
            wiki = wiki.replace ('скажи', '')
            wiki = wiki.replace ('пожалуйста', '')
            wiki = wiki.replace ('нам', '')
            wiki = wiki.replace ('что такое', '')
            wiki = wiki.replace ('кто такой', '')
            wiki = wiki.strip ()
            print ('Секундочку...')
            webbrowser.open('https://www.google.com/search?ei=iAnOX9LOMOnyqwG7ko6gBw&q=' + wiki + '&oq=' + wiki + '&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyBAgAEEMyAggAMgIIADIECAAQQzIFCAAQsQNQgfjUAlj0-dQCYOKB1QJoAXABeACAAd4DiAHeA5IBAzQtMZgBAKABAaoBB2d3cy13aXqwAQDAAQE&sclient=psy-ab&ved=0ahUKEwjSsu6H2rvtAhVp-SoKHTuJA3QQ4dUDCA0&uact=5', new = 2)
            time.sleep(1)
            result = wikipedia.summary(wiki)
            print (result)
            engine = pyttsx3.init()
            engine.say (result)
            engine.runAndWait()

        if 'найди' in text or 'ищи' in text:
            zapros = text.replace ('найди', '')
            zapros = zapros.replace ('спектра', '')
            zapros = zapros.replace ('ищи', '')
            zapros = zapros.replace ('мне', '')
            zapros = zapros.replace ('давай', '')
            zapros = zapros.replace ('пожалуйста', '') 
            zapros = zapros.replace ('нам', '')
            zapros = zapros.strip ()            
            print ('Уже ищу...')
            engine = pyttsx3.init()
            engine.say ('уже ищу')
            engine.runAndWait()  
            webbrowser.open('https://www.google.com/search?ei=iAnOX9LOMOnyqwG7ko6gBw&q=' + zapros + '&oq=' + zapros + '&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyBAgAEEMyAggAMgIIADIECAAQQzIFCAAQsQNQgfjUAlj0-dQCYOKB1QJoAXABeACAAd4DiAHeA5IBAzQtMZgBAKABAaoBB2d3cy13aXqwAQDAAQE&sclient=psy-ab&ved=0ahUKEwjSsu6H2rvtAhVp-SoKHTuJA3QQ4dUDCA0&uact=5', new = 2)
            time.sleep(1)
            print ('Вот что мне удалось найти по вашему запросу:')
            engine = pyttsx3.init()
            engine.say ('вот что мне удалось найти по вашему запросу')
            engine.runAndWait()       


        if 'английский' in text or 'английскии'in text:
            tran = text.replace ('спектра', '')
            tran = tran.replace ('переведи', '')
            tran = tran.replace ('давай', '')
            tran = tran.replace ('пожалуйста', '')
            tran = tran.replace ('на английский', '')
            tran = tran.replace ('нам', '')
            tran = tran.replace ('по-английски', '')
            tran = tran.replace ('мне', '')
            tran = tran.replace ('как будет', '')
            tran = tran.replace ('по английски', '')
            tran = tran.replace ('на английском', '')
            tran = tran.strip()
            translation = Translator (from_lang = "ru", to_lang = "en")
            result = translation.translate (tran)
            print ('Перевожу...')
            engine = pyttsx3.init()
            engine.say ('перевожу')
            engine.runAndWait()            
            time.sleep(1)
            print ('RU --> EN')
            print (tran + ' --> ' + result)
            engine = pyttsx3.init()
            engine.say ('На английском языке ' + tran + ' будет: ' + result)
            engine.runAndWait() 


        
        

        if 'песню' in text:
            
            music = text.replace ('включи', '')
            music = music.replace ('песню', '')
            music = music.replace ('давай', '') 
            music = music.replace ('песня', '')
            music = music.replace ('поставь', '')
            music = music.replace ('пожалуйста', '') 
            music = music.replace ('спектра', '')
            music = music.strip ()
            time.sleep(1)
            print ('Уже включаю...')
            engine = pyttsx3.init()
            engine.say ('уже включаю')
            engine.runAndWait()
            os.startfile(F"C:\\Files_for_Spectra_Assistant\\Music\\{music}.mp3") 

        if 'фильм' in text or 'видео' in text:
            film = text.replace ('спектром', '')
            film = text.replace ('включи', '')
            film = film.replace ('фильм', '')
            film = film.replace ('давай', '') 
            film = film.replace ('пожалуйста', '') 
            film = film.replace ('спектра', '')
            film = film.replace ('мне', '')
            film = film.replace ('видео', '')
            film = film.replace ('которое называется', '')
            film = film.replace ('под названием', '')
            film = film.replace ('спектра', '')
            film = film.strip ()
            time.sleep(1)
            print ('Уже включаю...')
            engine = pyttsx3.init()
            engine.say ('уже включаю')
            engine.runAndWait() 
            os.startfile(F"C:\\Files_for_Spectra_Assistant\\Film\\{film}.mp4")
         







        if 'энерджи' in text or 'energy' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.energyfm.ru', new = 2) 
    
        if 'рекорд' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.radiorecord.ru', new = 2) 

        if 'шансон' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://radioshanson.ru', new = 2)
        
        if 'лайк' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.likefm.ru', new = 2)
  
        if 'русское' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://rusradio.ru', new = 2)
  
        if 'ретро' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://retrofm.ru', new = 2)
   
        if 'вести' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://radiovesti.ru', new = 2)
  
        if 'европа' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://europaplus.ru', new = 2)
     
        if 'что ты умеешь' in text:
            print ('Вот что я умею:')
            print ('- Spectra, включи фильм "Зелёная миля"')
            print ('- Spectra, найди где купить цветы в Москве')
            print ('- Spectra, переведи на англйиский: "Красная машина едет по дороге"')
            print ('- Spectra, сколько сейчас времени?"')
            print ('- Spectra, какое сегодня число?"')
            print ('- Spectra, какой сейчас год?"')
            print ('- Spectra, открой статистику по коронавирусу"')
            print ('- Spectra, открой радио "Шансон"')
            print ('- Spectra, кто такой Пушкин?')
            engine = pyttsx3.init()
            engine.say('Вот что я умею')
            engine.runAndWait()


        if text in time_in:
            print (now.strftime('Сейчас ' + '%H:%M:%S'))
            engine = pyttsx3.init()
            engine.say(now.strftime('Сейчас' + '%H' + 'часов' + '%M' + 'минут' + '%S' + 'секунд'))
            engine.runAndWait()

        if text in date_in:
            print (now.strftime('Сегодня ' + '%Y.%m.%d'))
            engine = pyttsx3.init()
            engine.say(now.strftime('Сегодня' + '%Y:%m:%d'))
            engine.runAndWait()
    
        if text in year_in:
            print (now.strftime('Сейчас ' + '%Y' + ' год'))
            engine = pyttsx3.init()
            engine.say(now.strftime('сейчас ' + '%Y' + ' год'))
            engine.runAndWait()

        if text in month_in:
            print (now.strftime('Сейчас ' + '%m' + '  месяц года'))
            engine = pyttsx3.init()
            engine.say(now.strftime('сейчас ' + '%m' + '  месяц года'))
            engine.runAndWait()

        if 'какой сегодня день недели' in text:
            print (now.strftime('Сегодня ' + '%A'))
            engine = pyttsx3.init()
            engine.say(now.strftime('сегодня ' + '%A'))
            engine.runAndWait()




        if 'новости' in text or 'риа новости' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://ria.ru/', new = 2)

        if 'ютуб' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.youtube.com/', new = 2)

        if 'youtube' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.youtube.com/', new = 2)

        if 'вконтакте' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://vk.com/feed', new = 2)

        if 'гос услуги' in text or 'госуслуги'in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.gosuslugi.ru/', new = 2)

        if 'яндекс новости' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/news/', new = 2)

        if 'яндекс' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/', new = 2)

        if 'карты' in text  or 'яндекс карты' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/maps/', new = 2)

        if 'телепрограмму' in text or 'телепрограмма'in text or 'яндекс телепрограмму' in text or 'яндекс телепрограмма' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://tv.yandex.ru/', new = 2)

        if 'переводчик' in text or 'яндекс переводчик' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://translate.yandex.ru/', new = 2)

        if 'яндекс дзен' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://zen.yandex.ru/', new = 2)
	    
        if 'музыка' in text or 'яндекс музыка' in text or 'яндекс музыку' in text or 'музыку'  in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://music.yandex.ru/', new = 2)

        if 'одноклассиники' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://ok.ru/', new = 2)

        if 'фейсбук' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://ru-ru.facebook.com/', new = 2)

        if 'твиттер' in text or 'твитер' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://twitter.com/', new = 2)

        if 'инстаграмм' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.instagram.com/', new = 2)

        if 'статистику по коронавирусу' in text or 'статистика по коронавирусу' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/covid19/stat', new = 2)

        if 'погода' in text or 'погоду' in text or 'яндекс погода'in text or 'яндекс погоду' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/pogoda/', new = 2)

        if 'маркет' in text or 'яндекс маркет' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://market.yandex.ru/', new = 2)

        if 'стим' in text or 'steam' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://store.steampowered.com/', new = 2)

        if 'лавку' in text or 'лавка' in text or 'еда' in text or 'еду' in text: 
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://lavka.yandex.ru/', new = 2)


        if 'сколько тебе лет' in text or 'сколько тебе' in text:
            print ('К счастью или к сожалению я этого пока не знаю. И между прочим спрашивать у дамы про ее возраст неприлично.')
            engine = pyttsx3.init()
            engine.say ('К счастью или к сожалению я этого пока не знаю между прочим спрашивать у дамы про ее возраст неприлично')
            engine.runAndWait()

        if 'лучший' in text and 'голосовой' in text and 'какой' in text:
            print ('Я не могу ответить на этот вопрос, ведь существует множество голосывых помощников и каждый хорош по своему. Лично мне больше всех нравится голосовой ассистент Алиса')
            engine = pyttsx3.init()
            engine.say ('я не могу ответить на этот вопрос ведь существует множество голосывых помощников и каждый хорош по своему лично мне больше всех нравится голосовой ассистент алиса')
            engine.runAndWait()


        if 'какие языки ты знаешь' in text or 'сколько языков ты знаешь' in text:
            print ('На данный момент я знаю только руссский язык и немного аглийский.')
            engine = pyttsx3.init()
            engine.say ('на данный момент я знаю только руссский язык и немного аглийский')
            engine.runAndWait()

        if 'кто ты' in text:
            print ('Меня зовут Спектра и я голосовой помощник')
            engine = pyttsx3.init()
            engine.say ('меня зовут спектра и я голосовой помощник')
            engine.runAndWait()

        if 'ты искусственный интеллект' in text or 'ты являешься искусственным интеллектом' in text:
            print ('Нет, я не нейронная сеть и не искуственный интеллект. Я представляю собой лишь набор сотни алгоритмов и сценариев. Мой создатель полагает, что это када более надежная и безотказная система')
            engine = pyttsx3.init()
            engine.say ('нет я не нейронная сеть и не искуственный интеллект, я представляю собой лишь набор сотни алгоритмов и сценариев, мой создатель полагает что это куда более надежная и безотказная система')
            engine.runAndWait()

        if 'ты нейронная сеть' in text or 'ты являешься нейронной сетью' in text:
            print ('Я не нейронная сеть и не искуственный интеллект. Я представляю собой лишь набор сотни алгоритмов и сценариев. Мой создатель полагает, что это када более надежная и безотказная система')
            engine = pyttsx3.init()
            engine.say ('я не нейронная сеть и не искуственный интеллект, я представляю собой лишь набор сотни алгоритмов и сценариев, мой создатель полагает что это куда более надежная и безотказная система')
            engine.runAndWait()

        if 'кто твой создатель' in text:
            print ('К сожалению я не могу этого сказать, так как это конфиденциальная информация')
            engine = pyttsx3.init()
            engine.say ('к сожалению я не могу этого сказать так как это конфиденциальная информация')
            engine.runAndWait()

   
        if text == 'спектра':
            name = random.choice(name_out)
            print (name)
            engine = pyttsx3.init()
            engine.say (name)
            engine.runAndWait()
   
        if 'у меня дела' in text or 'у меня все' in text:
           print ('Я за вас рада.')
           engine = pyttsx3.init()
           engine.say ('Я за вас рада')
           engine.runAndWait()

        if text in holiday_in:
           print ('Я вас поздаравляю. Желаю всего самого наилучшего.')
           engine = pyttsx3.init()
           engine.say ('Я вас поздаравляю, желаю всего самого наилучшего')
           engine.runAndWait()

        if 'меня зовут' in text:
            print ('Меня Спектра. Приятно познакомиться.')
            engine = pyttsx3.init()
            engine.say ('Меня спектра, приятно познакомиться')
            engine.runAndWait()
      
        if 'как тебя зовут' in text:
            print ('Меня зовут Спектра и я голосовой помощник')
            engine = pyttsx3.init()
            engine.say ('Меня зовут Спектра и я голосовой помощник')
            engine.runAndWait()

        if text in greeting_in:
            greeting = random.choice(greeting_out)
            print (greeting)
            engine = pyttsx3.init()
            engine.say (greeting)
            engine.runAndWait()

        if text in farewell_in:
            farewell = random.choice(farewell_out)
            print (farewell)
            engine = pyttsx3.init()
            engine.say (farewell)
            engine.runAndWait()
            sys.exit()
        
        if  text in apology_in:
            apology = random.choice(apology_out)
            print (apology)
            engine = pyttsx3.init()
            engine.say (apology)
            engine.runAndWait()


        if  text in affairs_in:
            affairs = random.choice(affairs_out)
            print (affairs)
            engine = pyttsx3.init()
            engine.say (affairs)
            engine.runAndWait()
    






    if x == 1:

        print ('Напишите что-нибудь...')

        text = str(input())

        if 'что такое' in text or 'кто такой' in text:
            wiki = text.replace ('спектра', '')
            wiki = wiki.replace ('мне', '')
            wiki = wiki.replace ('скажи', '')
            wiki = wiki.replace ('пожалуйста', '')
            wiki = wiki.replace ('нам', '')
            wiki = wiki.replace ('что такое', '')
            wiki = wiki.replace ('кто такой', '')
            wiki = wiki.strip ()
            print ('Секундочку...')
            webbrowser.open('https://www.google.com/search?ei=iAnOX9LOMOnyqwG7ko6gBw&q=' + wiki + '&oq=' + wiki + '&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyBAgAEEMyAggAMgIIADIECAAQQzIFCAAQsQNQgfjUAlj0-dQCYOKB1QJoAXABeACAAd4DiAHeA5IBAzQtMZgBAKABAaoBB2d3cy13aXqwAQDAAQE&sclient=psy-ab&ved=0ahUKEwjSsu6H2rvtAhVp-SoKHTuJA3QQ4dUDCA0&uact=5', new = 2)
            time.sleep(1)
            result = wikipedia.summary(wiki)
            print (result)
            engine = pyttsx3.init()
            engine.say (result)
            engine.runAndWait()

        if 'найди' in text or 'ищи' in text:
            zapros = text.replace ('найди', '')
            zapros = zapros.replace ('спектра', '')
            zapros = zapros.replace ('ищи', '')
            zapros = zapros.replace ('мне', '')
            zapros = zapros.replace ('давай', '')
            zapros = zapros.replace ('пожалуйста', '') 
            zapros = zapros.replace ('нам', '')
            zapros = zapros.strip ()            
            print ('Уже ищу...')
            engine = pyttsx3.init()
            engine.say ('уже ищу')
            engine.runAndWait()  
            webbrowser.open('https://www.google.com/search?ei=iAnOX9LOMOnyqwG7ko6gBw&q=' + zapros + '&oq=' + zapros + '&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyBAgAEEMyAggAMgIIADIECAAQQzIFCAAQsQNQgfjUAlj0-dQCYOKB1QJoAXABeACAAd4DiAHeA5IBAzQtMZgBAKABAaoBB2d3cy13aXqwAQDAAQE&sclient=psy-ab&ved=0ahUKEwjSsu6H2rvtAhVp-SoKHTuJA3QQ4dUDCA0&uact=5', new = 2)
            time.sleep(1)
            print ('Вот что мне удалось найти по вашему запросу:')
            engine = pyttsx3.init()
            engine.say ('вот что мне удалось найти по вашему запросу')
            engine.runAndWait()       


        if 'английский' in text or 'английскии'in text:
            tran = text.replace ('спектра', '')
            tran = tran.replace ('переведи', '')
            tran = tran.replace ('давай', '')
            tran = tran.replace ('пожалуйста', '')
            tran = tran.replace ('на английский', '')
            tran = tran.replace ('нам', '')
            tran = tran.replace ('по-английски', '')
            tran = tran.replace ('мне', '')
            tran = tran.replace ('как будет', '')
            tran = tran.replace ('по английски', '')
            tran = tran.replace ('на английском', '')
            tran = tran.strip()
            translation = Translator (from_lang = "ru", to_lang = "en")
            result = translation.translate (tran)
            print ('Перевожу...')
            engine = pyttsx3.init()
            engine.say ('перевожу')
            engine.runAndWait()            
            time.sleep(1)
            print ('RU --> EN')
            print (tran + ' --> ' + result)
            engine = pyttsx3.init()
            engine.say ('На английском языке ' + tran + ' будет: ' + result)
            engine.runAndWait() 


        
        

        if 'песню' in text:
       
            music = text.replace ('включи', '')
            music = music.replace ('песню', '')
            music = music.replace ('давай', '') 
            music = music.replace ('песня', '')
            music = music.replace ('поставь', '')
            music = music.replace ('пожалуйста', '') 
            music = music.replace ('спектра', '')
            music = music.strip ()
            time.sleep(1)
            print ('Уже включаю...')
            engine = pyttsx3.init()
            engine.say ('уже включаю')
            engine.runAndWait()
            os.startfile(F"C:\\Files_for_Spectra_Assistant\\Music\\{music}.mp3") 

        if 'фильм' in text or 'видео' in text:
            film = text.replace ('спектром', '')
            film = text.replace ('включи', '')
            film = film.replace ('фильм', '')
            film = film.replace ('давай', '') 
            film = film.replace ('пожалуйста', '') 
            film = film.replace ('спектра', '')
            film = film.replace ('мне', '')
            film = film.replace ('видео', '')
            film = film.replace ('которое называется', '')
            film = film.replace ('под названием', '')
            film = film.replace ('спектра', '')
            film = film.strip ()
            time.sleep(1)
            print ('Уже включаю...')
            engine = pyttsx3.init()
            engine.say ('уже включаю')
            engine.runAndWait() 
            os.startfile(F"C:\\Files_for_Spectra_Assistant\\Film\\{film}.mp4")
        



        if 'энерджи' in text or 'energy' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.energyfm.ru', new = 2) 
    
        if 'рекорд' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.radiorecord.ru', new = 2) 

        if 'шансон' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://radioshanson.ru', new = 2)
        
        if 'лайк' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.likefm.ru', new = 2)
  
        if 'русское' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://rusradio.ru', new = 2)
  
        if 'ретро' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://retrofm.ru', new = 2)
   
        if 'вести' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://radiovesti.ru', new = 2)
  
        if 'европа' in text:
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://europaplus.ru', new = 2)
     
        if 'что ты умеешь' in text:
            print ('Вот что я умею:')
            print ('- Spectra, включи фильм "Зелёная миля"')
            print ('- Spectra, найди где купить цветы в Москве')
            print ('- Spectra, переведи на англйиский: "Красная машина едет по дороге"')
            print ('- Spectra, сколько сейчас времени?"')
            print ('- Spectra, какое сегодня число?"')
            print ('- Spectra, какой сейчас год?"')
            print ('- Spectra, открой статистику по коронавирусу"')
            print ('- Spectra, открой радио "Шансон"')
            print ('- Spectra, кто такой Пушкин?')
            engine = pyttsx3.init()
            engine.say('Вот что я умею')
            engine.runAndWait()


        if text in time_in:
            print (now.strftime('Сейчас ' + '%H:%M:%S'))
            engine = pyttsx3.init()
            engine.say(now.strftime('Сейчас' + '%H' + 'часов' + '%M' + 'минут' + '%S' + 'секунд'))
            engine.runAndWait()

        if text in date_in:
            print (now.strftime('Сегодня ' + '%Y.%m.%d'))
            engine = pyttsx3.init()
            engine.say(now.strftime('Сегодня' + '%Y:%m:%d'))
            engine.runAndWait()
    
        if text in year_in:
            print (now.strftime('Сейчас ' + '%Y' + ' год'))
            engine = pyttsx3.init()
            engine.say(now.strftime('сейчас ' + '%Y' + ' год'))
            engine.runAndWait()

        if text in month_in:
            print (now.strftime('Сейчас ' + '%m' + '  месяц года'))
            engine = pyttsx3.init()
            engine.say(now.strftime('сейчас ' + '%m' + '  месяц года'))
            engine.runAndWait()

        if 'какой сегодня день недели' in text:
            print (now.strftime('Сегодня ' + '%A'))
            engine = pyttsx3.init()
            engine.say(now.strftime('сегодня ' + '%A'))
            engine.runAndWait()




        if 'новости' in text or 'риа новости' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://ria.ru/', new = 2)

        if 'ютуб' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.youtube.com/', new = 2)

        if 'youtube' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.youtube.com/', new = 2)

        if 'вконтакте' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://vk.com/feed', new = 2)

        if 'гос услуги' in text or 'госуслуги'in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.gosuslugi.ru/', new = 2)

        if 'яндекс новости' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/news/', new = 2)

        if 'яндекс' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/', new = 2)

        if 'карты' in text  or 'яндекс карты' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/maps/', new = 2)

        if 'телепрограмму' in text or 'телепрограмма'in text or 'яндекс телепрограмму' in text or 'яндекс телепрограмма' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://tv.yandex.ru/', new = 2)

        if 'переводчик' in text or 'яндекс переводчик' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://translate.yandex.ru/', new = 2)

        if 'яндекс дзен' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://zen.yandex.ru/', new = 2)
        
        if 'музыка' in text or 'яндекс музыка' in text or 'яндекс музыку' in text or 'музыку'  in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://music.yandex.ru/', new = 2)

        if 'одноклассиники' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://ok.ru/', new = 2)

        if 'фейсбук' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://ru-ru.facebook.com/', new = 2)

        if 'твиттер' in text or 'твитер' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://twitter.com/', new = 2)

        if 'инстаграмм' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://www.instagram.com/', new = 2)

        if 'статистику по коронавирусу' in text or 'статистика по коронавирусу' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/covid19/stat', new = 2)

        if 'погода' in text or 'погоду' in text or 'яндекс погода'in text or 'яндекс погоду' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://yandex.ru/pogoda/', new = 2)

        if 'маркет' in text or 'яндекс маркет' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://market.yandex.ru/', new = 2)

        if 'стим' in text or 'steam' in text:
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://store.steampowered.com/', new = 2)

        if 'лавку' in text or 'лавка' in text or 'еда' in text or 'еду' in text: 
            time.sleep(1)
            print ('Уже открываю...')
            engine = pyttsx3.init()
            engine.say ('уже открываю')
            engine.runAndWait()
            webbrowser.open ('https://lavka.yandex.ru/', new = 2)


        if 'сколько тебе лет' in text or 'сколько тебе' in text:
            print ('К счастью или к сожалению я этого пока не знаю. И между прочим спрашивать у дамы про ее возраст неприлично.')
            engine = pyttsx3.init()
            engine.say ('К счастью или к сожалению я этого пока не знаю между прочим спрашивать у дамы про ее возраст неприлично')
            engine.runAndWait()

        if 'лучший' in text and 'голосовой' in text and 'какой' in text:
            print ('Я не могу ответить на этот вопрос, ведь существует множество голосывых помощников и каждый хорош по своему. Лично мне больше всех нравится голосовой ассистент Алиса')
            engine = pyttsx3.init()
            engine.say ('я не могу ответить на этот вопрос ведь существует множество голосывых помощников и каждый хорош по своему лично мне больше всех нравится голосовой ассистент алиса')
            engine.runAndWait()


        if 'какие языки ты знаешь' in text or 'сколько языков ты знаешь' in text:
            print ('На данный момент я знаю только руссский язык и немного аглийский.')
            engine = pyttsx3.init()
            engine.say ('на данный момент я знаю только руссский язык и немного аглийский')
            engine.runAndWait()

        if 'кто ты' in text:
            print ('Меня зовут Спектра и я голосовой помощник')
            engine = pyttsx3.init()
            engine.say ('меня зовут спектра и я голосовой помощник')
            engine.runAndWait()

        if 'ты искусственный интеллект' in text or 'ты являешься искусственным интеллектом' in text:
            print ('Нет, я не нейронная сеть и не искуственный интеллект. Я представляю собой лишь набор сотни алгоритмов и сценариев. Мой создатель полагает, что это када более надежная и безотказная система')
            engine = pyttsx3.init()
            engine.say ('нет я не нейронная сеть и не искуственный интеллект, я представляю собой лишь набор сотни алгоритмов и сценариев, мой создатель полагает что это куда более надежная и безотказная система')
            engine.runAndWait()

        if 'ты нейронная сеть' in text or 'ты являешься нейронной сетью' in text:
            print ('Я не нейронная сеть и не искуственный интеллект. Я представляю собой лишь набор сотни алгоритмов и сценариев. Мой создатель полагает, что это када более надежная и безотказная система')
            engine = pyttsx3.init()
            engine.say ('я не нейронная сеть и не искуственный интеллект, я представляю собой лишь набор сотни алгоритмов и сценариев, мой создатель полагает что это куда более надежная и безотказная система')
            engine.runAndWait()

        if 'кто твой создатель' in text:
            print ('К сожалению я не могу этого сказать, так как это конфиденциальная информация')
            engine = pyttsx3.init()
            engine.say ('к сожалению я не могу этого сказать так как это конфиденциальная информация')
            engine.runAndWait()

   
        if text == 'спектра':
            name = random.choice(name_out)
            print (name)
            engine = pyttsx3.init()
            engine.say (name)
            engine.runAndWait()
   
        if 'у меня дела' in text or 'у меня все' in text:
           print ('Я за вас рада.')
           engine = pyttsx3.init()
           engine.say ('Я за вас рада')
           engine.runAndWait()

        if text in holiday_in:
           print ('Я вас поздаравляю. Желаю всего самого наилучшего.')
           engine = pyttsx3.init()
           engine.say ('Я вас поздаравляю, желаю всего самого наилучшего')
           engine.runAndWait()

        if 'меня зовут' in text:
            print ('Меня Спектра. Приятно познакомиться.')
            engine = pyttsx3.init()
            engine.say ('Меня спектра, приятно познакомиться')
            engine.runAndWait()
      
        if 'как тебя зовут' in text:
            print ('Меня зовут Спектра и я голосовой помощник')
            engine = pyttsx3.init()
            engine.say ('Меня зовут Спектра и я голосовой помощник')
            engine.runAndWait()

        if text in greeting_in:
            greeting = random.choice(greeting_out)
            print (greeting)
            engine = pyttsx3.init()
            engine.say (greeting)
            engine.runAndWait()

        if text in farewell_in:
            farewell = random.choice(farewell_out)
            print (farewell)
            engine = pyttsx3.init()
            engine.say (farewell)
            engine.runAndWait()
            sys.exit()
        
        if  text in apology_in:
            apology = random.choice(apology_out)
            print (apology)
            engine = pyttsx3.init()
            engine.say (apology)
            engine.runAndWait()


        if  text in affairs_in:
            affairs = random.choice(affairs_out)
            print (affairs)
            engine = pyttsx3.init()
            engine.say (affairs)
            engine.runAndWait()
    



  




while True:
    exe()

