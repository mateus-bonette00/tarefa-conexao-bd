from controller.pedido_controller import criar_pedido_com_itens

print("== SISTEMA DE PEDIDOS ==")
print("1 - Inserir pedido")
print("2 - Relatório detalhado de pedido")
print("3 - Ranking de funcionários")


op = input("Escolha a opção (1, 2 ou 3): ")

if op == '1':
    modo = input("Modo: seguro (s), inseguro (i) ou ORM (o)? ").lower()
    
    cliente = input("Nome do cliente: ")
    funcionario = input("Nome do funcionário: ")

    itens = []
    while True:
        produto = input("Produto (ou 'fim'): ")
        if produto.lower() == 'fim':
            break
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço unitário: "))
        itens.append((produto, quantidade, preco))

    if modo == 's':
        from controller.pedido_controller import criar_pedido_com_itens
        criar_pedido_com_itens(cliente, funcionario, itens)
    elif modo == 'i':
        from controller.pedido_controller import criar_pedido_inseguro
        criar_pedido_inseguro(cliente, funcionario, itens)
    elif modo == 'o':
        from controller.pedido_controller import criar_pedido_orm
        criar_pedido_orm(cliente, funcionario, itens)

elif op == '2':
    from view.relatorios import relatorio_detalhes_pedido
    relatorio_detalhes_pedido()

elif op == '3':
    from view.relatorios import relatorio_ranking_funcionarios
    relatorio_ranking_funcionarios()