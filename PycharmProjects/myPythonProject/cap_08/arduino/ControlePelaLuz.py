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
            print("Iniciando...")
            while True:
                print("Recebendo dados...")
                # Lê uma linha da porta serial e converte para um número de ponto flutuante
                resposta = conexao.readline()
                valor = float(resposta.decode())
                # Imprime o valor recebido
                print(valor)
                # Se o valor for inferior a 700, envia o byte '1' pela porta serial
                if valor < 700:
                    conexao.write(b'1')
                else:
                    # Caso contrário, envia o byte '0' pela porta serial
                    conexao.write(b'0')
                    # Fecha a conexão serial
                    conexao.close()
                    print("Conexao encerrada!")
        else:
            print("Sem portas disponíveis!")
