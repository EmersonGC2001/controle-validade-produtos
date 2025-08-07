from app.funcoes import listar_produtos, atualizar_quantidade, excluir_produto, adicionar_produto, deseja_continuar
from app.banco_dados import criar_tabela


def main(): # Função principal que inicia o sistema 
    criar_tabela()


    print("=== SISTEMA DE PRODUTOS ===")

    while True:
        print('=' * 50)
        print('[0] Adicionar Produtos')
        print('[1] Listar Produtos')    
        print('[2] Atualizar Quantidade')   
        print('[3] Excluir Produtos')
        print('[4] Sair')
        print('=' * 50)

        try:
            opcao = int(input('Escolha uma opção: '))
        except ValueError:
            print("❌ Opção inválida. Digite um número.")
            continue

        if opcao == 0:
            adicionar_produto()
        elif opcao == 1:
            listar_produtos()
        elif opcao == 2:
            atualizar_quantidade()
        elif opcao == 3:
            excluir_produto()
        elif opcao == 4:
            print("👋 Saindo do sistema.")
            break
        else:
            print('❌ Opção inválida.')

        print('-' * 50)
        if not deseja_continuar():
            break


if __name__ == "__main__":
    main()
