import mysql.connector
from datetime import datetime

class Show_message:
    def __init__(self, messages, horaire, id_user, prenom,  nom):
        self.__messages = messages
        self.__horaire = horaire
        self.__id_user = id_user
        self.__prenom = prenom
        self.__nom = nom
    
    def get_messages(self):
        return self.__messages
    
    def get_heure(self):
        return self.__horaire
    
    def get_id_user(self):
        return self.__id_user
    
    def get_prenom(self):
        return self.__prenom
    
    def get_nom(self):
        return self.__nom
    
    def set_messages(self, messages):
        self.__messages = messages
    
    def set_heure(self,horaire):
        self.__horaire = horaire
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def set_nom(self, nom):
        self.__nom = nom

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
            query = """
                SELECT m.message, m.horaire, m.id_user, u.nom, u.prenom
                FROM messages m
                INNER JOIN users u ON m.id_user = u.id
                WHERE m.id_user = 3 OR m.id_user = 1
                ORDER BY m.horaire ASC
            """
            
            # Exécution de la requête
            self.curseur.execute(query)
            
            # Récupération des résultats
            resultats = self.curseur.fetchall()

            
            # Affichage des résultats
            for row in resultats:
                message = row[0]
                horaire = row[1]
                id_user = row[2]
                nom = row[3]
                prenom = row[4]
                
                print(f"{nom} {prenom} : {message}")
                print(f"{horaire}, ID_user: {id_user}")
        
        except mysql.connector.Error as err:
            print("Erreur lors de l'exécution de la requête :", err)
        
        finally:
            # Fermeture du curseur et de la connexion
            self.curseur.close()
            self.connexion.close()

# Utilisation
selecteur = Select_message()
selecteur.afficher_messages()
