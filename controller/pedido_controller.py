from model.pedido import Pedido
from dao.pedido_dao import inserir_pedido

def criar_pedido_com_itens(cliente, funcionario, itens):
    pedido = Pedido(cliente, funcionario)
    for item in itens:
        produto_nome, quantidade, preco = item
        pedido.adicionar_item(produto_nome, quantidade, preco)
    inserir_pedido(pedido)

from dao.pedido_dao_inseguro import inserir_pedido_inseguro

def criar_pedido_inseguro(cliente, funcionario, itens):
    pedido = Pedido(cliente, funcionario)
    for item in itens:
        produto_nome, quantidade, preco = item
        pedido.adicionar_item(produto_nome, quantidade, preco)
    inserir_pedido_inseguro(pedido)
    
from dao.pedido_dao_orm import inserir_pedido_orm

def criar_pedido_orm(cliente, funcionario, itens):
    pedido = Pedido(cliente, funcionario)
    for item in itens:
        produto_nome, quantidade, preco = item
        pedido.adicionar_item(produto_nome, quantidade, preco)
    inserir_pedido_orm(pedido)