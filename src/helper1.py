import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS

GOOGLE_API_KEY = "AIzaSyA7dtVBKkqzZF7aHcSpt9hBtxxqC4htOmQ"
os.environ['GOOGLE_API_KEY'] = "GOOGLE_API_KEY"

def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {format(e)}")
        
        
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    
def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(user_text)
    
    result = response.text
    
    return result