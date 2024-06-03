# Importando todas as funções do módulo socket
from socket import *

# Definindo o endereço IP do servidor
servidor = "127.0.0.1"

# Definindo a porta que será usada para a comunicação
porta = 43210

# Criando um objeto socket UDP
obj_socket = socket(AF_INET, SOCK_DGRAM)

# Conectando o socket ao servidor especificado (endereço IP e porta)
obj_socket.connect((servidor, porta))

# Inicializando a variável de controle 'saida' com uma string vazia
saida = ""

# Loop que continua até que o usuário digite "X" para sair
while saida != "X":
    # Solicitando ao usuário que digite uma mensagem para enviar ao servidor
    msg = input("Sua mensagem: ")

    # Enviando a mensagem ao servidor, codificada de string para bytes
    obj_socket.sendto(msg.encode(), (servidor, porta))

    # Recebendo a resposta do servidor (com buffer de até 65535 bytes)
    dados, origem = obj_socket.recvfrom(65535)

    # Exibindo a resposta recebida do servidor, decodificada de bytes para string
    print("Resposta do Servidor: ", dados.decode())

    # Solicitando ao usuário que digite "X" para sair ou outra tecla para continuar
    saida = input("Digite <X> para sair: ").upper()

# Fechando a conexão do socket
obj_socket.close()
