import customtkinter

screenAcceuil = customtkinter.CTk()

screenAcceuil.geometry("1000x700")
screenAcceuil.resizable(width=False, height=False)
screenAcceuil.title("MyDiscord | Acceuil")
screenAcceuil.config(bg="#192841")

# création de la frame container
framechat = customtkinter.CTkFrame(master=screenAcceuil, width=750, height=660, fg_color="#203354").place(x=230, y=20)
frameIsOnly = customtkinter.CTkFrame(master=screenAcceuil, width=200, height=550, fg_color="#203354").place(x=20,y=20)
frameProfil = customtkinter.CTkFrame(master=screenAcceuil, width=200, height=100, fg_color="#203354").place(x=20,y=580)


inputChat = customtkinter.CTkEntry(framechat, placeholder_text="Entrée votre messages", width=710).place(x =250, y = 635)

screenAcceuil.mainloop()