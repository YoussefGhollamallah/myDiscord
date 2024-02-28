import customtkinter as tk
from PIL import Image, ImageTk

def load_and_resize_avatar(image_path, size):
    avatar = Image.open(image_path)
    avatar_photo = ImageTk.PhotoImage(avatar)
    return avatar_photo

# Créer la fenêtre principale
root = tk.CTk()

# Créer un conteneur pour organiser les widgets
frame = tk.CTkFrame(root)
frame.pack(padx=10, pady=40)

# Ajouter les informations du profil
name_label = tk.CTkLabel(frame, text="Nom : Jean ticipe").place(x=10, y=10)

email_label = tk.CTkLabel(frame, text="Email : jean.ticipe@gmail.com").place(x=10, y=40)

# Charger et redimensionner l'image de l'avatar
avatar_photo = load_and_resize_avatar('asset/utilisateur.png', (100,100))

# Ajouter l'image de l'avatar
avatar_label = tk.CTkLabel(frame, image=avatar_photo)
avatar_label.grid(row=0, column=1, rowspan=2, padx=10)

# Définir la taille de la fenêtre
root.geometry("400x400")
root.resizable(width=False, height=False)
root.configure(bg="#192841")
root.title("MyDiscord | Profil")


# Démarrer la boucle principale
root.mainloop()
