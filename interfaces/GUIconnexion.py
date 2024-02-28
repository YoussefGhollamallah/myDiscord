import customtkinter
from personne import *
from GUIacceuil import AcceuilWindow

class ConnexionWindow(customtkinter.CTk):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.iconbitmap("images/discord.ico")
        self.geometry("1000x700")
        self.resizable(width=False, height=False)
        self.title("MyDiscord | Connexion")
        self.config(bg="#192841")

        # création de la frame container
        self.frameconnexion = customtkinter.CTkFrame(master=self, width=900, height=600, fg_color="#203354")
        self.frameconnexion.place(x=50, y=50)

        # création des entrées pour l'inscription de l'utilisateur
        labelConnexion = customtkinter.CTkLabel(self.frameconnexion, text="CONNEXION", font=(None, 20), fg_color="transparent")
        labelConnexion.place(x=400, y=45)

        labelEmail = customtkinter.CTkLabel(self.frameconnexion, text="Email", font=(None, 16), fg_color="transparent")
        labelEmail.place(x=400, y=185)
        self.entreeEmail = customtkinter.CTkEntry(self.frameconnexion, placeholder_text="Votre email")
        self.entreeEmail.place(x=400, y=225)

        labelPassword = customtkinter.CTkLabel(self.frameconnexion, text="Password", font=(None, 16), fg_color="transparent")
        labelPassword.place(x=400, y=255)
        self.entreePassword_var = customtkinter.StringVar()  # Variable pour le mot de passe
        self.entreePassword = customtkinter.CTkEntry(self.frameconnexion, placeholder_text="Password", show="*", textvariable=self.entreePassword_var)
        self.entreePassword.place(x=400, y=290)

        self.check_var = customtkinter.StringVar(value="off")
        checkbox = customtkinter.CTkCheckBox(self.frameconnexion, text="Afficher mot de passe", command=self.checkbox_event,
                                             variable=self.check_var, onvalue="on", offvalue="off")
        checkbox.place(x=400, y=330)

        buttonConnexion = customtkinter.CTkButton(self.frameconnexion, text="Se connecter", command=self.login_user)
        buttonConnexion.place(x=400, y=450)

    def checkbox_event(self):
        if self.check_var.get() == "on":
            self.entreePassword.configure(show="")
        else:
            self.entreePassword.configure(show="*")

    def login_user(self):
        email = self.entreeEmail.get()
        password = self.entreePassword_var.get()

        # Assuming the Users class has a method to fetch user details after login
        user_details = Users(self.db).get_user_details(email, password)

        if user_details:
            self.destroy()  # Close the current window

            # Open the GUIacceuil window with the user details
            acceuil_window = AcceuilWindow(user_details)
            acceuil_window.mainloop()
