from operacoesbd import *

conexao = criarConexao(endereco="127.0.0.1",usuario="root",senha="root",bancodedados="ouvidoria_z")

def pesquisar_codigo(conexao):
    codigo = int(input("\nDigite o código correspondente: "))
    consulta = "select * from ouvidoria where codigo = %s"
    dados = [codigo]

    pesquisar = listarBancoDados(conexao, consulta,dados)
    if pesquisar == []:
        print("\nManifestação com este código não está disponível")
    else:
        print(f"\n{pesquisar[0][0]} - Titulo: {pesquisar[0][1]} \nManifestação: {pesquisar[0][2]} \nTipo: {pesquisar[0][3]} \nNome: {pesquisar[0][4]}")

def excluir_manifestacao (conexao):
    codigo = int(input("Digite o código correspondente para excluir: "))
    consulta = "delete from ouvidoria where codigo = %s"
    dados = [codigo]

    excluir = excluirBancoDados(conexao,consulta,dados)

    if excluir == 0:
        print("Nenhuma manifestação foi excluida.")

    else:
        print("Manifestação excluida com sucesso.")

def adicionar_manifestacao(conexao):
    consulta = "insert into ouvidoria (titulo, manifestacao, tipo_manifestacao, usuario) values (%s, %s, %s, %s)"
    titulo = input("Título da manifestação: ")
    manifestacao = input("Digite sua manifestação: ")
    while True:
        tipo_manifestacao = int(input("Digite o tipo da manifestacao: (1 - reclamação | 2 - Elogio | 3 - Sugestão): "))
        if tipo_manifestacao == 1:
            tipo_manifestacao = "Reclamação"
            break
        elif tipo_manifestacao == 2:
            tipo_manifestacao = "Elogio"
            break
        elif tipo_manifestacao == 3:
            tipo_manifestacao = "Sugestão"
            break
        else:
            print("Digite uma opção válida.")
            continue
    usuario = input("Nome do manifestante: ")
    dados = [titulo,manifestacao,tipo_manifestacao, usuario]
    adicionar = insertNoBancoDados(conexao, consulta, dados)
    print(f"Sucesso! Manifestação adicionada com código {adicionar}")
