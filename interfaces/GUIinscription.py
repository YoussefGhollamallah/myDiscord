import customtkinter

class InscriptionWindow(customtkinter.CTk):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.iconbitmap("images/discord.ico")
        self.geometry("1000x700")
        self.resizable(width=False, height=False)
        self.title("MyDiscord | Inscription")
        self.config(bg="#192841")

        # création de la frameinscription container
        frameinscription = customtkinter.CTkFrame(master=self, width=900, height=600, fg_color="#203354")
        frameinscription.place(x=50, y=50)

        # création des entrées pour l'inscription de l'utilisateur
        labelInscription = customtkinter.CTkLabel(frameinscription, text="INSCRIPTION", font=(None, 20), fg_color="transparent").place(x=400, y=25)

        labelNom = customtkinter.CTkLabel(frameinscription, text="Nom", font=(None, 16), fg_color="transparent").place(x=400, y=70)
        entreeNom = customtkinter.CTkEntry(frameinscription, placeholder_text="Votre nom").place(x=400, y=105)

        labelPrenom = customtkinter.CTkLabel(frameinscription, text="Prénom", font=(None, 16), fg_color="transparent").place(x=400, y=175)
        entreePrenom = customtkinter.CTkEntry(frameinscription, placeholder_text="Votre Prenom").place(x=400, y=210)

        labelEmail = customtkinter.CTkLabel(frameinscription, text="Email", font=(None, 16), fg_color="transparent").place(x=400, y=275)
        entreeEmail = customtkinter.CTkEntry(frameinscription, placeholder_text="Votre email").place(x=400, y=310)

        labelPassword = customtkinter.CTkLabel(frameinscription, text="Password", font=(None, 16), fg_color="transparent").place(x=400, y=375)
        entreePassword = customtkinter.CTkEntry(frameinscription, placeholder_text="Password").place(x=400, y=410)

        buttonInscription = customtkinter.CTkButton(frameinscription, text="S'inscrire").place(x=400, y=450)


