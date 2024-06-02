from src.helper import speak, takeCommand, wish_me
import datetime
import wikipedia
import webbrowser
import os
import streamlit as st

if __name__ == "__main__":
    wish_me()
    while True:
        
        st.title("Desktop Assistant System")
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