# Installation WinOS:

# pip install pipwin 
# pipwin install pyaudio 
# pip install speechrecognition
# pip install pywhatkit 
# pip install pyttsx3 
# pip install pyjokes 
# pip install wikipedia
# -------------------------------

# Voice commands for the assistant:

# PREFIX: "hey siri"

# song- Hey siri play <song name>
# time- Hey siri whats the time
# info- Hey siri who is <name of the person>
# joke- Hey siri say a joke
# --------------------------------------------

# PLS USE "PLAY" ONLY FOR SONG COMMANDS. USAGE MAY OTHERWISE LEAD TO A MALFUNCTIONING..


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

engine.say("Im listening")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey siri' in command:
                command = command.replace('hey siri','')
            
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
