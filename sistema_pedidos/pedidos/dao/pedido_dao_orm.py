from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pedidos.model.models_orm import Base, Customers, Employees, Products, Orders, OrderDetails

from datetime import datetime
from pedidos.database.conexao import conectar

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTANTE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Atualize a senha do banco de dados

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/northwind"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def inserir_pedido_orm(pedido):
    try:
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()

        cliente = session.query(Customers).filter_by(companyname=pedido.cliente_nome).first()
        if not cliente:
            raise Exception("Cliente não encontrado (ORM)")

        funcionario = session.query(Employees).filter(
            (Employees.firstname + ' ' + Employees.lastname) == pedido.funcionario_nome
        ).first()
        if not funcionario:
            raise Exception("Funcionário não encontrado (ORM)")

        novo_pedido = Orders(
            customerid=cliente.customerid,
            employeeid=funcionario.employeeid,
            orderdate=pedido.data_pedido
        )
        session.add(novo_pedido)
        session.commit() 
        session.refresh(novo_pedido)  

        for nome_produto, quantidade, preco in pedido.itens:
            produto = session.query(Products).filter_by(productname=nome_produto).first()
            if not produto:
                raise Exception(f"Produto '{nome_produto}' não encontrado (ORM)")

            item = OrderDetails(
                orderid=novo_pedido.orderid,
                productid=produto.productid,
                quantity=quantidade,
                unitprice=preco
            )
            session.add(item)

        session.commit()

        print(f"[ORM] Pedido inserido com sucesso! ID: {novo_pedido.orderid}")
        return novo_pedido.orderid 

    except Exception as e:
        print("Erro (ORM):", e)
        session.rollback()
        return None 

    finally:
        session.close()
