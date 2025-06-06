from methods_ouvidoria import *

opcao = -1

while opcao != 7:

    print("\n- Bem vindo ao sistema de ouvidoria da unifacisa -")
    print("1) Listar manifestações | 2) Listar Manifestações por tipo | 3) Criar uma nova manisfestação")
    print("4) Exibir quantidade de manifestações | 5) Pesquisar manifestação por código | 6) Excluir uma manifestação por código")
    print("7) Sair do sistema")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("listar")

    elif opcao == 2:
        listar_por_tipo(conexao)

    elif opcao == 3:
        adicionar_manifestacao(conexao)

    elif opcao == 4:
        print("Exibir quantidade de manifestações")

    elif opcao == 5:
        pesquisar_codigo(conexao)

    elif opcao == 6:
        excluir_manifestacao(conexao)

    elif opcao != 7:
        print("Opcão inválida.")

encerrarConexao(conexao)
print("Obrigado por utilizar o sistema de manifestações da FACISA.")
