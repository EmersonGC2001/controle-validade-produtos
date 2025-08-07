import sqlite3
from app.banco_dados import conectar

def adicionar_produto():
    while True: # Função para adicionar um produto
        try:
            produto = input('Digite o nome do produto: ').upper()
            break
        except ValueError:
            print('❌ Erro: Digite um número válido para a quantidade.')
            return
    while True:
        try:
            quantidade = int(input('Digite a quantidade: '))
            break
        except ValueError:
            print('❌ Erro: Digite um número válido para a quantidade.')
            return
    while True:
        try:
            data_vencimento = input('Digite a data de vencimento: ')
            break
        except ValueError:
            print('❌ Erro: Digite uma data válida.')
            return

    conn = sqlite3.connect("data/produtos.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produtos (produto, quantidade, data_vencimento)
        VALUES (?, ?, ?)
    """, (produto, quantidade, data_vencimento))

    conn.commit()
    conn.close()

    print('Produto adicionado com sucesso! ✅')
    print('=' * 30)
    listar_produtos()




def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, produto, quantidade, data_vencimento FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    if not produtos:
        print('Nenhum produto cadastrado.')
        return

    print()
    print("📦 Produtos cadastrados:")
    print('=' * 30)

    for pid, nome, qtd, venc in produtos: # Exibe os produtos cadastrados
        print(f"[{pid}] | {nome} | {qtd} | VENCIMENTO: {venc}")
    print('=' * 30)




def excluir_produto():
    listar_produtos()
    pid = int(input("Digite o ID do produto a excluir: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id = ?", (pid,))
    conn.commit()
    conn.close()

    print("🗑️ Produto excluído com sucesso.")



def atualizar_quantidade():
    listar_produtos()
    pid = int(input("Digite o ID do produto a atualizar: "))
    nova_qtd = int(input("Nova quantidade: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_qtd, pid))
    conn.commit()
    conn.close()

    print("🔁 Quantidade atualizada com sucesso.")





def deseja_continuar():
    q = input('Deseja continuar? [s/n] ').lower()
    if q == 'n':
        print('Produtos próximos da válidade!\n')
        print('=' * 30)
        listar_produtos()
        print('👋 Saindo do sistema.')
        return False
    elif q == 's':
        print('🔁 Continuando...')
        return True
    else:
        print('❌ Opção inválida')
        return deseja_continuar()
