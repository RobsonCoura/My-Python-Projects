import serial
from serial.tools import list_ports

conexao = ""  # Variável para armazenar a conexão serial

# Itera sobre todas as portas seriais disponíveis
for port in list_ports.comports():
    # Imprime a descrição do dispositivo e a porta correspondente
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))

    # Verifica se a descrição do dispositivo contém "ARDUINO"
    if "ARDUINO" in port.description.upper():
        try:
            # Tenta estabelecer uma conexão serial com a porta encontrada
            conexao = serial.Serial(port.device, 115200)
            # Imprime a mensagem de conexão bem-sucedida
            print("Conexao realizada com {}.".format(conexao.portstr))
        except:
            pass

        # Se a conexão foi estabelecida com sucesso
        if conexao != "":
            while True:
                # Lê uma linha da porta serial
                resposta = conexao.readline()
                # Converte a resposta para um número de ponto flutuante e imprime
                print(float(resposta.decode()))
                # Fecha a conexão serial
                conexao.close()
