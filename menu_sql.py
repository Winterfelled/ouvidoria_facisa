from operacoesbd import criarConexao
https://code-with-me.global.jetbrains.com/J-Ovfpr8Ppme1ld_j_953g#p=PC&fp=E5E2872E5371F1EB0EE788CC92B766E65CF16F3071B022492B25776E396B67F9&newUi=true

conexao = criarConexao(endereco="127.0.0.1",usuario="root",senha="root",bancodedados="ouvidoria_z")

opcao = -1

while opcao != 7:

    print("\n- Bem vindo ao sistema de ouvidoria da unifacisa -")
    print("1) Listar manifestações | 2) Listar Manifestações por código | 3) Criar uma nova manisfestação")
    print("4) Exibir quantidade de manifestações | 5) Pesquisar manifestação por código 6) Excluir uma manifestação por código")
    print("7) Sair do sistema")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("listar")

    elif opcao == 2:
        print("listar por codigo")

    elif opcao == 3:
        print("criar nova manisfestacao")

    elif opcao == 4:
        print("Exibir quantidade de manifestações")

    elif opcao == 5:
        print("Pesquisar manifestação por código")

    elif opcao == 6:
        print("Excluir por código")

    elif opcao != 7:
        print("Opcão inválida.")
