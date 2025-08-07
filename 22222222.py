import speech_recognition as sr
import pyttsx3
import webbrowser  
import subprocess
import serial  # Import the serial module
import pyaudio

def connect_to_arduino():
    try: 
        arduino_port = "COM7"
        arduino = serial.Serial(arduino_port, 9600, timeout=1)  
        print("Physical body connected.")             
        return arduino
    except:
        print("Unable to connect to my physical body")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=25)
        print("Recognizing...")

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError as e:
            print("Google Speech Recognition request failed: {0}".format(e))
            return ""

def main():
    arduino = connect_to_arduino()
    if arduino is None:
        return

    speak("Hello! I am Jarvis. How can I help you today?")

    while True:
        command = listen()

        if "right hand" in command:
            speak("Moving my hand?")
            print("Sending 'right hand' command")  # Add this print
            arduino.write(b'right hand\n')  # Send command to Arduino

        elif 'rotate your head' in command:
            speak("Moving my head?")
            print("Sending 'rotate your head' command")  # Add this print
            arduino.write(b'rotate your head\n')  # Send command to Arduino

        elif 'say hi' in command:
            speak("Hi boss?")
            print("Sending 'say hi' command")  # Add this print
            arduino.write(b'say hi\n')  # Send command to Arduino

        if "hello jarvis" in command:
            speak("Hello boss. How can I assist you today?")

        elif "jarvis play video" in command:
            speak("What video would you like to watch?")
            video_query = listen()
            webbrowser.open(f"https://www.youtube.com/results?search_query={video_query}")

        elif "jarvis search google" in command:
            speak("What would you like to search on Google?")
            search_query = listen()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif "jarvis play song" in command:
            speak("What song would you like to listen to?")
            song_query = listen()
            webbrowser.open(f"https://music.youtube.com/search?q={song_query}")

        elif "jarvis exit" in command:
            speak("Ok boss. Have a nice day.")
            break

if __name__ == "__main__":
    main()