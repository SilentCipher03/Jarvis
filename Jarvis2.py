import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
from plyer import notification
import random
from pygame import mixer
import speedtest


# Password protection in Jarvis
for i in range(3):
    a = input("Enter Password to open JARVIS :- ")
    pw_file = open("python/Password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("Welcome ma'am ! Please speak [Wake Up JARVIS] to start")
        break
    elif (i == 2 and a != pw):
        exit()
    elif (a != pw):
        print("Try Again") 

# GUI of Jarvis 
from GUI import play_gif
play_gif

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

#Alarm Function 
def alarm(query):
    timehere = open("AlarmText.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("C:/Users/Lenovo/Desktop/Apni kaksha/Python/alarm.py")



if __name__  == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up jarvis" in query:
# Greet Me Funtion with Jarvis using GreetMe file
            from GreetMe import greetme
            greetme()

            while True:
                query = takeCommand().lower()
                if "nap time jarvis" in query:
                    speak("Ok ma'am, You can call me anytime")
                    break


################################### JARVIS 2.0 #####################

# Change Password 
                elif "change password" in query:
                    speak("What is the new password")
                    new_pw = input("Enter the new password\n")
                    with open("python/Password.txt","w") as password_file:       # W here remove old password and save new one and append is also used it keeps old one also and writes new one 
                        password_file.write(new_pw)
                    speak("Done ma'am")
                    speak(f"your new password is {new_pw}")

# Schedule Day Function
                elif "schedule my day" in query:
                    tasks = [] #Empty List
                    speak("Have you completed previous day tasks (Plz speak Yes or No)")
                    query = takeCommand().lower()  # Use a different variable name here
                    if "yes" in query:
                        file = open("python/Tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks to be completed today :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :- "))
                            file = open("python/Tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                    elif "no" in query:
                        i=0
                        no_tasks = int(input("Enter the number of tasks to be completed today :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :- "))
                            file = open("python/Tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                        
                            file = open("python/Tasks.txt","r")
                            content = file.read()
                            file.close()
                            mixer.init()
                            mixer.music.load("C:/Users/Lenovo/Desktop/Music/हमें_औरन_की_परवाह_नहीं_है_अपनी_ठकुरानी_श्री_राधिका_रानी_Hame_Auran_Ki_Parwah_Nahi(128k).mp3")
                            mixer.music.play()
                            notification.notify(
                                title = "My Schedule:",
                                message = content,
                                timeout= 25
                            )

# Open any app using jarvis (This is advanced code of doing also did by making dictionary as Dictapp)
                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")

# Check Internet Speed by just voice
 
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576 # 1 megabyte = 1024*1024 bytes
                    download_net = wifi.download()/1048576
                    print("wifi Upload Speed is", upload_net)
                    print("wifi Download speed is", download_net )
                    speak(f"wifi download speed is {download_net}")
                    speak(f"wifi upload speed is {upload_net}")

# Rock Paper and Scissor game 
                elif "play a game" in query:
                    from game import game_play
                    game_play()

# Focus Mode 
                elif "focus mode" in query:
                    a = int(input("Are you ready to enter Focus Mode [1 for yes / 2 for no]"))
                    if (a==1):
                        speak("Entering Focus Mode ma'am All the best be productive")
                        os.startfile("C:\\Users\\Lenovo\\Desktop\\Apni kaksha\\Python\\FocusMode.py")
                        exit()
                    else:
                        pass 

#Google translator
                elif "translate" in query:
                     from Translator import translate
                     query = query.replace("jarvis", "")
                     query = query.replace("translate", "")
                     translate(query)


                #############################################################################################################


# Conversation with Jarvis
                elif "hello" in query:
                    speak(" Hello ma'am, How are you ?")
                elif "i am fine" in query:
                    speak(" That's great ma'am ")
                elif "how are you jarvis" in query:
                    speak(" Perfect, ma'am What about you? I want you to be happy, you are damn amazing ma'am you are doing best ")
                elif "thank you" in query:
                    speak(" Your welcome ma'am ")
                      
#YouTube Controls 
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video mute") 
                #Volume
                elif "increase volume" in query:
                    from keyboard import volumeup
                    speak("Raising Volume ma'am")
                    volumeup()
                elif "decrease volume" in query:
                    from keyboard import volumedown
                    speak("decreasing volume")
                    volumedown()    
                    


#Opening and closing of the apps and web using Dictapp file                    
                elif "open" in query:
                    from Dictapp import openwebapp
                    openwebapp(query)
                elif "close" in query:
                    from Dictapp import closewebapp
                    closewebapp(query)


# Searching from Web (Google, Youtube, Wikipedia) using SearchNow file
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYouTube
                    searchYouTube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)  

# News Function 
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()  

# Calculator Function 
                elif "calculate" in query:
                    from Calculatenumbers import Wolframalpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

# Whatdapp Function 
                elif "whatsapp" in query:
                    from Whatsapp import sendmessage
                    sendmessage()
                    

                elif "temperature" in query:
                    search = "temperature at Ajmer"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url) #  This line sends a GET request to the specified URL and stores the response in the variable r.
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")
                elif "Weather" in query:
                    search = "Weather at Ajmer"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"Current {search} is {temp}")
                

# alarm Condition
                elif "set an alarm" in query:
                    print("input time example :- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell time :- ")
                    alarm(a)
                    speak("Alarm set, Ma'am")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Ma'am, the time is {strTime}")  
                elif "finally sleep Jarvis" in query:
                    speak("Going to sleep ma'am, had amazing time will meet soon")
                    exit() 


                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    rememberMessage = query.replace("remember that", "")
                    speak("You asked me to" + rememberMessage)
                    remember =open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You asked me to remember that" + remember.read()) 

#ShutDown Function in Jarvis
                elif "Shutdown pc" in query:
                    speak("Are you sure you want to shutdoen ma'am")
                    shutdown = input("Do you wish to shutdown PC ma'am? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s  /t/1")
                    elif shutdown == "no":
                        break                        

'''Playlist of songs
                elif "tired" in query:
                    speak("Let me make your mood better by playing songs you like ")
                    music_directory = "C:/Users/Lenovo/Desktop/Music/Media Player"
                    music_files =[f for f in os.listdir(music_directory) if f.endswith(('.mp3'))]
                    if music_files:
                        random_music = random.choice(music_files)
                        music_path = os.path.join(music_directory, random_music)
                        music_player_command = ["C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories", music_path]
                        subprocess.Popen(media_player_command)
                        speak("Enjoy the music! ma'am")
                    else:
                        speak('No music files found')'''                   

                                        

