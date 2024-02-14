import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Définit le mode sombre pour l'apparence
ctk.set_default_color_theme("dark-blue")  # Définit le thème de couleur par défaut

inscription = ctk.CTk()
inscription.title("Inscription")
inscription.geometry("500x500")

def inscription_action():
    print("Inscription effectuée")

frame = ctk.CTkFrame(master=inscription, corner_radius=30)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Configuration de la grille à l'intérieur du frame
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

# Boutons placés en bas du frame et collés aux côtés
button_inscription = ctk.CTkButton(master=frame, text="Inscription", command=inscription_action)
button_inscription.grid(row=4, column=1, pady=20, padx=(10, 5), sticky="ew")

inscription.mainloop()
