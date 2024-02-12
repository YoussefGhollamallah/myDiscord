from database import Database
import mysql.connector
from hashlib import sha512

class Users:
    def __init__(self, db):
        self.db = db

    def inscription(self, nom, prenom, email, password):
        try:
            self.db.connect()

            password = password.encode()
            password_hash = sha512(password).hexdigest()

            # Insertion de l'utilisateur
            query = "INSERT INTO users (nom, prenom, email, password) VALUES (%s, %s, %s, %s)"
            data = (nom, prenom, email, password_hash)

            # Exécution de la requête
            self.db.executeQuery(query, data)

            print("Inscription réussie")

        except mysql.connector.Error as err:
            print(f"Erreur: {err}")

        finally:
            # Fermeture de la connexion
            self.db.disconnect()

# Exemple d'utilisation
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'laplateforme'
}

db = Database(**db_config)
user = Users(db)
user.inscription("Hachem", "Bastien", "justine.bastien@laplateforme.io", "test")
