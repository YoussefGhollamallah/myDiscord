import mysql.connector
from datetime import datetime

class Message():
    def __init__(self, message, id_user):
        self.__message = message
        self.__id_user = id_user

    def get_message(self):
        return self.__message
    
    def get_id_utilisateur(self):
        return self.__id_user
        
    def set_message(self, message):
        self.__message = message
    
    def set_id_utilisateur(self, id_user):
        self.__id_user = id_user

class Create_message(Message):
    def __init__(self):
        # Établir la connexion à MySQL
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydiscord"
        )
        self.curseur = self.connexion.cursor()

    def verifier_utilisateur_existe(self, id_user):
        # Vérifier si l'utilisateur avec l'ID s'il existe dans la base de données
        requete = "SELECT COUNT(*) FROM users WHERE id = %s"
        self.curseur.execute(requete, (id_user,))
        nombre_utilisateurs = self.curseur.fetchone()[0]
        return nombre_utilisateurs > 0

    def creer_message(self, message, id_user):
        # Vérifier si l'utilisateur existe dans la base de données
        if not self.verifier_utilisateur_existe(id_user):
            print("Erreur: L'utilisateur avec l'ID donné n'existe pas.")
            return
        
        # Créer un nouveau message dans la base de données
        now = datetime.now()  # Obtenir l'heure actuelle
        horaire = now.strftime("%Y-%m-%d %H:%M:%S")  # Formatter l'heure
        requete = "INSERT INTO messages (message, id_user, horaire) VALUES (%s, %s, %s)"
        donnees = (message, id_user, horaire)
        self.curseur.execute(requete, donnees)
        self.connexion.commit()
        print("Message créé avec succès.")
        
    def fermer_connexion(self):
        # Fermer la connexion à la base de données
        self.connexion.close()
        print("Connexion fermée.")

createur_message = Create_message()
createur_message.creer_message("Bonjour tout le monde!", 1)
createur_message.creer_message("ça va ?", 2)
createur_message.creer_message("salutation!", 3)
createur_message.fermer_connexion()
