from api import api
from flask import json, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import funcionario_schema
from ..entidades import funcionario
from ..services import funcionario_service


class FuncionarioList(Resource):
    def get(self):
        funcionarios = funcionario_service.lista_funcionarios()
        fs = funcionario_schema.FuncionarioSchema(many=True)
        return make_response(fs.jsonify(funcionarios), 200)

    def post(self):
        fs = funcionario_schema.FuncionarioSchema()
        validate = fs.validate(request.json)

        # Caso retorne algo no validate, ocorreu algo na validacao dos dados
        if validate:
            return make_response(jsonify(validate), 400) # retorna os erros de validacao
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]
            novo_funcionario = funcionario.Funcionario(nome, idade)
            result = funcionario_service.criar_funcionario(novo_funcionario)
            return make_response(fs.jsonify(result), 201)


class FuncionarioDetail(Resource):
    def get(self, id):
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("Funcionário não encontrado"), 404)
        fs = funcionario_schema.FuncionarioSchema()
        return make_response(fs.jsonify(funcionario), 200)

    def put(self, id):
        funcionario_bd = funcionario_service.listar_funcionario_id(id)
        if funcionario_bd is None:
            return make_response(jsonify("Funcionario não encontrada"), 404)
        fs = funcionario_schema.FuncionarioSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]
            novo_funcionario = funcionario.Funcionario(nome, idade)
            funcionario_service.editar_funcionario(funcionario_bd, novo_funcionario)
            funcionario_atualizada = funcionario_service.listar_funcionario_id(id)
            return make_response(fs.jsonify(funcionario_atualizada), 200)

    def delete(self, id):
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("Funcionario não encontrada"), 404)
        else:
            funcionario_service.remover_funcionario(funcionario)
            return make_response('', 204)

api.add_resource(FuncionarioList, '/funcionarios')
api.add_resource(FuncionarioDetail, '/funcionarios/<int:id>')