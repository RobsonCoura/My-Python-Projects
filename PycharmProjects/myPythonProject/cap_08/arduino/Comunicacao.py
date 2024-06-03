# Importando o módulo serial para comunicação serial
import serial

# Importando a ferramenta list_ports do módulo serial.tools para listar portas seriais disponíveis
from serial.tools import list_ports

# Listando todas as portas seriais disponíveis
for port in list_ports.comports():
    # Imprimindo a descrição do dispositivo e a porta correspondente
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))

    # Estabelecendo conexão serial com a porta 'COM3' e taxa de transmissão de 115200 bps
    conexao = serial.Serial('COM3', 115200)

    # Solicitando ao usuário que digite uma ação: <L> para Ligar ou <D> para Desligar
    acao = input("Digite:\n<L> para Ligar\n<D> para Desligar: ").upper()

    # Mantendo o loop enquanto a ação for "L" (Ligar) ou "D" (Desligar)
    while acao == "L" or acao == "D":
        if acao == "L":
            # Enviando o byte '1' para a porta serial se a ação for "L"
            conexao.write(b'1')
        else:
            # Enviando o byte '0' para a porta serial se a ação for "D"
            conexao.write(b'0')

        # Solicitando novamente ao usuário que digite uma ação: <L> para Ligar ou <D> para Desligar
        acao = input("Digite:\n<L> para Ligar\n<D> para Desligar: ").upper()

    # Fechando a conexão serial
    conexao.close()
    # Informando que a conexão foi encerrada
    print("Conexao encerrada")
