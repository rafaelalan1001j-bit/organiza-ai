# OrganizaAI — Gerenciador de Tarefas em Django (NAP 2)

> **Segunda Entrega de Desenvolvimento Web (WEB26SMG)**  
> **Universidade Federal Rural da Amazônia (UFRA)**  
> **Docente:** Prof. Roberto Franco  
> **Prazo:** 25/09/2026 até as 22:00

---

## 📌 Visão Geral

O **OrganizaAI** é uma aplicação Web desenvolvida em **Python** e **Django 5** para gerenciamento simples de tarefas. O sistema implementa o **CRUD completo diretamente na interface do sistema** para **Tarefas** e **Categorias**, com layout responsivo em **Bootstrap 5.3** e banco de dados **SQLite**.

---

## 🚀 Funcionalidades

### 1. CRUD de Tarefas
- **Cadastrar Tarefa (`/`):** Formulário direto no topo da tela inicial com título, descrição, categoria, prioridade (Baixa, Média, Alta) e prazo.
- **Listar Tarefas (`/`):** Tabela limpa com filtros por status (*Todas, Pendentes, Concluídas*), filtro por categoria e busca por título.
- **Editar Tarefa (`/tarefa/<id>/editar/`):** Tela para atualizar os dados de uma tarefa existente.
- **Excluir Tarefa (`/tarefa/<id>/excluir/`):** Botão de exclusão com confirmação.
- **Concluir Tarefa (`/tarefa/<id>/concluir/`):** Botão direto para marcar como concluída ou reabrir.

### 2. CRUD de Categorias
- **Listar e Cadastrar Categorias (`/categorias/`):** Tela simples para cadastrar novas categorias e listar as existentes com o total de tarefas vinculadas.
- **Excluir Categoria (`/categorias/<id>/excluir/`):** Botão para remover categorias com tratamento relacional seguro.

---

## 🛠️ Tecnologias

- **Python 3.11**
- **Django 5.2.17** (Padrão MTV: Models, Templates, Views)
- **Bootstrap 5.3** & Bootstrap Icons
- **SQLite3**

---

## 💻 Como Rodar o Projeto

```bash
# 1. Ativar o ambiente virtual
.\organizaai-main\ai\Scripts\Activate.ps1

# 2. Entrar na pasta do projeto
cd organizaai-main/organizaai

# 3. Rodar as migrações do banco
python manage.py migrate

# 4. Executar os testes automatizados
python manage.py test

# 5. Iniciar o servidor
python manage.py runserver
```

Acesse no navegador:
👉 **http://127.0.0.1:8000/**

Admin do Django:
👉 **http://127.0.0.1:8000/admin/**

---

## 📄 Relatório em PDF

O relatório técnico exigido para a entrega do NAP2 está gerado e disponível na raiz:
- **`Relatorio_NAP2_OrganizaAI.pdf`**

---

## 📬 Dados para Envio

- **Para:** `roberto.franco@ufra.edu.br`
- **Assunto:** `WEB26SMG – OrganizaAI`
- **Anexo:** `Relatorio_NAP2_OrganizaAI.pdf`
