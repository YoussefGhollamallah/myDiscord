import tkinter as tk
from PIL import Image, ImageTk

def load_and_resize_avatar(image_path, size):
    avatar = Image.open(image_path)
    
    avatar_photo = ImageTk.PhotoImage(avatar)
    return avatar_photo

# Créer la fenêtre principale
root = tk.Tk()
root.configure(background='#333333')  # Fond gris-noir

# Créer un conteneur pour organiser les widgets
frame = tk.Frame(root, bg='#333333')  # Fond gris-noir
frame.pack(padx=15, pady=15)

# Ajouter les informations du profil
name_label = tk.Label(frame, text="Nom : Jean ticipe",  font=("Arial", 12), bg='#333333', fg='white')  # Fond gris-noir, texte blanc
name_label.grid(row=0, column=0, sticky='w')

email_label = tk.Label(frame, text="Email : jean.ticipe@gmail.com",  font=("Arial", 12), bg='#333333', fg='white')  # Fond gris-noir, texte blanc
email_label.grid(row=1, column=0, sticky='w')

# Charger et redimensionner l'image de l'avatar
avatar_photo = load_and_resize_avatar('asset/avatar1.png', (100,100))

# Ajouter l'image de l'avatar
avatar_label = tk.Label(frame, image=avatar_photo, bg='#333333')  # Fond gris-noir
avatar_label.grid(row=0, column=1, rowspan=2, padx=10)

# Définir la taille de la fenêtre
root.geometry("400x350")

# Démarrer la boucle principale
root.mainloop()
