from socket import *  # Importa todas as funções e constantes do módulo socket.

servidor = "127.0.0.1"  # Endereço IP do servidor (localhost).
porta = 43210  # Porta em que o servidor estará ouvindo as conexões.

# Cria um objeto socket. AF_INET indica que será usado o protocolo IPv4, SOCK_STREAM indica que será um socket TCP.
obj_socket = socket(AF_INET, SOCK_STREAM)

# Liga o socket ao endereço do servidor e à porta especificada.
obj_socket.bind((servidor, porta))

# Define o número máximo de conexões pendentes que o socket aceitará. Neste caso, 2.
obj_socket.listen(2)

print("Aguardando cliente....")

# Loop principal para aceitar conexões de clientes continuamente.
while True:
    # Aceita a conexão e retorna um novo objeto socket e o endereço do cliente.
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)

    # Loop secundário para lidar com a comunicação com o cliente atual.
    while True:
        # Recebe uma mensagem do cliente. O número 1024 indica o tamanho máximo dos dados recebidos.
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)

        # Envia uma mensagem de volta para o cliente.
        msg_enviada = b'Olah cliente'  # A mensagem é convertida para bytes.
        con.send(msg_enviada)

        break  # Sai do loop secundário para aguardar mais mensagens do cliente.

    # Fecha a conexão com o cliente atual.
    con.close()
