import customtkinter as ctk
from tkinter import PhotoImage

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("DaynNight.json")  

login = ctk.CTk()
login.title("Connexion")
login.geometry("500x500")

def connexion():
    print("Bienvenue")

def inscription_action():
    login.withdraw()  # Masquer la fenêtre de connexion
    inscription = ctk.CTk()  # Créer une nouvelle fenêtre
    inscription.title("Inscription")
    inscription.geometry("500x500")

    frame = ctk.CTkFrame(master=inscription, corner_radius=30)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    nom_entry = ctk.CTkEntry(master=frame, placeholder_text="Nom")
    nom_entry.grid(row=0, column=1, columnspan=1, pady=12, padx=(10, 5), sticky="ew")

    prenom_entry = ctk.CTkEntry(master=frame, placeholder_text="Prénom")
    prenom_entry.grid(row=1, column=1, columnspan=1, pady=12, padx=(10, 5), sticky="ew")

    mail_entry = ctk.CTkEntry(master=frame, placeholder_text="Mail")
    mail_entry.grid(row=2, column=1, columnspan=1, pady=12, padx=(10, 5), sticky="ew")

    password_entry = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
    password_entry.grid(row=3, column=1, columnspan=1, pady=12, padx=(10, 5), sticky="ew")

    button_inscription = ctk.CTkButton(master=frame, text="Inscription", command=lambda: print("Inscription effectuée"))
    button_inscription.grid(row=4, column=1, pady=20, padx=(10, 5), sticky="ew")

    inscription.mainloop()

frame = ctk.CTkFrame(master=login, corner_radius=30)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

image_path = "../test/asset/logo.png" 
original_image = PhotoImage(file=image_path)
resized_image = original_image.subsample(3, 3)  

label_image = ctk.CTkLabel(master=frame, image=resized_image)
label_image.image = resized_image  
label_image.grid(row=0, column=0, columnspan=4, pady=12, padx=10)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="Mail")
champ1.grid(row=1, column=1, columnspan=2, pady=12, padx=10, sticky="ew")

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
champ2.grid(row=2, column=1, columnspan=2, pady=12, padx=10, sticky="ew")

button_connexion = ctk.CTkButton(master=frame, text="Connexion", command=connexion)
button_connexion.grid(row=4, column=1, pady=20, padx=10, sticky="ew")

button_inscription = ctk.CTkButton(master=frame, text="Inscription", command=inscription_action)
button_inscription.grid(row=4, column=2, pady=20, padx=10, sticky="ew")

login.mainloop()
