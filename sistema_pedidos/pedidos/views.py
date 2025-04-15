from django.shortcuts import render
from pedidos.controller.pedido_controller import criar_pedido_com_itens


def index(request):
    if request.method == 'POST':
        cliente = request.POST['cliente']
        funcionario = request.POST['funcionario']
        produto = request.POST['produto']
        quantidade = int(request.POST['quantidade'])
        preco = float(request.POST['preco'])

        itens = [(produto, quantidade, preco)]
        criar_pedido_com_itens(cliente, funcionario, itens)

        return render(request, 'confirmacao.html', {'cliente': cliente})
    
    return render(request, 'index.html')

from django.shortcuts import render
from pedidos.database.conexao import conectar

def relatorio_pedido(request):
    dados = None
    erro = None

    if request.method == 'POST':
        try:
            pedido_id = int(request.POST['pedido_id'])

            conn = conectar()
            cur = conn.cursor()

            # Cabeçalho do pedido
            cur.execute("""
                SELECT o.orderid, o.orderdate, c.companyname, e.firstname || ' ' || e.lastname
                FROM northwind.orders o
                JOIN northwind.customers c ON o.customerid = c.customerid
                JOIN northwind.employees e ON o.employeeid = e.employeeid
                WHERE o.orderid = %s
            """, (pedido_id,))
            cabecalho = cur.fetchone()

            if not cabecalho:
                erro = f"Pedido {pedido_id} não encontrado."
            else:
                # Itens do pedido
                cur.execute("""
                    SELECT p.productname, od.quantity, od.unitprice
                    FROM northwind.order_details od
                    JOIN northwind.products p ON od.productid = p.productid
                    WHERE od.orderid = %s
                """, (pedido_id,))
                itens = cur.fetchall()

                dados = {
                    'pedido_id': cabecalho[0],
                    'data': cabecalho[1],
                    'cliente': cabecalho[2],
                    'funcionario': cabecalho[3],
                    'itens': itens
                }

            cur.close()
            conn.close()

        except Exception as e:
            erro = f"Erro: {str(e)}"

    return render(request, 'relatorio.html', {'dados': dados, 'erro': erro})

from datetime import datetime

def ranking_funcionarios(request):
    dados = []
    erro = None

    if request.method == 'POST':
        try:
            data_inicio = request.POST['data_inicio']
            data_fim = request.POST['data_fim']

            conn = conectar()
            cur = conn.cursor()

            cur.execute("""
                SELECT e.firstname || ' ' || e.lastname AS nome,
                       COUNT(o.orderid) AS total_pedidos,
                       SUM(od.unitprice * od.quantity) AS total_vendido
                FROM northwind.orders o
                JOIN northwind.employees e ON o.employeeid = e.employeeid
                JOIN northwind.order_details od ON o.orderid = od.orderid
                WHERE o.orderdate BETWEEN %s AND %s
                GROUP BY nome
                ORDER BY total_vendido DESC
            """, (data_inicio, data_fim))

            dados = cur.fetchall()
            cur.close()
            conn.close()

        except Exception as e:
            erro = f"Erro: {str(e)}"

    return render(request, 'ranking.html', {
        'dados': dados,
        'erro': erro
    })
    
def home(request):
    return render(request, 'home.html')