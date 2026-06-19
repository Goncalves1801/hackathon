import mysql.connector


def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senai",
        database="saep_estoque"
    )
    return conexao

def cadastrar_produto(nome, categorias, quantidade, preco):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO produtos (nome, categorias, quantidade, preco)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nome, categorias, quantidade, preco)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()