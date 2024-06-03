# Importando todas as funções do módulo socket
from socket import *

# Definindo o endereço IP do servidor(localhost) e a porta que será usada para a comunicação
servidor = "127.0.0.1"
porta = 43210

# Solicitando ao usuário que digite uma mensagem para enviar ao servidor
msg = bytes(input("Digite algo: "), 'utf-8')

# Criando um objeto socket TCP/IP
obj_socket = socket(AF_INET, SOCK_STREAM)

# Estabelecendo uma conexão com o servidor usando o endereço IP e a porta especificados
obj_socket.connect((servidor, porta))

# Enviando a mensagem ao servidor
obj_socket.send(msg)

# Recebendo a resposta do servidor (com buffer de até 1024 bytes)
resposta = obj_socket.recv(1024)

# Exibindo a resposta recebida do servidor
print("Recebemos: ", resposta)

# Fechando a conexão com o servidor
obj_socket.close()
