import mysql.connector
from datetime import datetime

class Show_message:
    def __init__(self, message, horaire, id_user):
        self.__message = message
        self.__horaire = horaire
        self.__id_user = id_user
    
    def get_message(self):  # Modifier le nom de la méthode pour correspondre à l'attribut
        return self.__message
    
    def get_heure(self):
        return self.__horaire
    
    def get_id_user(self):
        return self.__id_user
    
    def set_message(self, message):  # Modifier le nom de la méthode pour correspondre à l'attribut
        self.__message = message
    
    def set_heure(self,horaire):
        self.__horaire = horaire

class Select_message:
    def __init__(self):
        # Établir la connexion à MySQL
        self.connexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydiscord"
        )
        self.curseur = self.connexion.cursor()
        
    def afficher_messages(self):
        requete = "SELECT * FROM message WHERE id_user IN (1, 2) ORDER BY id_user"  # Requête modifiée
        self.curseur.execute(requete)
        resultats = self.curseur.fetchall()  # Récupération des résultats
        for row in resultats:
            # Création d'un objet Show_message pour chaque ligne de résultat
            message = Show_message(row[0], row[1], row[2])
            print("Message:", message.get_message())  # Utiliser la méthode correcte pour obtenir le message
