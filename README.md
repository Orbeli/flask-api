# Projeto de Estudos com Flask, Swagger e Docker
Projeto criado com o objetivo de criar uma API RESTful em Flask, implementando Swagger e outros recursos que auxiliem o desenvolvimento e facilidade de consumo da API.

---
## Requisitos
1) Python 3.6.x ou superior
2) PostgreSQL 13.0 ou superior

---
A instalação deve ser feita manualmente, para isso:
1) Criar a *.venv*: 
```
    python3 -m venv .venv
```
2) Instalar as dependências do projeto através do *requirements.txt*:
```
    .venv/bin/pip install -r requirements.txt
```
3) Setar a variável de ambiente *FLASK_APP*:
```
    export FLASK_APP="api.py"
```
4) Rodar as migrations do projeto:
```
    .venv/bin/flask db upgrade
```

---
## Start
Para startar o projeto:
1) Setar a variável de ambiente *FLASK_APP*:
```
    export FLASK_APP="api.py"
```
2) Rodar o comando:
```
    .venv/bin/flask run
```

---
## Exemplos de Uso
Exemplos de uso com cURL:
1) Retornar todas as tarefas:
```
    curl -X GET "http://localhost:5000/tarefas" -H "accept: application/json"
```
2) Retornar a tarefa de id 1:
```
    curl -X GET "http://localhost:5000/tarefas/1" -H "accept: application/json"
```
3) Remover uma tarefa:
```
    curl -X DELETE "http://localhost:5000/tarefas/1" -H "accept: application/json"
```

---
## Metas do Projeto
Metas que serão realizadas ao longo do desenvolvimento do projeto:
- [] Desenvolver todos os endpoints da API (CRUD tarefas, projetos e funcionários)
- [x] Implementar sistema de versionamento do Banco de Dados
- [] Implementar [Swagger](https://swagger.io/)
- [] Implementar [Docker](https://www.docker.com/)
- [] Implementar Testes automatizados
- [] Configurar [Nginx](https://www.nginx.com/) para o projeto
- [] Parametrizar o projeto para ambientes de desenvolvimento e produção
 
---
## Links
[GitHub](https://github.com/Orbeli/flask-api) - GitHub do projeto  

---
## Author
Gabriel Orbeli Rodrigues Belíssimo

[E-mail](mailto:gabriel.orbeli@gmail.com)
[GitHub](https://github.com/Orbeli)
[Linkedin](https://www.linkedin.com/in/gabriel-orbeli-436815171/)
