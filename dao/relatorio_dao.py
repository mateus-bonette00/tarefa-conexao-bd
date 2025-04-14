from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.models_orm import Orders, Customers, Employees, OrderDetails, Products

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/northwind"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def buscar_detalhes_pedido(order_id):
    session = Session()

    try:
        pedido = session.query(Orders).filter(Orders.orderid == order_id).first()
        if not pedido:
            print("Pedido não encontrado.")
            return

        cliente = session.query(Customers).filter(Customers.customerid == pedido.customerid).first()
        funcionario = session.query(Employees).filter(Employees.employeeid == pedido.employeeid).first()
        itens = session.query(OrderDetails).filter(OrderDetails.orderid == order_id).all()

        print(f"\n📦 Pedido #{pedido.orderid}")
        print(f"Data do pedido: {pedido.orderdate}")
        print(f"Cliente: {cliente.companyname}")
        print(f"Funcionário: {funcionario.firstname} {funcionario.lastname}")
        print("\nItens do pedido:")
        print("-" * 50)
        for item in itens:
            produto = session.query(Products).filter(Products.productid == item.productid).first()
            print(f"Produto: {produto.productname} | Quantidade: {item.quantity} | Preço unitário: {item.unitprice}")

    except Exception as e:
        print("Erro ao buscar relatório:", e)
    finally:
        session.close()

from sqlalchemy import func
from datetime import datetime

def ranking_funcionarios_por_periodo(data_inicio, data_fim):
    session = Session()

    try:
        # Subconsulta: total vendido por pedido
        resultados = (
            session.query(
                Employees.firstname,
                Employees.lastname,
                func.count(Orders.orderid).label("total_pedidos"),
                func.sum(OrderDetails.unitprice * OrderDetails.quantity).label("total_vendido")
            )
            .join(Orders, Employees.employeeid == Orders.employeeid)
            .join(OrderDetails, Orders.orderid == OrderDetails.orderid)
            .filter(Orders.orderdate >= data_inicio)
            .filter(Orders.orderdate <= data_fim)
            .group_by(Employees.employeeid)
            .order_by(func.sum(OrderDetails.unitprice * OrderDetails.quantity).desc())
            .all()
        )

        print(f"\n📊 Ranking de Funcionários entre {data_inicio} e {data_fim}")
        print("-" * 60)
        for nome, sobrenome, total_pedidos, total_vendido in resultados:
            print(f"{nome} {sobrenome} | Pedidos: {total_pedidos} | Total vendido: ${total_vendido:.2f}")

    except Exception as e:
        print("Erro ao gerar ranking:", e)
    finally:
        session.close()