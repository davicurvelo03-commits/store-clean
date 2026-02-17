from db import db
from flask_login import UserMixin
class User(UserMixin, db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)

class produto(db.Model):
    __tablename__ = 'Produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Float, nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
    imagem = db.Column(db.String, nullable=True)