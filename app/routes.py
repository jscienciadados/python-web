from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joao Souza'}
    posts = [
        {'author': {'username': 'Luisa'}, 'body': 'olá da Luisa'},
        {'author': {'username': 'Joao Souza'}, 'body': 'olá do Joao'}

    ]
    return render_template("index.html", user=user, posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.values.get("user"), request.values.get("pass"))
    return render_template("login.html", title="Login")    

