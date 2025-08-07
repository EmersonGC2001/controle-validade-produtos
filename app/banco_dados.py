import sqlite3
import os

# Caminho correto do banco
DB_PATH = os.path.join("data", "produtos.db")

# Função para conectar ao banco
def conectar():
    return sqlite3.connect(DB_PATH)

# Função para criar a tabela se não existir
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            data_vencimento TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
