import mysql.connector
from datetime import datetime

class Show_message:
    def __init__(self, messages, horaire, id_user):
        self.__messages = messages
        self.__horaire = horaire
        self.__id_user = id_user
    
    def get_messages(self):
        return self.__messages
    
    def get_heure(self):
        return self.__horaire
    
    def get_id_user(self):
        return self.__id_user
    
    def set_messages(self, messages):
        self.__messages = messages
    
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
        try:
            # Requête SQL pour sélectionner les messages avec id_user 1 et 2, triés par ordre croissant d'horaire
            query = "SELECT * FROM messages WHERE (id_user = 1 OR id_user = 3) ORDER BY horaire ASC"
            
            # Exécution de la requête
            self.curseur.execute(query)
            
            # Récupération des résultats
            resultats = self.curseur.fetchall()
            
            # Affichage des résultats
            for row in resultats:
                messages = row[1]
                horaire = row[2]
                id_user = row[3]
                print(f" Messages: {messages}, {horaire}, ID utilisateur: {id_user}")
        
        except mysql.connector.Error as err:
            print("Erreur lors de l'exécution de la requête :", err)
        
        finally:
            # Fermeture du curseur et de la connexion
            self.curseur.close()
            self.connexion.close()

# Utilisation
selecteur = Select_message()
selecteur.afficher_messages()
