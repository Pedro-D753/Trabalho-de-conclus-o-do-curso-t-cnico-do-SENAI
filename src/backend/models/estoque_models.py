from connection import db
from passlib import CryptContext
from sqlalchemy import Column, Integer, String

class IgredienteModel(db.Model):
    __tablename__ = 'estoque'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    nome_ingrediente = db.Column(String(100), nullable=False)
    uni_medida = db.Column(String(100), nullable=False, unique=True)
    quant_estoque = db.Column(String(100), nullable=False)

    