from ..models import tarefa_model
from api import db

def criar_tarefa(tarefa):
    tarefa_bd = tarefa_model.Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao,
                                    data_expiracao=tarefa.data_expiracao, projeto=tarefa.projeto)
    db.session.add(tarefa_bd)
    db.session.commit()
    return tarefa_bd

def lista_tarefas():
    return tarefa_model.Tarefa.query.all()

def listar_tarefa_id(id):
    return tarefa_model.Tarefa.query.get(id)

def editar_tarefa(tarefa_bd, tarefa_nova):
    tarefa_bd.titulo = tarefa_nova.titulo
    tarefa_bd.descricao = tarefa_nova.descricao
    tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
    tarefa_bd.projeto = tarefa_nova.projeto
    db.session.commit()

def remover_tarefa(tarefa):
    db.session.delete(tarefa)
    db.session.commit()