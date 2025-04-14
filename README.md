# Tarefa Prática – Conexão com Banco de Dados

Disciplina: Banco de Dados II  
Professora: Vanessa Cristina Oliveira de Souza  
Integrantes: 
- Mateus de Freitas Bonette - 2020001519
- Gustavo Kiyoshi Souza Noda - 2020000718

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

## Funcionalidades

- Inserção de pedidos com cliente, funcionário e produtos
- Relatório completo de um pedido específico
- Ranking de funcionários com base no total vendido
- Modo inseguro com SQL Injection para fins educacionais
- Modo com ORM usando SQLAlchemy

## Links

- [Repositório GitHub](https://github.com/mateus-bonette00/tarefa-conexao-bd)
- [Vídeo explicativo (YouTube)](https://youtu.be/SEU-LINK)

## Como rodar

```bash
pip install -r requirements.txt
python -m view.main
