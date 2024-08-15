import tkinter as tk
import customtkinter as ctk

#System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Our app frame
app = ctk.CTk()
app.geometry("720x480")
app.title("Game time tracker")

# Adding UI elements
title = ctk.CTkLabel(app, text="Welcome to GTT")
title.pack(padx=10, pady=10)

valButton = ctk.CTkButton(app, text="Valorant")
valButton.pack(padx=10, pady=10)

# Screen for each individual game
# Valorant
def valorant():
    val = ctk.CTk()
    val.geometry("720x480")
    val.title("Valorant")

if valButton:
    valorant()

# Run loop
app.mainloop()
