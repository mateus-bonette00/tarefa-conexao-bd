from dao.relatorio_dao import buscar_detalhes_pedido

def relatorio_detalhes_pedido():
    try:
        order_id = int(input("Digite o número do pedido que deseja consultar: "))
        buscar_detalhes_pedido(order_id)
    except ValueError:
        print("ID inválido. Digite um número inteiro.")

from dao.relatorio_dao import ranking_funcionarios_por_periodo

def relatorio_ranking_funcionarios():
    try:
        data_inicio = input("Data início (YYYY-MM-DD): ")
        data_fim = input("Data fim (YYYY-MM-DD): ")
        ranking_funcionarios_por_periodo(data_inicio, data_fim)
    except Exception as e:
        print("Erro ao gerar relatório:", e)