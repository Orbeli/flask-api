from api import api
from flask import json, request, make_response, jsonify
from flask_restful import Resource
from ..schemas import tarefa_schema
from ..entidades import tarefa
from ..services import tarefa_service, projeto_service


class TarefaList(Resource):
    def get(self):
        tarefas = tarefa_service.lista_tarefas()
        ts = tarefa_schema.TarefaSchema(many=True)
        return make_response(ts.jsonify(tarefas), 200)

    def post(self):
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)

        # Caso retorne algo no validate, ocorreu algo na validacao dos dados
        if validate:
            return make_response(jsonify(validate), 400) # retorna os erros de validacao
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]
            projeto = request.json["projeto"]
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)
            if projeto_tarefa is None:
                return make_response(jsonify("Projeto não encontrado"), 404)
            nova_tarefa = tarefa.Tarefa(titulo, descricao, data_expiracao, projeto_tarefa)
            result = tarefa_service.criar_tarefa(nova_tarefa)
            return make_response(ts.jsonify(result), 201)


class TarefaDetail(Resource):
    def get(self, id):
        tarefa = tarefa_service.listar_tarefa_id(id)
        if tarefa is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)
        ts = tarefa_schema.TarefaSchema()
        return make_response(ts.jsonify(tarefa), 200)

    def put(self, id):
        tarefa_bd = tarefa_service.listar_tarefa_id(id)
        if tarefa_bd is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json["titulo"]
            descricao = request.json["descricao"]
            data_expiracao = request.json["data_expiracao"]
            projeto = request.json["projeto"]
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)
            if projeto_tarefa is None:
                return make_response(jsonify("Projeto não encontrado"), 404)
            nova_tarefa = tarefa.Tarefa(titulo, descricao, data_expiracao, projeto_tarefa)
            tarefa_service.editar_tarefa(tarefa_bd, nova_tarefa)
            tarefa_atualizada = tarefa_service.listar_tarefa_id(id)
            return make_response(ts.jsonify(tarefa_atualizada), 200)

    def delete(self, id):
        tarefa = tarefa_service.listar_tarefa_id(id)
        if tarefa is None:
            return make_response(jsonify("Tarefa não encontrada"), 404)
        else:
            tarefa_service.remover_tarefa(tarefa)
            return make_response('', 204)

api.add_resource(TarefaList, '/tarefas')
api.add_resource(TarefaDetail, '/tarefas/<int:id>')