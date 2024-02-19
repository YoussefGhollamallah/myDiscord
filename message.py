import mysql.connector

class Message():
    def __init__(self, message, id_utilisateur):
        self.__message = message
        self.__id_utilisateur = id_utilisateur

    def obtenir_message(self):
        return self.__message
    
    def obtenir_id_utilisateur(self):
        return self.__id_utilisateur
        
    def definir_message(self, message):
        self.__message = message
    
    def definir_id_utilisateur(self, id_utilisateur):
        self.__id_utilisateur = id_utilisateur

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

    def creer_message(self, message, id_user):
        # Créer un nouveau message dans la base de données
        requete = "INSERT INTO messages (message, id_user) VALUES (%s, %s)"
        donnees = (message, id_user)
        self.curseur.execute(requete, donnees)
        self.connexion.commit()
        print("Message créé avec succès.")
        
        createur_message = Create_message()
        createur_message.creer_message("Bonjour tout le monde!", 123) 
        createur_message.fermer_connexion()

    def fermer_connexion(self):
        # Fermer la connexion à la base de données
        self.connexion.close()
        print("Connexion fermée.")
