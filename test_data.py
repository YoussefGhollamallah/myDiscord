import mysql.connector

class connection():
    def __init__(self):
        self.email = email
        self.password = password

    def email(self):
        return self.email 
    
    def password(self):
        return password

def verifier_connexion(email, password):
    # Se connecter à la base de données MySQL
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydiscord"
        )
        
        cursor = connection.cursor()

        # Exécuter la requête pour vérifier l'existence de l'utilisateur
        cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, password))
        
        # Récupérer le résultat de la requête
        utilisateur = cursor.fetchone()

        if utilisateur:
            print("Connexion réussie !")
        else:
            print("Email ou mot de passe incorrect.")

    except mysql.connector.Error as error:
        print("Erreur lors de la connexion à la base de données:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connexion à MySQL fermée.")

# Utilisation de la fonction pour vérifier la connexion
email = input("Entrez votre email : ")
password= input("Entrez votre mot de passe : ")

verifier_connexion(email, password)
