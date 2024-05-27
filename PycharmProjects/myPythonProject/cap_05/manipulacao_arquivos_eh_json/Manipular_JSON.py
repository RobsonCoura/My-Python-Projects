from myPythonProject.cap_05.funcoes.Funcoes_JSON import *
# Lê o inventário do arquivo JSON
inventario = ler_arquivo("inventario_json.json")

# Exibe o menu de opções e obtém a escolha do usuário
opcao = chamarMenu()

# Continua executando enquanto a opção for válida (entre 1 e 2)
while opcao > 0 and opcao < 3:
    if opcao == 1:
        # Registra um novo ativo e exibe a mensagem de confirmação
        print(registrar(inventario, "inventario_json.json"))
    elif opcao == 2:
        # Exibe os ativos armazenados no inventário
        exibir("inventario_json.json")

    # Exibe o menu novamente e obtém a nova escolha do usuário
    opcao = chamarMenu()
