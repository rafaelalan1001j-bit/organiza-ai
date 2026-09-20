# ⚡ Organiza AI

Aplicação Web para gerenciamento e organização de tarefas cotidianas e acadêmicas, desenvolvida com Python e Django no âmbito da disciplina de Desenvolvimento Web na **Universidade Federal Rural da Amazônia (UFRA)** - Campus Capitão Poço.

---

## 👥 Equipe do Projeto
* **Rafael Alan Ramos de Farias**
* **Jhony Moreira Silva**
* **Herbert Luan Martins Meireles**
* **João Paulo Correia de Oliveira**

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.12+
* **Framework Web:** Django
* **Front-end:** HTML5, CSS3, Bootstrap 5.0.2
* **Arquivos Estáticos:** dj-static e Cling (WSGI)
* **Banco de Dados:** SQLite (nativo do Django)

---

## 📁 Estrutura do Projeto
`
organiza-ai/
├── manage.py
├── db.sqlite3
├── README.md
├── organiza_ai/        # Configurações gerais do projeto (settings, urls, wsgi, asgi)
├── tarefa/             # Módulo da aplicação (models, views, migrations, Templates)
│   └── Templates/
│       └── tarefa/
│           ├── menu.html           # Tela inicial e layout base com sidebar
│           └── lista_tarefas.html  # Tela de visualização das tarefas
├── static/             # Arquivos estáticos de desenvolvimento (CSS)
└── staticfiles/        # Arquivos estáticos coletados para produção
`

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório
`ash
git clone https://github.com/OrganizaAI/organiza-ai.git
cd organiza-ai
`

### 2. Criar e ativar o ambiente virtual (venv)
* **Windows (PowerShell):**
`powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
`
* **Linux/macOS:**
`ash
python3 -m venv venv
source venv/bin/activate
`

### 3. Instalar as dependências
`ash
pip install django dj-static
`

### 4. Aplicar as migrações do banco de dados
`ash
python manage.py migrate
`

### 5. Coletar os arquivos estáticos
`ash
python manage.py collectstatic --noinput
`

### 6. Executar o servidor de desenvolvimento
`ash
python manage.py runserver
`

Acesse a aplicação no navegador em: 👉 **http://127.0.0.1:8000/**

---

## 🌐 Rotas Principais
* / ou /menu/ : Tela inicial do Organiza AI com menu lateral de navegação.
* /lista_tarefas/ : Tabela com as tarefas cadastradas no sistema.
* /admin/ : Painel administrativo do Django para controle geral de dados.
