from flask import Flask, render_template, request
from classe import *


app = Flask(__name__)

@app.route("/")
def bonjour():
    return render_template("index.html")

@app.route("/connexion")
def connexion():
    if request.method == "GET":
        email = request.form["email"]
        password = request.form["password"]
        user.connexion(email, password)
        return render_template("acceuil.html")
    return render_template("connexion.html")

@app.route("/inscription")
def inscription():
    return render_template("inscription.html")


@app.route("/traitement")
def traitement():
    return "traitement réussi !"


if __name__ == "__main__":
    app.run(debug=True)
