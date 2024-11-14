# import all Libraries
import tkinter as tk
from tkinter import ttk
from gtts import gTTS
from playsound import playsound
from langdetect import detect
import speech_recognition as sr

win = tk.Tk()
win.title("Text & Speech Converter")# Name the window
win.geometry("430x250")#Size
win.configure(bg="#f5f5f5")  # This part For Change abackground

counter = 1 #This counter For Change Name audio everytime 

# First Function to Convert Text To Speech
def Text_To_Speech():
    global counter
    text = entry.get()
    try:
        lang = detect(text)
        speech = gTTS(text=text, lang=lang)
        filename = f"speech_{counter}.mp3"
        speech.save(filename)
        playsound(filename)
        counter += 1
    except Exception as e: #Exception Handling Block (if the text is empty ==> Error)
        print("Error:", e)


# 2'nd Function to Convert Speech To Text 
def Speech_To_Text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...", foreground="blue")
        win.update_idletasks()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        status_label.config(text="Processing...", foreground="orange")
    try:
        text = recognizer.recognize_google(audio, language="en")
        entry.delete(0, tk.END)
        entry.insert(0, text)
        status_label.config(text="Done", foreground="green")
    except sr.UnknownValueError:
        status_label.config(text="Could not understand audio", foreground="red")
    except sr.RequestError as e:
        status_label.config(text="Request error", foreground="red")

# Some change in Style by Using ttk 
style = ttk.Style()
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", font=("Arial", 12), background="#f5f5f5")
style.configure("TEntry", padding=5)

# This part for GUI tkinter
title_label = ttk.Label(win, text="Text to Speech & Speech to Text Converter", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

label = ttk.Label(win, text="Enter text or use the microphone:")
label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
entry = ttk.Entry(win, width=40)
entry.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

text_to_speech_button = ttk.Button(win, text="Text to Speech", command=Text_To_Speech)
text_to_speech_button.grid(row=3, column=0, padx=10, pady=10, sticky="e")

speech_to_text_button = ttk.Button(win, text="Speech to Text", command=Speech_To_Text)
speech_to_text_button.grid(row=3, column=1, padx=10, pady=10, sticky="w")

status_label = ttk.Label(win, text="", font=("Arial", 10, "italic"))
status_label.grid(row=4, column=0, columnspan=2, pady=5)

win.mainloop()

#End 'Ammar Atef'  
'''
    _____
   /     \
  |  o o  |
  |   ^   |
  |  ---  |
   \_____/
''' 
