import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import requests
import smtplib
import random
import os
import webbrowser
from bs4 import BeautifulSoup
from colorama import Fore, init

# Initialize colorama and text-to-speech engine
init(autoreset=True)
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set properties for the TTS voice
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 0.9)  # Volume level

# Sample jokes and fun facts
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call fake spaghetti? An impasta!"
]

fun_facts = [
    "Did you know honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!",
    "Did you know the Eiffel Tower can be 15 cm taller during the summer due to heat expansion?",
    "Bananas are berries, but strawberries aren’t!"
]

# Function to make JARVIS speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command
def take_command():
    with sr.Microphone() as source:
        print(Fore.GREEN + "Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print(Fore.YELLOW + "Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, the service is unavailable.")
        return ""

# Fallback function to take typed command
def take_command_type():
    print(Fore.BLUE + "Type your command:")
    command = input(">> ").strip().lower()
    return command

# Functions for jokes and fun facts
def tell_joke():
    speak(random.choice(jokes))

def tell_fun_fact():
    speak(random.choice(fun_facts))

# Function for quick search
def quick_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    summary = soup.find("div", class_="BNeawe").text
    return summary

# Function to greet the user
def greet_user():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am JARVIS. How can I assist you today?")

# Main function to process commands
def process_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching for {query}")
        pywhatkit.search(query)

    elif "play" in command:
        song = command.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "who is" in command or "what is" in command:
        query = command.replace("who is", "").replace("what is", "")
        info = wikipedia.summary(query, sentences=2)
        speak(info)

    elif "tell me a joke" in command:
        tell_joke()

    elif "tell me a fun fact" in command:
        tell_fun_fact()

    elif "quick search" in command:
        query = command.replace("quick search", "").strip()
        speak(f"Searching for {query}")
        result = quick_search(query)
        speak(result)

    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("notepad")

    elif "open command prompt" in command or "open cmd" in command:
        speak("Opening Command Prompt.")
        os.system("start cmd")

    elif "open vs code" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code.")
        os.system("code")  # This assumes "code" is in the system PATH

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand the command.")

# Run JARVIS with fallback to typing mode
def run_jarvis():
    greet_user()
    while True:
        try:
            # Try listening for a command
            command = take_command()
            if command:
                process_command(command)
        except Exception as e:
            print(Fore.RED + "Listening error occurred. Switching to typing mode.")
            speak("There was an issue with listening. Please type your command.")
            command = take_command_type()
            process_command(command)

# Start JARVIS
run_jarvis()
