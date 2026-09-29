from src import ma
from src.backend.models import clientes_models
from marshmallow import fields

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = clientes_models.ClienteModel
        load_instance = True
        fields = ('id', 'nome', 'contato', 'cep', 'senha')


    nome = fields.String(required=True)
    contato = fields.String(required=True)
    cep = fields.Integer(required=True)
    senha = fields.String(required=True)

cliente_schema = ClienteSchema()
clientes_schema = ClienteSchema(many=True)