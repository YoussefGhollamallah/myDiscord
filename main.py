from flask import Flask, redirect, render_template, request, session, url_for
from classe import *  # Assurez-vous d'importer correctement votre classe User
from hashlib import sha512
from flask_socketio import SocketIO, emit

def hash_password(password):
    return sha512(password.encode()).hexdigest()


users = Users(db)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.secret_key = 'valeur_secrete'


@app.route("/")
def bonjour():
    return render_template("index.html")


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
        prenom = donnees.get("prénom") 
        nom = donnees.get("nom") 
        email = donnees.get("email")  
        password = donnees.get("password")
        users.inscription(nom, prenom, email, password)
        message = "Inscription réussie"
        return render_template("traitement.html", message)
    else:
        message = "Erreur lors de l'inscription"
        return render_template("inscription.html", message=message)
 
@app.route("/traitementtest", methods=["POST"])
def traitementtest():
    if request.method == "POST":
        donnees = request.form
        email = donnees.get("email")
        password = donnees.get("password")
        user_result = users.connexion(email, password)

        if user_result:
            session['user'] = user_result
            return render_template("accueil.html", user=users.get_user(email))
        else:
            message = "Erreur lors de la connexion"
            return render_template("connexion.html", message=message)
        
@app.route("/test")
def index():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('chat'))  
    return render_template('connect.html')

@app.route('/chat', methods=['GET', "POST"])
def chat():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return redirect(url_for('connect'))

@socketio.on('message')
def handle_message(msg):
    emit('message',{"username":session['username'], "message":msg}, broadcast=True)

@app.route('/myprofil')
def myprofil():
    if 'user' in session:
        user_result = session['user']
        user_details = {k: v for k, v in user_result.items() if k != 'password'}
        return render_template('profil.html', user=user_details)
    else:
        return redirect(url_for('connexion'))   

if __name__ == "__main__":
    socketio.run(app, debug=True)
