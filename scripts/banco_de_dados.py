import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def criar_banco_de_dados():
    """Script para criar o banco de dados student_db se não existir"""
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="0",
            port="5432"
        )
        conexao.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'student_db'")
        existe = cursor.fetchone()
        
        if not existe:
            cursor.execute('CREATE DATABASE student_db')
            print("Banco de dados 'student_db' criado com sucesso!")
        else:
            print("ℹBanco de dados 'student_db' já existe.")
        
        cursor.close()
        conexao.close()
        
    except psycopg2.Error as e:
        print(f"Erro ao criar banco de dados: {e}")
        print("Verifique se o PostgreSQL está rodando e as credenciais estão corretas.")

if __name__ == "__main__":
    criar_banco_de_dados()