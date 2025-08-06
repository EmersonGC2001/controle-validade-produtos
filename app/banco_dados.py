import sqlite3
import os

# Caminho correto do banco
DB_PATH = os.path.join("data", "usuarios.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Cria a tabela se não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
""")
conn.commit()

def adicionar_usuario(nome):
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()

def listar_usuarios():
    cursor.execute("SELECT nome FROM usuarios")
    return [linha[0] for linha in cursor.fetchall()]
