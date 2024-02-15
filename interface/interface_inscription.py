import tkinter as tk
from tkinter import ttk

class InterfaceInscription(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Inscription")
        self.geometry("800x600")
        self.config(background="#211951")

        

        self.label_prenom = tk.Label(self, text="Prénom:")
        self.label_prenom.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.label_nom = tk.Label(self, text="Nom:")
        self.label_nom.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_nom = tk.Entry(self)
        self.entry_nom.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.label_email = tk.Label(self, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.label_mot_de_passe = tk.Label(self, text="Mot de passe:")
        self.label_mot_de_passe.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.entry_mot_de_passe = tk.Entry(self, show="*")
        self.entry_mot_de_passe.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.bouton_inscrire = tk.Button(self, text="S'inscrire", command=self.inscrire)
        self.bouton_inscrire.grid(row=4, column=0, columnspan=2, pady=20)

    def inscrire(self):
        nom = self.entry_nom.get()
        email = self.entry_email.get()
        mot_de_passe = self.entry_mot_de_passe.get()

        # Ici, vous pouvez implémenter la logique d'inscription avec les données fournies
        print(f"Nom: {nom}\nEmail: {email}\nMot de passe: {mot_de_passe}")

