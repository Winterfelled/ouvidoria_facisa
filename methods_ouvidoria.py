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
    while True:
        consulta = "insert into ouvidoria (titulo, manifestacao, tipo_manifestacao, usuario) values (%s, %s, %s, %s)"
        titulo = input("\nTítulo da manifestação: ")
        manifestacao = input("Digite sua manifestação: ")
        usuario = input("Nome do manifestante: ")

        if len(consulta) == 0 or len(titulo) == 0 or len(manifestacao) == 0 or len(usuario) == 0:
            print("Um dos valores inseridos é inválido, tente novamente.")

        else:
            break

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
    dados = [titulo,manifestacao,tipo_manifestacao, usuario]
    adicionar = insertNoBancoDados(conexao, consulta, dados)
    print(f"Sucesso! Manifestação adicionada com código {adicionar}")

def listar_por_tipo(conexao):
    while True:
        try:
            codigo = int(input(
                "Indique o tipo da manifestação que você deseja consultar:\n"
                "1 - Reclamação\n"
                "2 - Elogio\n"
                "3 - Sugestão\n"
                "1 - Sair\n"
                "Opção: "
            ))

            if codigo == -1:
                print("Saindo da consulta.")
                return  

            if codigo not in [1, 2, 3]:
                print("Opção inválida. Tente novamente.")
                continue

            if codigo == 1:
                dados1 = "Reclamação"
            elif codigo == 2:
                dados1 = "Elogio"
            else:
                dados1 = "Sugestão"

            consulta = "SELECT * FROM ouvidoria WHERE tipo_manifestacao = %s"
            dados = [dados1]
            lista = listarBancoDados(conexao, consulta, dados)

            if not lista:
                print("Nenhuma manifestação encontrada para esse tipo.")
            else:
                print("Resultados encontrados:")
                for item in lista:
                    print(f"\n{item[0]} - Titulo: {item[1]} \nManifestação: {item[2]} \n Tipo: {item[3]} \n Nome: {item[4]}")

            return  # Finaliza a função após exibir o resultado


        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def quantidade_Manifestacoes(conexao):
    consulta = 'select count(*) from ouvidoria'
    quantidade_Manifestacoes = listarBancoDados(conexao, consulta)
    print("Atualmente Temos", quantidade_Manifestacoes[0][0], "manifestação(oes) listadas!")

def listar(conexao):
    consulta = "select * from ouvidoria"
    lista_de_manifestacao = listarBancoDados(conexao,consulta)
    for item in lista_de_manifestacao:
        print(item)
