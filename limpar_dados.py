import sqlite3
import os

# Caminho do banco
DB_PATH = os.path.join("data", "usuarios.db")

def limpar_dados():
    if not os.path.exists(DB_PATH):
        print("❌ Banco de dados não encontrado.")
        return

    try:
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()

        cur.execute("DELETE FROM usuarios;")
        con.commit()
        con.close()

        print("✅ Todos os dados da tabela 'usuarios' foram apagados com sucesso.")
    except Exception as e:
        print(f"⚠️ Erro ao limpar dados: {e}")

if __name__ == "__main__":
    limpar_dados()
