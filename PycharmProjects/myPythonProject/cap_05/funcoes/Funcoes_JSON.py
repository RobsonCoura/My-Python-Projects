import json
import os


def chamarMenu():
    # Exibe o menu de opções e retorna a escolha do usuário como um inteiro
    escolha = int(input("Digite: \n"
                        "<1> para registrar ativo\n"
                        "<2> para exibir ativos armazenados: "))
    return escolha


def ler_arquivo(arquivo):
    # Verifica se o arquivo existe
    if os.path.exists(arquivo):
        # Abre o arquivo no modo de leitura
        with open(arquivo, "r") as arq_json:
            # Lê o conteúdo do arquivo JSON e o converte para um dicionário
            dicionario = json.load(arq_json)
    else:
        # Se o arquivo não existe, retorna um dicionário vazio
        dicionario = {}
    return dicionario


def gravar_arquivo(dicionario, arquivo):
    # Abre o arquivo no modo de escrita
    with open(arquivo, "w") as arq_json:
        # Converte o dicionário para JSON e escreve no arquivo
        json.dump(dicionario, arq_json)


def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        # Solicita ao usuário que insira os detalhes do ativo
        numero_patrimonial = input("Digite o número patrimonial: ")
        data_atualizacao = input("Digite a data da última atualização: ")
        descricao = input("Digite a descrição: ")
        departamento = input("Digite o departamento: ")

        # Armazena os detalhes do ativo no dicionário
        dicionario[numero_patrimonial] = [data_atualizacao, descricao, departamento]

        # Pergunta se o usuário deseja continuar registrando ativos
        resp = input("Digite <S> para continuar.").upper()

    # Grava o dicionário atualizado no arquivo
    gravar_arquivo(dicionario, arquivo)
    return "JSON gerado!!!!"


def exibir(arquivo):
    # Lê o conteúdo do arquivo JSON e o converte para um dicionário
    dicionario = ler_arquivo(arquivo)
    # Exibe cada ativo armazenado no inventário
    for chave, dado in dicionario.items():
        print(f"Número Patrimonial: {chave}")
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])