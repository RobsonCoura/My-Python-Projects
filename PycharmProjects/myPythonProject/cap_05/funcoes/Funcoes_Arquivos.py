def chamarMenu():
    # Solicita ao usuário que escolha uma opção do menu e retorna a escolha como um inteiro
    escolha = int(input("Digite: \n"
                        "<1> para registrar ativo\n"
                        "<2> para persistir em arquivo\n"
                        "<3> para exibir ativos armazenados: "))
    return escolha


def registrar(dicionario):
    # Inicializa a variável de resposta como "S" para entrar no loop
    resp = "S"
    while resp == "S":
        # Solicita ao usuário que insira os detalhes do ativo e os armazena no dicionário
        numero_patrimonial = input("Digite o número patrimonial: ")
        data_atualizacao = input("Digite a data da última atualização: ")
        descricao = input("Digite a descrição: ")
        departamento = input("Digite o departamento: ")
        dicionario[numero_patrimonial] = [data_atualizacao, descricao, departamento]

        # Pergunta se o usuário deseja continuar registrando ativos
        resp = input("Digite <S> para continuar.").upper()


def persistir(dicionario):
    # Abre o arquivo "inventario.csv" no modo de append ("a")
    with open("inventario.csv", "a") as inv:
        # Escreve cada item do dicionário no arquivo, separado por ponto e vírgula
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
    return "Persistido com sucesso"


def exibir():
    # Abre o arquivo "inventario.csv" no modo de leitura ("r")
    with open("inventario.csv", "r") as inv:
        # Lê todas as linhas do arquivo e as retorna como uma lista
        linhas = inv.readlines()
    return linhas
