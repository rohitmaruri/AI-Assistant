# Importing necessary libraries
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Setting up text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Defining function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Defining function to recognize user speech
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# Defining main function for AI assistant
if __name__ == "__main__":
    speak("Hello! I am your AI assistant. How may I help you?")

    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google...")
            webbrowser.open("google.com")

        elif 'time' in query:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {now}")

        elif 'play music' in query:
            speak("Playing music...")
            music_dir = 'C:\\Users\\User\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'remind me' in query:
            speak("What would you like me to remind you of?")
            reminder = take_command()
            speak(f"Okay, I will remind you of {reminder} in 5 minutes.")
            time.sleep(300)
            speak(f"Reminder: {reminder}")

        elif 'stop' in query:
            speak("Goodbye!")
            break
