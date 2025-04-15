from pedidos.database.conexao import conectar


def inserir_pedido_inseguro(pedido):
    try:
        conn = conectar()
        cur = conn.cursor()

        # ⚠️ Query INSEGURA com f-string (vulnerável a SQL Injection)
        query_cliente = f"SELECT customerid FROM northwind.customers WHERE companyname = '{pedido.cliente_nome}'"
        cur.execute(query_cliente)
        cliente = cur.fetchone()
        if not cliente:
            raise Exception("Cliente não encontrado.")
        cliente_id = cliente[0]

        query_func = f"""
            SELECT employeeid FROM northwind.employees 
            WHERE CONCAT(firstname, ' ', lastname) = '{pedido.funcionario_nome}'
        """
        cur.execute(query_func)
        funcionario = cur.fetchone()
        if not funcionario:
            raise Exception("Funcionário não encontrado.")
        funcionario_id = funcionario[0]

        query_pedido = f"""
            INSERT INTO northwind.orders (customerid, employeeid, orderdate)
            VALUES ('{cliente_id}', '{funcionario_id}', '{pedido.data_pedido}') RETURNING orderid
        """
        cur.execute(query_pedido)
        order_id = cur.fetchone()[0]

        for produto_nome, quantidade, preco in pedido.itens:
            query_prod = f"SELECT productid FROM northwind.products WHERE productname = '{produto_nome}'"
            cur.execute(query_prod)
            produto = cur.fetchone()
            if not produto:
                raise Exception(f"Produto '{produto_nome}' não encontrado.")
            produto_id = produto[0]

            query_item = f"""
                INSERT INTO northwind.order_details (orderid, productid, quantity, unitprice)
                VALUES ({order_id}, {produto_id}, {quantidade}, {preco})
            """
            cur.execute(query_item)

        conn.commit()
        print(f"[INSEGURO] Pedido inserido com sucesso! ID: {order_id}")
        return order_id

    except Exception as e:
        print("Erro ao inserir pedido (modo inseguro):", e)
        conn.rollback()
        return None
    
    finally:
        cur.close()
        conn.close()
