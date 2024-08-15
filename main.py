import tkinter as tk
import customtkinter as ctk
import wmi
f = wmi.WMI() 
import time

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Our app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Game time tracker")

def clearWidgets():
    for widget in app.winfo_children():
        widget.destroy()

def backButton():
    mainButton = ctk.CTkButton(app, text="Back", command = mainMenu, width = 65)
    mainButton.place(x=1, y=1)

def mainMenu():
    clearWidgets()
    main = app
    main.title("Main Menu")
    valButton = ctk.CTkButton(app, text="Valorant", command = valorant)
    valButton.pack(padx=10, pady=10)
    RLButton = ctk.CTkButton(app, text="Rocket League", command = rocketLeague)
    RLButton.pack(padx=10, pady=10)

# Welcome screen
title = ctk.CTkLabel(app, text="Welcome to GTT")
title.pack(padx=10, pady=10)

welcomeButton = ctk.CTkButton(app, text="Click to continue", command = mainMenu)
welcomeButton.pack(padx=10, pady=10)

# Screen for each individual game
def valorant():

    clearWidgets()
    val = app
    val.title("Valorant")

    backButton()

    valHours = ctk.CTkLabel(app, text="You have played XXX hours of Valorant")
    valHours.pack(padx=10, pady=10)

    flagVal = 0
    for process in f.Win32_Process(): 
        if "VALORANT-Win64-Shipping.exe" == process.Name: 
            valRunning = True
            flagVal = 1
            break
    if flagVal == 0:
        valRunning = False
    if valRunning:
        valStatus = ctk.CTkLabel(app, text="Valorant is running.")
        valStatus.pack(padx=10,pady=10)
    else:
        valStatus = ctk.CTkLabel(app, text="Valorant is not running")
        valStatus.pack(padx=10,pady=10)
    
def rocketLeague():

    clearWidgets()
    RL = app
    RL.title("Rocket League")

    backButton()

    RLHours = ctk.CTkLabel(app, text="You have played XXX hours of Rocket League")
    RLHours.pack(padx=10, pady=10)

    flagRL = 0
    for process in f.Win32_Process(): 
        if "RocketLeague.exe" == process.Name: 
            RLRunning = True
            flagRL = 1
            break
    if flagRL == 0:
        RLRunning = False
    if RLRunning:
        valStatus = ctk.CTkLabel(app, text="Rocket League is running")
        valStatus.pack(padx=10,pady=10)
    else:
        valStatus = ctk.CTkLabel(app, text="Rocket League is not running")
        valStatus.pack(padx=10,pady=10)

# Run loop
app.mainloop()