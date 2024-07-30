import speech_recognition as sr
import pyttsx3
import tkinter as tk


root = tk.Tk()
root.title("Speech to Text")

r = sr.Recognizer()
engine = pyttsx3.init()

# Flag to control speech-to-text
is_listening = False

text_box = tk.Text(root, height=10, width=30)

print("Please speak in short and loud sentences.")
print("Please wait for 2-3 seconds after you finish a sentence.")
print("You may start speaking.")

def start_listening():
    global is_listening
    is_listening = True
    while is_listening:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.1)
                audio = r.listen(source)
                text = r.recognize_google(audio)
                engine.say(text)
                print(text)
                with open('Transformedtext', 'a') as file:
                    file.write("\n")
                    file.write(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

start_listening()