# pyttsx3 is used for query to speech conversion
import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
print(voices[1].id)
print(type(voices))

# Selecting a female voice
engine.setProperty('voice', voices[1].id)

def speak(query):
    """This function takes query and returns vocie

    Args:
        query (_type_): string
    """
    engine.say(query)
    engine.runAndWait()
    


def takeCommand():
    """This function will recognize voice and returns query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    
    
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Bappy sir. How are you doing")
    elif hour>=12 and hour<18:
        speak("Good afternoon Bappy sir. How are you doing")
    else:
        speak("Good evening Bappy sir. How are you doing")    
        
    speak("I am JARVIS. Tell me sir how can I help you")

 
if __name__ == "__main__":
    wish_me()
    while True:
        
        query = takeCommand().lower()
        # speak(query)
        print(query)
        
        if "wikipedia" in query:
            print("yes")
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif "youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            
        elif "google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
            
        elif "github" in query:
            speak("Opening Github")
            webbrowser.open("github.com")
            
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            
        elif "goodbye" in query:
            speak("Ok bye. I'm always there for you.")
            exit()