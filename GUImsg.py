import tkinter as tk
from tkinter import scrolledtext, messagebox
import emoji

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat avec Emojis")
        self.root.configure(background='#000000')  # Couleur de fond pour la fenêtre principale

        # Cadre pour afficher les messages
        self.messages_frame = tk.Frame(root, bg='#000000')  
        self.scrollbar = tk.Scrollbar(self.messages_frame)  # Pour faire défiler les messages
        self.msg_list = scrolledtext.ScrolledText(self.messages_frame, height=20, width=50, yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
        self.msg_list.config(state=tk.DISABLED)
        self.messages_frame.pack(padx=10, pady=10)

        # Champ de saisie pour les messages
        self.entry_field = tk.Entry(root, width=40, bg='#ffffff')  # Couleur de fond pour le champ de saisie
        self.entry_field.bind("<Return>", self.send_message)
        self.entry_field.pack(side=tk.LEFT, padx=10, pady=5)

        # Bouton pour envoyer un message
        self.send_button = tk.Button(root, text="Envoyer", command=self.send_message, bg='#F0F0F0', fg='#370028')  
        self.send_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Boutons d'emojis
        self.emojis = ["😊", "😂", "😍", "😎", "😜", "😡"]
        self.emoji_buttons = []
        for emoji_unicode in self.emojis:
            emoji_button = tk.Button(root, text=emoji_unicode, font=('Segoe UI Emoji', 12), command=lambda e=emoji_unicode: self.insert_emoji(e), bg='#FDFEDF')  # Couleur de fond pour les boutons emoji
            emoji_button.pack(side=tk.LEFT, padx=5, pady=5)
            self.emoji_buttons.append(emoji_button)

    def insert_emoji(self, emoji):
        self.entry_field.insert(tk.END, emoji)

    def send_message(self, event=None):
        message = self.entry_field.get()
        if message.strip():
            # Afficher le message de l'utilisateur dans une bulle de message
            self.msg_list.config(state=tk.NORMAL)
            self.msg_list.insert(tk.END, "Vous: \n") #remplacer vous par nom prenom
            self.msg_list.insert(tk.END, f"{message}\n", 'sent_message')
            self.msg_list.config(state=tk.DISABLED)
            self.msg_list.tag_configure('sent_message', justify='right', foreground='white', background='#645552', font=('Arial', 10))  # Ajuster la taille de la police
            self.msg_list.yview(tk.END)  
            self.entry_field.delete(0, tk.END)

root = tk.Tk()
chat = ChatGUI(root)
root.mainloop()
