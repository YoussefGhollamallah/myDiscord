import customtkinter as ctk

class AcceuilWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x700")
        self.resizable(width=False, height=False)
        self.title("MyDiscord | Acceuil")
        self.config(bg="#192841")

        # création de la frame container
        self.framechat = ctk.CTkFrame(master=self, width=750, height=660, fg_color="#203354")
        self.framechat.place(x=230, y=20)

        self.frameIsOnly = ctk.CTkFrame(master=self, width=200, height=550, fg_color="#203354")
        self.frameIsOnly.place(x=20, y=20)

        self.frameProfil = ctk.CTkFrame(master=self, width=200, height=100, fg_color="#203354")
        self.frameProfil.place(x=20, y=580)

        self.inputChat = ctk.CTkEntry(self.framechat, placeholder_text="Entrée votre messages", width=710)
        self.inputChat.place(x=250, y=635)
