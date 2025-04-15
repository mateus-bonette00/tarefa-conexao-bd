from pedidos.dao.pedido_dao import inserir_pedido
from pedidos.dao.pedido_dao_inseguro import inserir_pedido_inseguro
from pedidos.dao.pedido_dao_orm import inserir_pedido_orm
from pedidos.model.pedido import Pedido

def criar_pedido_com_itens(cliente, funcionario, itens, modo="seguro"):
    pedido = Pedido(cliente, funcionario)
    for produto_nome, quantidade, preco in itens:
        pedido.adicionar_item(produto_nome, quantidade, preco)

    if modo == "inseguro":
        return inserir_pedido_inseguro(pedido)
    elif modo == "orm":
        return inserir_pedido_orm(pedido)
    else:
        return inserir_pedido(pedido)