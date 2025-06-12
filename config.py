import os

# Pega o caminho absoluto do diretório do arquivo config.py
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6fw4ZSYpCdytQwbzVlYHO0at8Sq4Ae0whcldWzjad83Dptmr'
    # --- CONFIGURAÇÃO DO BANCO DE DADOS ---
    # Por enquanto, usaremos um banco de dados SQLite para facilitar o desenvolvimento local.
    # Quando formos para produção no Hostinger, trocaremos esta linha.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # Desativa um recurso do Flask-SQLAlchemy que não usaremos e que emite avisos.
    SQLALCHEMY_TRACK_MODIFICATIONS = False