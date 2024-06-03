import socket  # Importa o módulo de rede 'socket'.

resp = "S"  # Define a variável de controle 'resp' com valor inicial "S".

while (resp == "S"):  # Continua executando enquanto 'resp' for "S".
    url = input("Digite uma url: ") # Solicita ao usuário uma URL.
    ip = socket.gethostbyname(url) # Obtém o endereço IP da URL.
    print("O IP referente a url informada é: ", ip) # Exibe o endereço IP.
    resp = input("Digite <S> para continuar: ").upper() # Pergunta se o usuário deseja continuar e converte a resposta para maiúsculas.
