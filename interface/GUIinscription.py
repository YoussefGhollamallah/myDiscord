import customtkinter
# from classe.Users import *

# user = Users(db)
# Mise en place de l'écran
screenInscription = customtkinter.CTk()
screenInscription.iconbitmap("./images/discord.ico")
screenInscription.geometry("1000x700")
screenInscription.resizable(width=False, height=False)
screenInscription.title("MyDiscord | inscription")
screenInscription.config(bg="#192841")


# création de la frame container
frame = customtkinter.CTkFrame(master=screenInscription, width=900, height=600,fg_color="#203354")
frame.place(x=50, y=50)

# création des entrées pour l'inscription de l'utilisateur
labelInscription = customtkinter.CTkLabel(frame, text="INSCRIPTION",font=(None,20), fg_color="transparent").place(x= 400, y = 25)

labelNom = customtkinter.CTkLabel(frame, text="Nom",font=(None,16), fg_color="transparent").place(x= 400, y = 70)
entreeNom = customtkinter.CTkEntry(frame,placeholder_text="Votre nom" ).place(x=400, y= 105)
labelPrenom = customtkinter.CTkLabel(frame, text="Prénom",font=(None,16), fg_color="transparent").place(x= 400, y = 175)
entreePrenom = customtkinter.CTkEntry(frame,placeholder_text="Votre Prenom" ).place(x=400, y= 210)
labelEmail = customtkinter.CTkLabel(frame, text="Email",font=(None,16), fg_color="transparent").place(x= 400, y = 275)
entreeEmail = customtkinter.CTkEntry(frame,placeholder_text="Votre email" ).place(x=400, y= 305)
labelPassword = customtkinter.CTkLabel(frame, text="Password",font=(None,16), fg_color="transparent").place(x= 400, y = 375)
entreePassword = customtkinter.CTkEntry(frame,placeholder_text="Password" ).place(x=400, y= 405)

buttonInscription = customtkinter.CTkButton(frame, text="S'inscrire").place(x=400,y=450)

screenInscription.mainloop()