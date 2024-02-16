import tkinter as tk
from tkinter import ttk

class DiscordGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Discord")
        self.master.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Définition des couleurs
        bg_color = "#36393f"
        fg_color = "#ffffff"
        accent_color = "#7289da"
        
        # Frame principal
        self.main_frame = ttk.Frame(self.master, style="Main.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame du côté gauche
        self.left_frame = ttk.Frame(self.main_frame, style="Left.TFrame", width=200)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Liste des serveurs
        self.server_list_label = ttk.Label(self.left_frame, text="Serveurs", style="Bold.TLabel")
        self.server_list_label.pack(side=tk.TOP, fill=tk.X)

        self.server_listbox = tk.Listbox(self.left_frame, bg=bg_color, fg=fg_color, selectbackground=accent_color, highlightthickness=0)
        self.server_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Frame du centre
        self.center_frame = ttk.Frame(self.main_frame, style="Center.TFrame")
        self.center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Profil utilisateur
        self.profile_frame = ttk.Frame(self.center_frame, style="Profile.TFrame", height=50)
        self.profile_frame.pack(side=tk.TOP, fill=tk.X)

        self.profile_label = ttk.Label(self.profile_frame, text="Nom d'utilisateur", style="Bold.TLabel")
        self.profile_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Messages
        self.message_frame = ttk.Frame(self.center_frame, style="Message.TFrame")
        self.message_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.message_text = tk.Text(self.message_frame, bg=bg_color, fg=fg_color, wrap=tk.WORD, font=("Helvetica", 10))
        self.message_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.message_scroll = ttk.Scrollbar(self.message_frame, command=self.message_text.yview)
        self.message_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_text.config(yscrollcommand=self.message_scroll.set)

        # Entrée de message
        self.input_frame = ttk.Frame(self.center_frame, style="Input.TFrame")
        self.input_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.message_entry = ttk.Entry(self.input_frame, style="Input.TEntry")
        self.message_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.send_button = ttk.Button(self.input_frame, text="Envoyer", style="Send.TButton", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        # Bouton de message
        self.message_button = ttk.Button(self.profile_frame, text="Message", style="Message.TButton", command=self.open_message)
        self.message_button.pack(side=tk.RIGHT, padx=10, pady=10)

def main():
    root = tk.Tk()

    # Définition du style
    style = ttk.Style(root)
    style.theme_use('clam')

    style.configure('Main.TFrame', background="#2c2f33")
    style.configure('Left.TFrame', background="#2c2f33")
    style.configure('Center.TFrame', background="#2c2f33")
    style.configure('Profile.TFrame', background="#2c2f33")
    style.configure('Message.TFrame', background="#2c2f33")
    style.configure('Input.TFrame', background="#2c2f33")
    style.configure('Bold.TLabel', foreground="#ffffff", background="#2c2f33")
    style.configure('Message.TButton', background="#7289da", foreground="#ffffff")
    style.map('Message.TButton', background=[('active', "#677bc4")])
    style.configure('Send.TButton', background="#7289da", foreground="#ffffff")
    style.map('Send.TButton', background=[('active', "#677bc4")])
    style.configure('Input.TEntry', background="#40444b", foreground="#ffffff")
    style.map('TButton', background=[('active', '#677bc4')])

    app = DiscordGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
