__version__ = "0.1.0"

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

# Cria as instâncias das extensões
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importa os módulos de rotas e modelos no final
# para evitar problemas de importação circular.
from app import routes, models