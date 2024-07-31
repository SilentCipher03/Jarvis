import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5") # sapi5 is Speech Application Programming Interface, version 5 developed by Microsoft that allow programmers to include speech related features.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wolframalpha(query):
    apikey = "896LVE-WGYV9Y4W3K"
    requestor = wolframalpha.Client(apikey)
    requested = requestor.query(query)  

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable") 

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiple","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = Wolframalpha(Final)
        print(f"{result}")
        speak(" Result is ")
    except:
        speak("value is not answerable")