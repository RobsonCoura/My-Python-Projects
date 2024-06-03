# Importando todas as funções do módulo socket
from socket import *

# Definindo o endereço IP do servidor
servidor = "127.0.0.1"

# Definindo a porta que será usada para a comunicação
porta = 43210

# Criando um objeto socket UDP
obj_socket = socket(AF_INET, SOCK_DGRAM)

# Associando o socket ao endereço IP e porta especificados
obj_socket.bind((servidor, porta))

# Informando que o servidor está pronto para receber dados
print("Servidor pronto....")

# Loop infinito para manter o servidor ativo
while True:
    # Recebendo dados do cliente (com buffer de até 65535 bytes)
    dados, origem = obj_socket.recvfrom(65535)

    # Exibindo o endereço de origem dos dados recebidos
    print("Origem..........: ", origem)

    # Exibindo os dados recebidos, decodificados de bytes para string
    print("Dados recebidos.: ", dados.decode())

    # Solicitando ao usuário que digite uma resposta para enviar ao cliente
    resposta = input("Digite a resposta: ")

    # Enviando a resposta ao cliente, codificada de string para bytes
    obj_socket.sendto(resposta.encode(), origem)

# Fechando a conexão do socket (nunca será alcançado devido ao loop infinito)
obj_socket.close()
