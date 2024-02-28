import customtkinter
from personne import *

class InscriptionWindow(customtkinter.CTk):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.geometry("1000x700")
        self.resizable(width=False, height=False)
        self.title("MyDiscord | Inscription")
        self.config(bg="#192841")

        # création de la frameinscription container
        frameinscription = customtkinter.CTkFrame(master=self, width=900, height=600, fg_color="#203354")
        frameinscription.place(x=50, y=50)

        # création des entrées pour l'inscription de l'utilisateur
        self.labelInscription = customtkinter.CTkLabel(frameinscription, text="INSCRIPTION", font=(None, 20), fg_color="transparent")
        self.labelInscription.place(x=400, y=25)

        self.labelNom = customtkinter.CTkLabel(frameinscription, text="Nom", font=(None, 16), fg_color="transparent")
        self.labelNom.place(x=400, y=70)
        self.entreeNom = customtkinter.CTkEntry(frameinscription, placeholder_text="Votre nom")
        self.entreeNom.place(x=400, y=105)

        self.labelPrenom = customtkinter.CTkLabel(frameinscription, text="Prénom", font=(None, 16), fg_color="transparent")
        self.labelPrenom.place(x=400, y=175)
        self.entreePrenom = customtkinter.CTkEntry(frameinscription, placeholder_text="Votre Prenom")
        self.entreePrenom.place(x=400, y=210)

        labelEmail = customtkinter.CTkLabel(frameinscription, text="Email", font=(None, 16), fg_color="transparent")
        labelEmail.place(x=400, y=275)
        self.entreeEmail = customtkinter.CTkEntry(frameinscription, placeholder_text="Votre email")
        self.entreeEmail.place(x=400, y=310)

        labelPassword = customtkinter.CTkLabel(frameinscription, text="Password", font=(None, 16), fg_color="transparent")
        labelPassword.place(x=400, y=375)
        self.entreePassword = customtkinter.CTkEntry(frameinscription, placeholder_text="Password")
        self.entreePassword.place(x=400, y=410)

        self.buttonInscription = customtkinter.CTkButton(frameinscription, text="S'inscrire", command=self.register_user)
        self.buttonInscription.place(x=400, y=450)

    def register_user(self):
        nom = self.entreeNom.get()
        prenom = self.entreePrenom.get()
        email = self.entreeEmail.get()
        password = self.entreePassword.get()
        user.inscription(nom=nom, prenom=prenom, email=email, password=password)
        
inscription_window = InscriptionWindow()