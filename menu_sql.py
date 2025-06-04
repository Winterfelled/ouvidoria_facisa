from operacoesbd import criarConexao

conexao = criarConexao(endereco="127.0.0.1",usuario="root",senha="programa@11",bancodedados="ouvidoria")

opcao = -1

while opcao != 6:

    print("\n- Bem vindo ao sistema de ouvidoria da unifacisa -")
    print("1) Listar manifestações 2) Coloque seu feedback 3)Remover feedback ")