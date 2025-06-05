from operacoesbd import *

conexao = criarConexao(endereco="127.0.0.1",usuario="root",senha="root",bancodedados="ouvidoria_z")

def pesquisar_codigo(conexao):
    codigo = int(input("\nDigite o código correspondente: "))
    consulta = "select * from ouvidoria where codigo = %s"
    dados = [codigo]

    ouvidoria = listarBancoDados(conexao, consulta,dados)
    if ouvidoria == []:
        print("\nManifestação com este código não está disponível")
    else:
        print(f"\n{ouvidoria[0][0]} - Titulo: {ouvidoria[0][1]} \nManifestação: {ouvidoria[0][2]} \nTipo: {ouvidoria[0][3]} \nNome: {ouvidoria[0][4]}")

def excluir_manifestacao (conexao):
    codigo = int(input("Digite o código correspondente para excluir: "))
    consulta = "delete from ouvidoria where codigo = %s"
    dados = [codigo]

    ouvidoria = excluirBancoDados(conexao,consulta,dados)

    if ouvidoria == 0:
        print("Nenhuma manifestação foi excluida.")

    else:
        print("Manifestação excluida com sucesso.")
