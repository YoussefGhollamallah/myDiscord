import customtkinter
from PIL import Image
import os

screenBienvenue = customtkinter.CTk()

image_width = 100
image_height = 100
icon_path = "images/discord.png"

screenBienvenue.iconbitmap("./images/discord.ico")
screenBienvenue.geometry("1000x700")
screenBienvenue.resizable(width=False, height=False)
screenBienvenue.title("MyDiscord")
screenBienvenue.config(bg="#192841")

icon = customtkinter.CTkImage(light_image=Image.open(os.path.join(icon_path)), size=(image_width,image_height))
icon_position = customtkinter.CTkLabel(master=screenBienvenue, image=icon).place(x = 470 , y =250)

def function_connexion():
    print("connecté")

def function_inscription():
    print("inscription")

button_connexion = customtkinter.CTkButton(screenBienvenue, text="se connecter", command=function_connexion).place(x = 350 , y = 450)
button_inscription = customtkinter.CTkButton(screenBienvenue,text="s'inscrire", command=function_inscription).place(x= 550, y = 450)


screenBienvenue.mainloop()