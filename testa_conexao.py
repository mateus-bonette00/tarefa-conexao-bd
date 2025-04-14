from database.conexao import conectar

try:
    conn = conectar()
    print("Conexão realizada com sucesso!")
    conn.close()
except Exception as e:
    print("Erro na conexão com o banco de dados:")
    print(e)