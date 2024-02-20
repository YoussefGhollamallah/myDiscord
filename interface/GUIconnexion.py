import customtkinter

# Mise en place de l'écran
screenConnexion = customtkinter.CTk()
screenConnexion.iconbitmap("./images/discord.ico")
screenConnexion.geometry("1000x700")
screenConnexion.resizable(width=False, height=False)
screenConnexion.title("MyDiscord | Connexion")
screenConnexion.config(bg="#192841")

# création de la frame container
frame = customtkinter.CTkFrame(master=screenConnexion, width=900, height=600, fg_color="#203354")
frame.place(x=50, y=50)

# création des entrées pour la'inscription de l'utilisateur
labelConnexion = customtkinter.CTkLabel(frame, text="CONNEXION", font=(None, 20), fg_color="transparent").place(x=400, y=45)

labelEmail = customtkinter.CTkLabel(frame, text="Email", font=(None, 16), fg_color="transparent").place(x=400, y=185)
entreeEmail = customtkinter.CTkEntry(frame, placeholder_text="Votre email")
entreeEmail.place(x=400, y=225)

labelPassword = customtkinter.CTkLabel(frame, text="Password", font=(None, 16), fg_color="transparent").place(x=400, y=255)
entreePassword_var = customtkinter.StringVar()  # Variable pour le mot de passe
entreePassword = customtkinter.CTkEntry(frame, placeholder_text="Password", show="*", textvariable=entreePassword_var)
entreePassword.place(x=400, y=290)

def checkbox_event():
    if check_var.get() == "on":
        entreePassword.configure(show="")
    else:
        entreePassword.configure(show="*")

check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(frame, text="Afficher mot de passe", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off").place(x=400, y=330)

buttonConnexion = customtkinter.CTkButton(frame, text="Se connecter").place(x=400, y=450)

screenConnexion.mainloop()
