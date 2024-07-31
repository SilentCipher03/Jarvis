import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5") # sapi5 is Speech Application Programming Interface, version 5 developed by Microsoft that allow programmers to include speech related features.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1f0ed04a8db940e5bd5c045f042e1b94",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=1f0ed04a8db940e5bd5c045f042e1b94",
               "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=1f0ed04a8db940e5bd5c045f042e1b94",
               "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=1f0ed04a8db940e5bd5c045f042e1b94",
               "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=1f0ed04a8db940e5bd5c045f042e1b94",
               "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=1f0ed04a8db940e5bd5c045f042e1b94"
               }

    content = None 
    url = None
    speak("Which genre specifically you want, [business], [entertainment], [health], [science], [sports], [technology] please type it") 
    field = input("Type the genre you want to be updated with")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
        if url is True:
                print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("news today")

    arts = news["articles"]
    for articles in arts:
        article =  articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info gain: {news_url}")

        a = input("[press 1 to count] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("thankyou ma'am")           