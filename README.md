# Organiza AI

Projeto da disciplina de Desenvolvimento Web - UFRA (Campus Sao Miguel do Guama).
Sistema para gerenciamento e organizacao de tarefas.

## Integrantes
- Rafael Alan Ramos de Farias
- Jhony Moreira Silva
- Herbert Luan Martins Meireles
- Joao Paulo Correia de Oliveira

## Tecnologias
- Python
- Django
- HTML e CSS
- Bootstrap 5
- SQLite
- dj-static

## Como rodar o projeto

1. Criar e ativar o ambiente virtual:
`ash
python -m venv venv
.\venv\Scripts\Activate.ps1
`

2. Instalar os pacotes necessarios:
`ash
pip install django dj-static
`

3. Rodar as migracoes do banco:
`ash
python manage.py migrate
`

4. Coletar os arquivos estaticos:
`ash
python manage.py collectstatic --noinput
`

5. Iniciar o servidor:
`ash
python manage.py runserver
`

Acesse no navegador: http://127.0.0.1:8000/

## Rotas
- / ou /menu/ : Tela inicial com o menu lateral
- /lista_tarefas/ : Tabela com a lista de tarefas
- /admin/ : Painel administrativo do Django
