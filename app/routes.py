from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Olá, SisPirita! Nosso projeto está no ar!"