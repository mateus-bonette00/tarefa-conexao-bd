# Tarefa Prática – Conexão com Banco de Dados

**Disciplina:** Banco de Dados II  
**Professora:** Vanessa Cristina Oliveira de Souza  

**Dupla:**  
- Mateus de Freitas Bonette - 2020001519  
- Gustavo Kiyoshi Souza Noda - 2020000718  

---

## Objetivo

Implementar uma aplicação Python com interface web em Django para inserção de pedidos no banco de dados Northwind, utilizando diferentes abordagens de acesso ao banco de dados e segurança:

- Inserção de pedidos com cliente, funcionário e produtos
- Relatórios de pedidos e ranking de funcionários
- Simulação de SQL Injection
- ORM com SQLAlchemy

---

## Funcionalidades

- **Modo Seguro (psycopg2 com parâmetros seguros)**
- **Modo Inseguro (simulação de SQL Injection)**
- **Modo ORM (SQLAlchemy)**
- **Relatório detalhado de pedido**
- **Ranking de funcionários por período**
- **Interface web com Django + HTML/CSS (sem Bootstrap)**


---

## Padrões Utilizados

- MVC (Model-View-Controller)
- DAO (Data Access Object)

---

## Tecnologias

- Python 3.x
- Django 5.2
- PostgreSQL
- psycopg2
- SQLAlchemy
- SQLACodeGen

---

## Links

- [Repositório GitHub](https://github.com/mateus-bonette00/tarefa-conexao-bd)
- [Vídeo explicativo (YouTube)]()

---

## Como rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Acessar a pasta do projeto Django
cd sistema_pedidos

# Rodar o servidor local
python manage.py runserver
