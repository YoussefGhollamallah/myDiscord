import customtkinter as ctk
from PIL import Image
from GUIconnexion import *
from GUIinscription import *

screenBienvenue = ctk.CTk()

# Keep a reference to the CTkImage object
# avatar_image = Image.open("asset/logo.png")
# avatar = ctk.CTkImage(light_image=avatar_image, size=(100, 100))

# image_label = ctk.CTkLabel(screenBienvenue, image=avatar, text='')
# image_label.place(x=450, y=100)

screenBienvenue.geometry("1000x700")
screenBienvenue.resizable(width=False, height=False)
screenBienvenue.title("MyDiscord")
screenBienvenue.config(bg="#192841")

def function_connexion():
    screenBienvenue.destroy()
    screenConnexion = ConnexionWindow()
    screenConnexion.mainloop()

def function_inscription():
    screenBienvenue.destroy()
    inscription_window = InscriptionWindow()
    inscription_window.mainloop()

button_connexion = ctk.CTkButton(screenBienvenue, text="se connecter", command=function_connexion)
button_connexion.place(x=350, y=450)

button_inscription = ctk.CTkButton(screenBienvenue, text="s'inscrire", command=function_inscription)
button_inscription.place(x=550, y=450)

screenBienvenue.mainloop()
