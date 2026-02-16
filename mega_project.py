import speech_recognition as sr
import webbrowser
import pyttsx3
import os

recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000
recognizer.dynamic_energy_threshold = True

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)

    return recognizer.recognize_google(audio).lower()


speak("I am ready to listen.")

# Noise adjust only once
with sr.Microphone() as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=2)

while True:
    try:
        command = take_command()
        print("You said:", command)

        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "chatgpt" in command:
            speak("Opening ChatGPT")
            webbrowser.open("https://chatgpt.com")


        elif "paint" in command:
            speak("Opening Paint")
            os.system("mspaint")


        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        elif "stop" in command or "bye" in command:
            speak("Goodbye!")
            break

        else:
            speak("I did not understand.")

    except sr.WaitTimeoutError:
        print("Listening timeout...")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
    except sr.RequestError:
        speak("Network error.")
