from database.conexao import conectar

def inserir_pedido(pedido):
    try:
        conn = conectar()
        cur = conn.cursor()

        # Pegar IDs reais no banco
        cur.execute("SELECT customerid FROM northwind.customers WHERE companyname = %s", (pedido.cliente_nome,))
        cliente = cur.fetchone()
        if not cliente:
            raise Exception("Cliente não encontrado.")
        cliente_id = cliente[0]

        cur.execute("""
            SELECT employeeid 
            FROM northwind.employees 
            WHERE CONCAT(firstname, ' ', lastname) = %s
        """, (pedido.funcionario_nome,))
        funcionario = cur.fetchone()
        if not funcionario:
            raise Exception("Funcionário não encontrado.")
        funcionario_id = funcionario[0]

        # Inserir pedido
        cur.execute("""
            INSERT INTO northwind.orders (customerid, employeeid, orderdate)
            VALUES (%s, %s, %s) RETURNING orderid
        """, (cliente_id, funcionario_id, pedido.data_pedido))
        order_id = cur.fetchone()[0]

        # Inserir itens
        for produto_nome, quantidade, preco in pedido.itens:
            cur.execute("SELECT productid FROM northwind.products WHERE productname = %s", (produto_nome,))
            produto = cur.fetchone()
            if not produto:
                raise Exception(f"Produto '{produto_nome}' não encontrado.")
            produto_id = produto[0]

            cur.execute("""
                INSERT INTO northwind.order_details (orderid, productid, quantity, unitprice)
                VALUES (%s, %s, %s, %s)
            """, (order_id, produto_id, quantidade, preco))

        conn.commit()
        print(f"Pedido inserido com sucesso! ID: {order_id}")

    except Exception as e:
        print("Erro ao inserir pedido:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()
