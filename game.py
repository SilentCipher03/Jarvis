import pyttsx3
import speech_recognition
import random 

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

def game_play():
    speak("Let's have fun together, and we will play rock paper and scissor ma'am ")
    print("Let's start")
    speak("How is the josh high sir huuuu")
    i =0
    user_score =0
    jarvis_score =0

    while(i<5):
        choose = ("rock", "paper", "scissor")
        jarvis_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if(jarvis_choose == "rock"):
                speak("ROCK")
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
            elif (jarvis_choose == "paper"):
                speak("paper")
                jarvis_score +=1
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
            else:
                speak("scissor")
                user_score +=1 
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
        elif (query == "paper"):
            if(jarvis_choose == "rock"):
                speak("Rock")
                user_score +=1    
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
            elif(jarvis_choose == "paper"):
                speak("Paper")
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
            else:
                speak("Scissor")
                jarvis_score +=1
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
        elif( query == "scissor" or query == "scissors"):
            if(jarvis_choose == "rock"):
                speak("ROCK")
                jarvis_score += 1
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
            elif(jarvis_choose == "paper"):
                speak("Paper")
                user_score += 1
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")
            else:
                speak("Scissor")
                print(f"User :- {user_score} : Jarvis :- {jarvis_score}")

        i += 1

    print(f"FINAL SCORE :- User :- {user_score} : Jarvis :- {jarvis_score}")
                    



