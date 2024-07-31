from time import sleep
from googletrans import Translator
import googletrans
from gtts import gTTS
import pyttsx3
import speech_recognition
import os
from playsound import playsound
import time


engine = pyttsx3.init("sapi5") # sapi5 is Speech Application Programming Interface, version 5 developed by Microsoft that allow programmers to include speech related features.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer() 
    with speech_recognition.Microphone() as source :
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)######

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e :
        print("Say that again")
        return "None"
    return query

def translate(query):
    speak("Sure Ma'am")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language to be translated")
    b = input("To Language :-")
    text_to_translate = translator.translate(query, src ="auto", dest =b)
    text = text_to_translate.text
    try:
        speakgl = gTTS(text=text, lang=b, slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        time.sleep(5)
        os.remove("voice.mp3")
    except Exception as e:
        print("Unable to translate", e)  

