from datetime import date

class Pedido:
    def __init__(self, cliente_nome, funcionario_nome, data_pedido=None):
        self.cliente_nome = cliente_nome
        self.funcionario_nome = funcionario_nome
        self.data_pedido = data_pedido or date.today()
        self.itens = []

    def adicionar_item(self, produto_nome, quantidade, preco):
        self.itens.append((produto_nome, quantidade, preco))
