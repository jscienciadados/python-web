from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Joao Souza'}
    posts = [
        {'author': {'username': 'Luisa'}, 'body': 'olá da Luisa'},
        {'author': {'username': 'Joao Souza'}, 'body': 'olá do Joao'}

    ]
    return render_template("index.html", user=user, posts=posts)

