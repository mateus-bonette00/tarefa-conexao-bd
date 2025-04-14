# Tarefa Prática – Conexão com Banco de Dados

Disciplina: Banco de Dados II  
Professora: Vanessa Souza
Integrantes: 
- Mateus de Freitas Bonette - 2020001519
- Gustavo Kiyoshi Souza Noda - 2020

## Objetivo

Implementar uma aplicação Python com inserção de pedidos no banco de dados Northwind usando:

- Driver `psycopg2`
- Simulação de SQL Injection
- ORM com `SQLAlchemy`
- Relatórios:
  - Detalhes completos de um pedido
  - Ranking de funcionários por período

## Padrões utilizados
- MVC (Model-View-Controller)
- DAO (Data Access Object)

## Tecnologias

- Python 3.x
- PostgreSQL
- psycopg2
- SQLAlchemy
- SQLACodeGen

## Como rodar

```bash
pip install -r requirements.txt
python -m view.main
