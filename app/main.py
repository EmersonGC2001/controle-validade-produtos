from app.banco_dados import adicionar_usuario, listar_usuarios
from app.funcoes import saudacao, exibir_lista

def main():
    print("=== SISTEMA DE USUÁRIOS ===")

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ").strip()
        if nome.lower() == 'sair':
            break

        adicionar_usuario(nome)
        print(saudacao(nome))

    usuarios = listar_usuarios()
    exibir_lista(usuarios)

if __name__ == "__main__":
    main()
