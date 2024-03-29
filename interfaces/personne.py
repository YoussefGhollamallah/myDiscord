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

    def inscription(self, nom, prenom, email, password, visibility=0):
        
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

    def connexion(self, email, password, visibility=1):
        try:
            self.db.connect()

            # Vérification de l'existence de l'email dans la table users
            query = "SELECT * FROM users WHERE email = %s"
            data = (email,)

            with self.db.connection.cursor() as cursor:
                cursor.execute(query, data)
                result = cursor.fetchall()

            if len(result) == 0:
                print("Erreur : Cet email n'existe pas.")
                return

            # Vérification du mot de passe
            stored_password_hash = result[0][4]  # La colonne password est la cinquième (index 4)
            input_password_hash = sha512(password.encode('utf-8')).hexdigest()


            if stored_password_hash != input_password_hash:
                print("Erreur : Mot de passe incorrect.")
                return

            print("Connexion réussie")

        except mysql.connector.Error as err:
            print(f"Erreur lors de la connexion : {err}")

        finally:
            self.db.disconnect()


# Exemple d'utilisation
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'mydiscord'
}

db = Database(**db_config)
user = Users(db)
