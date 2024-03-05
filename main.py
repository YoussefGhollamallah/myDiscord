from flask import Flask, redirect, render_template, request, session, url_for
from classe import *  # Assurez-vous d'importer correctement votre classe User


app = Flask(__name__)
app.secret_key = 'valeur_secrete'  


@app.route("/")
def bonjour():
    return render_template("index.html")

@app.route("/connexion")
def connexion():
    return render_template("connexion.html")

@app.route("/inscription")
def inscription():
    return render_template("inscription.html")

@app.route("/profil")
def profil():
    return render_template("profil.html")

@app.route("/accueil")
def accueil():
    return render_template("accueil.html")

@app.route("/traitement", methods=["POST"])
def traitement():
    if request.method == "POST":
        donnees = request.form
        prenom = donnees["prenom"]  # Assurez-vous de récupérer le prénom correctement
        nom = donnees["nom"]
        email = donnees["email"]
        password = donnees["password"]

        user.inscription(nom, prenom, email, password, visibility=0)
        message = "Inscription réussie"
        return render_template("traitement.html", message=message)
    else:
        message = "Erreur lors de l'inscription"
        return render_template("inscription.html", message=message)
 
@app.route("/traitement_connexion", methods=["POST"])
def traitement_connexion():
    if request.method == "POST":
        donnees = request.form
        email = donnees["email"]
        password = donnees["password"]
        user_result = user.connexion(email, password)
        if user_result is not None:
            message = "Connexion réussie"
            session['user'] = user_result
            return render_template("accueil.html", user=user, message=message)
        else:
            message = "Erreur lors de la connexion"
            return render_template("connexion.html", message=message)

@app.route('/myprofil')
def myprofil():
    if 'user' in session:
        user_result = session['user']
        user_details = {k: v for k, v in user_result.items() if k != 'password'}
        return render_template('profil.html', user=user_details)
    else:
        return redirect(url_for('connexion'))   

if __name__ == "__main__":
    app.run(debug=True)
