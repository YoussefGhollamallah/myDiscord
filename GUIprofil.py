import tkinter as tk
from PIL import Image, ImageTk

def load_and_resize_avatar(image_path, size):
    avatar = Image.open(image_path)
    avatar_photo = ImageTk.PhotoImage(avatar)
    return avatar_photo

# Créer la fenêtre principale
root = tk.Tk()

# Créer un conteneur pour organiser les widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Ajouter les informations du profil
name_label = tk.Label(frame, text="Nom : Jean ticipe")
name_label.grid(row=0, column=0)

email_label = tk.Label(frame, text="Email : jean.ticipe@gmail.com")
email_label.grid(row=1, column=0)

# Charger et redimensionner l'image de l'avatar
avatar_photo = load_and_resize_avatar('asset/avatar.png', (100,100))

# Ajouter l'image de l'avatar
avatar_label = tk.Label(frame, image=avatar_photo)
avatar_label.grid(row=0, column=1, rowspan=2, padx=10)

# Définir la taille de la fenêtre
root.geometry("400x120")

# Démarrer la boucle principale
root.mainloop()
