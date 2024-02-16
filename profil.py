import tkinter as tk
from tkinter import ttk

def show_profile():
    profile_window = tk.Toplevel(root)
    profile_window.title("Profil")
    profile_window.geometry("300x200")
    profile_window.resizable(False, False)

    style = ttk.Style()
    style.configure("Profile.TLabel", font=("Helvetica", 12))
    style.configure("Profile.TButton", font=("Helvetica", 10), padding=5)

    username_label = ttk.Label(profile_window, text="Nom d'utilisateur: JohnDoe#1234", style="Profile.TLabel")
    username_label.pack(pady=10)

    status_label = ttk.Label(profile_window, text="Statut: En ligne", style="Profile.TLabel")
    status_label.pack(pady=5)

    profile_button = ttk.Button(profile_window, text="Fermer", command=profile_window.destroy, style="Profile.TButton")
    profile_button.pack(pady=10)

root = tk.Tk()
root.title("Discord")
root.geometry("200x100")
root.resizable(False, False)

style = ttk.Style()
style.configure("Profile.TButton", font=("Helvetica", 10), padding=5)

profile_button = ttk.Button(root, text="Profil", command=show_profile, style="Profile.TButton")
profile_button.pack(pady=20, padx=50)

root.mainloop()
