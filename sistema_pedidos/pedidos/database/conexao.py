import psycopg2



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> IMPORTANTE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Atualize a senha do banco de dados
def conectar():
    try:
        conexao = psycopg2.connect(
            dbname="northwind",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        return conexao
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Só pra verificar se a conexão tá funcionando mesmo
def testar_conexao():
    conexao = conectar()
    if conexao:
        print("Conexão estabelecida com sucesso!")
        # Verificar se é possível executar uma consulta simples
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT version()")
            versao_db = cursor.fetchone()
            print(f"Versão do PostgreSQL: {versao_db[0]}")
            cursor.close()
        except psycopg2.Error as e:
            print(f"Conexão estabelecida, mas erro ao executar consulta: {e}")
        finally:
            conexao.close()
            print("Conexão fechada.")
        return True
    else:
        print("Falha ao estabelecer conexão.")
        return False


# Não tinha ctz qual q era o meu user, criei essa função só pra printar qual q era
def get_current_user():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT current_user")
        user = cursor.fetchone()[0]
        cursor.close()
        conexao.close()
        return user
    else:
        return None


if __name__ == "__main__":
    testar_conexao()
    print(get_current_user()) # <<<<< printando o user