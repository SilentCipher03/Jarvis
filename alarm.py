# import pyttsx3
# import datetime
# import os

# engine = pyttsx3.init("sapi5") # sapi5 is Speech Application Programming Interface, version 5 developed by Microsoft that allow programmers to include speech related features.
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# extractedtime = open("AlarmText.txt","rt")
# time = extractedtime.read()
# Time = str(time)
# extractedtime.close()

# datetime = open("AlarmText.txt","r+")
# datetime.truncate(0)
# datetime.close()

# def ring(time):
#     timeset = str(time)
#     timenow = timeset.replace("jarvis","")
#     timenow = timenow.replace("set an alarm","")
#     timenow = timenow.replace(" and ",":")
#     Alarmtime = str(timenow)
#     print(Alarmtime)
#     while True:
#         currenttime = datetime.datetime.now().strftime("%H:%M:%S")    
#         if currenttime == Alarmtime:
#             speak("alarm ringing, ma'am")
#             os.startfile("C:/Users/Lenovo/Desktop/Music/चलो_रे_मन_श्री_वृन्दावन_धाम_जपेंगे_राधे_राधे_नाम_~_Chitra_Vichitra_Ji_Maharaj_~_Krishna_Bhajan_2022(128k).mp3")
#         elif currenttime + "00:00:50" == Alarmtime:
#             exit()

#         elif "Stop the alarm" in query:
            

# ring(time) 




import pyttsx3
import datetime
import os
import time

engine = pyttsx3.init("sapi5")  # sapi5 is Speech Application Programming Interface, version 5 developed by Microsoft that allows programmers to include speech-related features.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def read_alarm_time():
    with open("AlarmText.txt", "rt") as file:
        time = file.read()
    return time.strip()

def clear_alarm_file():
    with open("AlarmText.txt", "w") as file:
        file.write("")  # Clear the contents of the file

def play_alarm_sound():
    os.startfile("C:/Users/Lenovo/Desktop/Music/चलो_रे_मन_श्री_वृन्दावन_धाम_जपेंगे_राधे_राधे_नाम_~_Chitra_Vichitra_Ji_Maharaj_~_Krishna_Bhajan_2022(128k).mp3")

def stop_alarm():
    os.system("taskkill /f /im wmplayer.exe")  # Stops Windows Media Player, assuming it's used for playing the alarm sound
    speak("Alarm stopped.")

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    
    alarm_playing = False
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        
        if currenttime == Alarmtime and not alarm_playing:
            speak("Alarm ringing, ma'am")
            play_alarm_sound()
            alarm_playing = True
        
        elif alarm_playing and (datetime.datetime.now() - datetime.datetime.strptime(currenttime, "%H:%M:%S")).seconds > 50:
            # Stop alarm if it has been ringing for more than 50 seconds
            stop_alarm()
            break

        # Check for user input to stop the alarm
        user_input = input("Type 'stop' to stop the alarm: ").strip().lower()
        if user_input == 'stop':
            stop_alarm()
            break
        
        time.sleep(1)  # Check every second

# Clear the alarm time file
clear_alarm_file()

# Read alarm time from the file
time = read_alarm_time()

# Start the alarm process
ring(time)
