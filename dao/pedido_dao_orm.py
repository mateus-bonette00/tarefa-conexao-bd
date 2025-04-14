from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.models_orm import Base, Customers, Employees, Products, Orders, OrderDetails
from datetime import datetime

# Configuração da conexão com SQLAlchemy
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/northwind"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def inserir_pedido_orm(pedido):
    session = Session()

    try:
        # Buscar cliente
        cliente = session.query(Customers).filter(Customers.companyname == pedido.cliente_nome).first()
        if not cliente:
            raise Exception("Cliente não encontrado.")

        # Buscar funcionário
        funcionario = session.query(Employees).filter(
            (Employees.firstname + ' ' + Employees.lastname) == pedido.funcionario_nome
        ).first()
        if not funcionario:
            raise Exception("Funcionário não encontrado.")

        # Criar novo pedido
        novo_pedido = Orders(
            customerid=cliente.customerid,
            employeeid=funcionario.employeeid,
            orderdate=pedido.data_pedido
        )
        session.add(novo_pedido)
        session.flush()  # gera o orderid automaticamente

        # Adicionar os itens do pedido
        for nome_produto, quantidade, preco in pedido.itens:
            produto = session.query(Products).filter(Products.productname == nome_produto).first()
            if not produto:
                raise Exception(f"Produto '{nome_produto}' não encontrado.")

            item = OrderDetails(
                orderid=novo_pedido.orderid,
                productid=produto.productid,
                quantity=quantidade,
                unitprice=preco
            )
            session.add(item)

        session.commit()
        print(f"[ORM] Pedido inserido com sucesso! ID: {novo_pedido.orderid}")

    except Exception as e:
        session.rollback()
        print("Erro ao inserir com ORM:", e)
    finally:
        session.close()
