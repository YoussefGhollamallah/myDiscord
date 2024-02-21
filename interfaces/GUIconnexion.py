import customtkinter


class ConnexionWindow(customtkinter.CTk):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.iconbitmap("images/discord.ico")
        self.geometry("1000x700")
        self.resizable(width=False, height=False)
        self.title("MyDiscord | Connexion")
        self.config(bg="#192841")

        # création de la frame container
        frameconnexion = customtkinter.CTkFrame(master=self, width=900, height=600, fg_color="#203354")
        frameconnexion.place(x=50, y=50)

        # création des entrées pour l'inscription de l'utilisateur
        labelConnexion = customtkinter.CTkLabel(frameconnexion, text="CONNEXION", font=(None, 20), fg_color="transparent").place(x=400, y=45)

        labelEmail = customtkinter.CTkLabel(frameconnexion, text="Email", font=(None, 16), fg_color="transparent").place(x=400, y=185)
        entreeEmail = customtkinter.CTkEntry(frameconnexion, placeholder_text="Votre email")
        entreeEmail.place(x=400, y=225)

        labelPassword = customtkinter.CTkLabel(frameconnexion, text="Password", font=(None, 16), fg_color="transparent").place(x=400, y=255)
        entreePassword_var = customtkinter.StringVar()  # Variable pour le mot de passe
        entreePassword = customtkinter.CTkEntry(frameconnexion, placeholder_text="Password", show="*", textvariable=entreePassword_var)
        entreePassword.place(x=400, y=290)

        def checkbox_event():
            if check_var.get() == "on":
                entreePassword.configure(show="")
            else:
                entreePassword.configure(show="*")

        check_var = customtkinter.StringVar(value="off")
        checkbox = customtkinter.CTkCheckBox(frameconnexion, text="Afficher mot de passe", command=checkbox_event,
                                             variable=check_var, onvalue="on", offvalue="off").place(x=400, y=330)

        buttonConnexion = customtkinter.CTkButton(frameconnexion, text="Se connecter").place(x=400, y=450)

