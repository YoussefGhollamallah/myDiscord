from database import Database
import mysql.connector
from hashlib import sha512

class Users:
    def __init__(self, db):
        self.db = db

    def email_exists(self, email):
        try:
            self.db.connect()

            # Vérification de l'existence de l'email dans la table users
            query = "SELECT * FROM users WHERE email = %s"
            data = (email,)

            # Exécution de la requête avec le curseur utilisé comme gestionnaire de contexte
            with self.db.connection.cursor() as cursor:
                cursor.execute(query, data)
                result = cursor.fetchall()

            return len(result) > 0

        except mysql.connector.Error as err:
            print(f"Erreur lors de la vérification de l'email: {err}")
            return False

        finally:
            # Fermeture de la connexion en cas d'erreur
            self.db.disconnect()

    def inscription(self, nom, prenom, email, password):
        try:
            # Vérification de l'existence de l'email
            if self.email_exists(email):
                print("Erreur: Cet email est déjà utilisé.")
                return

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
            # Fermeture de la connexion en cas d'erreur
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
