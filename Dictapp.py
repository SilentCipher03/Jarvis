import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5") # sapi5 is Speech Application Programming Interface, version 5 developed by Microsoft that allow programmers to include speech related features.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd.exe","paint":"mspaint.exe","word":"winword.exe","excel":"excel.exe","chrome":"chrome.exe","vscode":"code.exe","powerpoint":"powerpoint.exe","edge":"msedge.exe","photo":"photo.exe","music":"mediaplayer.exe"}

def openwebapp(query):
    speak("Launching,Ma'am")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}") 

def closewebapp(query):
    speak("Closing ma'am")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("Closed current tab")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w") 
        sleep(0.5) # The sleep(0.5) calls introduce a short delay between consecutive tab-closing actions to ensure that each action is recognized and executed properly
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w") 
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w") 
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w") 
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed") 

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
