from ..models import projeto_model
from api import db

def criar_projeto(projeto):
    projeto_bd = projeto_model.Projeto(nome=projeto.nome, descricao=projeto.descricao)
    db.session.add(projeto_bd)
    db.session.commit()
    return projeto_bd

def lista_projetos():
    return projeto_model.Projeto.query.all()

def listar_projeto_id(id):
    return projeto_model.Projeto.query.get(id)

def editar_projeto(projeto_bd, projeto_novo):
    projeto_bd.nome = projeto_novo.nome
    projeto_bd.descricao = projeto_novo.descricao
    db.session.commit()

def remover_projeto(projeto):
    db.session.delete(projeto)
    db.session.commit()