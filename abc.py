import random
import pyttsx3
from tkinter import *
import tkinter as tk
import random
import pyttsx3

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty('voice', voice[1].id)

def speak(msg):
    engine.say(msg)
    engine.runAndWait()
    
root = Tk()
root.title("Chat bot")
root.resizable(width=False, height=False)
root.geometry("800x600")  
root.config(bg="aliceblue")

botsaid = StringVar()

hello = ["hi", "is anyone there?", "hello", "good day"]
bye = ["see you later", "goodbye", "I am Leaving", "have a good day","bye"]
thanks=["thank you","Thanks for the service","thanks"]
howare = ["how are you", "whats up", "how you doing"]
name = ["who are you", "what is your name", "do you have any name", "what should i call you"]
hours = ["when are you guys open", "what are your hours", "hours of operation", "time", "work"]
doctors = ["any information about doctors?","doctors info?","doctors"]
appointments = ["book an appointment", "book", "appointment", "book appointment", "when can i come",
                "when can i meet the doctor?", "doctor meet"]
services = ["lab test", "general checkup", "doctor appointment"]
times = ["10am", "1pm", "3pm", "5pm", "8pm"]
print('''“Time and health are two precious assets that we don’t recognize and appreciate until they have been depleted.”''')

def chat():
    if userinput.get().lower() in hello:
        botan = ["Hello!", "Hi there, how can I help ?", "Greetings sir!"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))

    elif userinput.get().lower() in howare:
        botan = ["I am fine, thanks", "Happy", "I am good"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))

    elif userinput.get().lower() in name:
        botan = ["My name is Devi. I am your personal healthcare companion", "You can call me Devi",
                 "Devi the Healthcare bot in your service", "Call me Devi"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in bye:
        botan = ["Sad to see you go :(", "Talk to you later", "Goodbye", "Have a nice day"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in hours:
        botan = ["We are open 7 am to 4 pm monday to saturday"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in thanks:
        botan = ["My Pleasure","You're Welcome"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in doctors:
        botan = ["Dr.Ishan:general-surgeon, Dr.Kishan:gynecologist,  Dr.Karthik-dentist,  Dr.Kunal-cardiologist"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
    elif userinput.get().lower() in appointments:
        botan = ["select the service for booking an appointment"]
        botan2 = services
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))
        botsaid.set(botan2)
        speak(botan2)
    elif userinput.get().lower() in services:
        botan1=["You have selected " + userinput.get().lower() ]
        botan = ["enter the date of appointment in ddmmyyyy"]
        botsaid.set(botan1)
        speak(botan1)
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))

    elif userinput.get().isdigit():
        speak("entered date is ")
        speak(userinput.get())
        botan4 = userinput.get()
        speak("Select the time from")
        botsaid.set(times)
        speak(times)

    elif userinput.get().lower() in times:
        botan3 = ["Appointment booked at " + userinput.get().lower()]
        botsaid.set(random.choice(botan3))
        speak(random.choice(botan3))

    else:
        botan = ["I did not get that"]
        botsaid.set(random.choice(botan))
        speak(random.choice(botan))



head = Label(root, text="Devi : Healthcare Bot", font="Times 30 italic bold")
head.place(x=250, y=20)

holder = Frame(root)
holder.place(x=100, y=100)

usertext = Label(holder, text="Input:", font="Times 20 italic bold", height=3)
usertext.grid(row=0, column=0)

userinput = Entry(holder, font="Times 20 italic bold",width=40)
userinput.grid(row=0, column=1)

submitbtn = Button(holder, text="Submit", font="Times 20 italic bold", command=chat)
submitbtn.grid(row=2, column=1,columnspan=4)

bottext = Label(holder, text="Devi:", font="Times 20 italic bold", height=3)
bottext.grid(row=1, column=0)

botoutput = Entry(holder, textvariable=botsaid, font="Times 20 italic bold",width=40)
botoutput.grid(row=1, column=1)
root.mainloop()