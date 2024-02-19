import tkinter as tk
from tkinter import ttk
import emoji

class ChatApp:
    def __init__(self, window):
        self.window = window
        self.window.title("WhatsApp Style Chat")
        
        self.style = ttk.Style()
        self.style.configure("Me.TLabel", background="#DCF8C6", foreground="black", justify="right", relief="raised")
        self.style.configure("You.TLabel", background="#FFFFFF", foreground="black", justify="left", relief="raised")

        self.messages_frame = tk.Frame(self.window, bg="#183B59")
        self.messages_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.messages_list = tk.Listbox(self.messages_frame, width=50, height=15, bg="#183B59", fg="white", font=("Arial", 10))
        self.messages_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.entry_field = tk.Entry(self.window, width=50, font=("Arial", 10))
        self.entry_field.pack(padx=10, pady=10)

        self.send_button = tk.Button(self.window, text="Envoyer", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self):
        message = self.entry_field.get()
        if message:
            message_with_emoji = emoji.emojize(message, use_aliases=True)
            self.messages_list.insert(tk.END, "Moi: " + message_with_emoji)
            self.messages_list.itemconfig(tk.END, {'bg': '#DCF8C6', 'relief': 'raised'})
            self.entry_field.delete(0, tk.END)

def main():
    window = tk.Tk()
    app = ChatApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
