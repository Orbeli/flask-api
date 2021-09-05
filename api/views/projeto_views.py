from api import api
from flask import json, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import projeto_schema
from ..entidades import projeto
from ..services import projeto_service


class ProjetoList(Resource):
    def get(self):
        projetos = projeto_service.lista_projetos()
        ps = projeto_schema.ProjetoSchema(many=True)
        return make_response(ps.jsonify(projetos), 200)

    def post(self):
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json)

        # Caso retorne algo no validate, ocorreu algo na validacao dos dados
        if validate:
            return make_response(jsonify(validate), 400) # retorna os erros de validacao
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            novo_projeto = projeto.Projeto(nome, descricao)
            result = projeto_service.criar_projeto(novo_projeto)
            return make_response(ps.jsonify(result), 201)


class ProjetoDetail(Resource):
    def get(self, id):
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("Projeto não encontrada"), 404)
        ps = projeto_schema.ProjetoSchema()
        return make_response(ps.jsonify(projeto), 200)

    def put(self, id):
        projeto_bd = projeto_service.listar_projeto_id(id)
        if projeto_bd is None:
            return make_response(jsonify("Projeto não encontrada"), 404)
        ps = projeto_schema.ProjetoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            novo_projeto = projeto.Projeto(nome, descricao)
            projeto_service.editar_projeto(projeto_bd, novo_projeto)
            projeto_atualizada = projeto_service.listar_projeto_id(id)
            return make_response(ps.jsonify(projeto_atualizada), 200)

    def delete(self, id):
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("Projeto não encontrada"), 404)
        else:
            projeto_service.remover_projeto(projeto)
            return make_response('', 204)

api.add_resource(ProjetoList, '/projetos')
api.add_resource(ProjetoDetail, '/projetos/<int:id>')