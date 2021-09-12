from ..models import funcionario_model
from api import db

def criar_funcionario(funcionario):
    funcionario_bd = funcionario_model.Funcionario(nome=funcionario.nome, idade=funcionario.idade)
    db.session.add(funcionario_bd)
    db.session.commit()
    return funcionario_bd

def lista_funcionarios():
    return funcionario_model.Funcionario.query.all()

def listar_funcionario_id(id):
    return funcionario_model.Funcionario.query.get(id)

def editar_funcionario(funcionario_bd, funcionario_novo):
    funcionario_bd.nome = funcionario_novo.nome
    funcionario_bd.idade = funcionario_novo.idade
    db.session.commit()

def remover_funcionario(funcionario):
    db.session.delete(funcionario)
    db.session.commit()