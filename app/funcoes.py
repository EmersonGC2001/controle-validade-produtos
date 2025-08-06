def saudacao(nome):
    return f"✅ Usuário cadastrado: {nome}"

def exibir_lista(nomes):
    print("\n📋 Lista de usuários:")
    for nome in nomes:
        print(f"• {nome}")
