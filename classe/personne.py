from classe.database import Database
import mysql.connector
from werkzeug.security import check_password_hash, generate_password_hash


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

            password_hash = generate_password_hash(password)
            # Insertion de l'utilisateur
            query = "INSERT INTO users (nom, prenom, email, password) VALUES (%s, %s, %s, %s)"
            data = (nom, prenom, email, password_hash)

            # Exécution de la requête
            self.db.executeQuery(query, data)
            

        except mysql.connector.Error as err:
            print(f"Erreur: {err}")

        finally:
            # Fermeture de la connexion en cas d'erreur
            self.db.disconnect()

    def connexion(self, email, password):
        try:
            self.db.connect()

            # Vérification de l'existence de l'email dans la table users
            query = "SELECT * FROM users WHERE email = %s"
            data = (email, )

            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            result = cursor.fetchone()

            if not result:
                print("Erreur : Cet email n'existe pas.")
                return None
            
            if not check_password_hash(result['password'], password):
                print("Erreur : Le mot de passe est incorrect.")
                return None

            user_details = { k: v for k, v in result.items() if k != 'password' }
            return user_details
        
        finally:
            self.db.disconnect()


    def get_user(self, email):
        try:
            self.db.connect()

            # Récupération des informations de l'utilisateur
            query = "SELECT * FROM users WHERE email = %s"
            data = (email,)

            with self.db.connection.cursor() as cursor:
                cursor.execute(query, data)
                result = cursor.fetchall()

            nom = result[0][1]
            prenom = result[0][2]
            email = result[0][3]
            visibility = "connecté"

            return nom, prenom, email, visibility

        except mysql.connector.Error as err:
            print(f"Erreur lors de la récupération des informations de l'utilisateur : {err}")

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
