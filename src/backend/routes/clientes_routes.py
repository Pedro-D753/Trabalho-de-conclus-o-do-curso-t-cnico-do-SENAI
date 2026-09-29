from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.backend.schemas.clientes_schemas import cliente_schema, clientes_schema
from src.backend.controllers import clientes_controllers
from src import api


class ClienteList(Resource):
    def get(self):
        """
        Lista todos os clientes
        ---

        tags:
        - Clientes
        responses:
          200:
            description: Lista de clientes da lanchonete
          404:
            description: Nenhum cliente encontrado
        """

        clientes = clientes_controllers.listar_usuario()

        if not clientes:
            return make_response(jsonify({"message": "Não existem usuários"}), 404)

        return make_response(jsonify(clientes_schema.dump(clientes)), 200)



    def post(self):
        """
        Cadastrar um novo cliente
        ---

        tags:
        -- Clientes
        parameters:
          - in: body
          name: body
          required: True
          schema:
            type: object
            properties:
              data_registro:
                type: datetime
                example: 21/08/2026
              tipo:
                type: string
                example: Lanchonete
        responses:
          201:
            description: Registro cadastrado
          400:
            description: Erro de validação
        """
        try:
            cliente = clientes_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400


        try:
            resultado = clientes_controllers.cadastrar_cliente(cliente)

            return clientes_schema.dump(resultado), 201

        except Exception as e:
            return {"message": str(e)}, 400


api.add_resource(ClienteList, "/clientes")


class ClienteResource(Resource):
    def get(self, id_cliente):
        """
        Buscar cliente por ID
        ---
        tags:
          - Clientes
        parameters:
        - name
        int: path
        type: integer
        required: True
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
            senha:
              type: string

        responses:


        """
        cliente = clientes_controllers.listar_cliente_por_id(id_cliente)

        if not cliente:
            return {"message": "Cliente não encontrado"}, 404
        

def put(self, id_cliente):
    """ Editar cliente."""
    try:
        novo_cliente = cliente_schema.load(request.get_json())
    except ValidationError as err:
        return {"errors": err.messages}, 400

    cliente = clientes_controllers.editar_cliente(
        id_cliente,
        {
            "nome": novo_cliente.nome,
            "cep": novo_cliente.cep,
            "contato": novo_cliente.contato,
            "senha": novo_cliente.senha,
        },
    )

    if cliente is None:
        return {"message": "Cliente não encontrado"}, 404

    return cliente_schema.dump(cliente), 200


def delete(self, id_cliente):
  
    """
    Deletar cliente
    ---
    tags:
      - Cliente
    parametes:
        name: id_cliente
        in: path
        type: integer
        required: True
    responses:
       200:
        description: Cliente deletado
       404:
       description: Cliente não encontrado

    """

    if clientes_controllers.deletar_cliente(id_cliente):
        return {"message": "Cliente deletado com sucesso"}, 404


api.add_resource(ClienteResource, "/cliente/<int:id_cliente>")

