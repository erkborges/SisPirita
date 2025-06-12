# app/models.py
from app import db
from datetime import datetime

class Usuario(db.Model):
    # __tablename__ = 'usuarios' # Opcional: define um nome explícito para a tabela
    
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    senha_hash = db.Column(db.String(256)) # Aumentado para 256 para hashes modernos
    telefone = db.Column(db.String(20), nullable=True)
    data_cadastro = db.Column(db.DateTime, index=True, default=datetime.now)
    ativo = db.Column(db.Boolean, default=True)
    
    # Futuramente adicionaremos o campo 'funcao' e os relacionamentos.

    def __repr__(self):
        # O método __repr__ define como o objeto será exibido para debug.
        return f'<Usuário {self.nome_completo} ({self.email})>'