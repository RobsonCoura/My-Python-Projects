# Abre o arquivo "pagina.html" no modo de escrita ("w")
with open("pagina.html", "w") as pagina:
    # Escreve o início do corpo HTML com um título de nível 1
    pagina.write("<body> <h1> Esta é um teste para página WEB </h1>")

    # Escreve um título de nível 2 seguido por uma breve descrição
    pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto: </h2>")

    # Inicia um título de nível 3 para listar os nomes
    pagina.write("<h3>")

    # Inicializa a variável 'nome' com uma string vazia
    nome = ""

    # Loop que continua pedindo nomes até que o usuário digite "SAIR"
    while nome != "SAIR":
        # Solicita ao usuário que digite um nome ou "SAIR"
        nome = input("Digite um nome ou SAIR: ").upper()

        # Se o nome digitado não for "SAIR", escreve o nome na página HTML
        if nome != "SAIR":
            pagina.write("<br>" + nome)

    # Fecha o título de nível 3 e o corpo HTML
    pagina.write("</h3></body>")
