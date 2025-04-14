import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="northwind",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
