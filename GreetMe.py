import pyttsx3
import datetime

engine = pyttsx3.init("sapi5") # sapi5 is Speech Application Programming Interface, version 5 developed by Microsoft that allow programmers to include speech related features.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<= 12:
        speak("Good Morning,Ma'am")
    elif hour>12 and hour<17:
        speak("Good Afternoon,Ma'am") 

    else:
        speak("Good Evening,Ma'am")

    speak("Please tell me, How can I help you ?")           