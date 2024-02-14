import customtkinter as ctk
from tkinter import PhotoImage

ctk.set_appearance_mode("dark")  # Définit le mode sombre pour l'apparence
ctk.set_default_color_theme("dark-blue")  # Définit le thème de couleur par défaut

login = ctk.CTk()
login.title("Connexion")
login.geometry("500x500")

def connexion():
    print("Bienvenue")

frame = ctk.CTkFrame(master=login, corner_radius=30)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Configuration de la grille à l'intérieur du frame
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

# Charger l'image et la redimensionner
image_path = "../test/asset/logo.png" # Remplacez cela par le chemin vers votre image PNG
original_image = PhotoImage(file=image_path)
# Redimensionner l'image à 100x100 pixels
resized_image = original_image.subsample(3, 3)  # Changer les valeurs de subsample selon vos besoins

# Utilisation de l'image dans un CTkLabel
label_image = ctk.CTkLabel(master=frame, image=resized_image)
label_image.image = resized_image  # Gardez une référence
label_image.grid(row=0, column=0, columnspan=4, pady=12, padx=10)

champ1 = ctk.CTkEntry(master=frame, placeholder_text="Mail")
champ1.grid(row=1, column=1, columnspan=2, pady=12, padx=10, sticky="ew")

champ2 = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
champ2.grid(row=2, column=1, columnspan=2, pady=12, padx=10, sticky="ew")

# Boutons placés en bas du frame et collés aux côtés
button_connexion = ctk.CTkButton(master=frame, text="Connexion", command=connexion)
button_connexion.grid(row=4, column=1, pady=20, padx=10, sticky="ew")

button_inscription = ctk.CTkButton(master=frame, text="Inscription", command=connexion)
button_inscription.grid(row=4, column=2, pady=20, padx=10, sticky="ew")


login.mainloop()






