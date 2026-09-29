from src.backend.models.clientes_models import ClienteModel
from connection import db

def cadastrar_cliente(cliente):
    cliente_db = ClienteModel(nome=cliente.nome, cep=cliente.cep, contato=cliente.contato )
    cliente_db.gen_senha(cliente.senha)
    db.session.add(cliente_db)
    db.session.commit()
    return cliente_db

    
def listar_cliente():
    return ClienteModel.query.all()


def listar_cliente_por_id(id):
    cliente_encontrado = ClienteModel.query.get(id)
    return cliente_encontrado

    
def deletar_cliente():
    cliente = ClienteModel.query.get(id)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        return True
    return False
    
    
def editar_cliente(id, novo_cliente):
    cliente = ClienteModel.query.get(id)
    if cliente:
        cliente.nome = novo_cliente['nome']
        cliente.cep = novo_cliente['cep']
        cliente.contato = novo_cliente['contato']
        if novo_cliente.get('senha'):
            cliente.gen_senha(novo_cliente['senha'])

        db.session.commit()
        return cliente
    return None
    
    
