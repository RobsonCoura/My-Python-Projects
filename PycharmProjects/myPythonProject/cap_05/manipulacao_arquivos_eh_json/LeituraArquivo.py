# Abre o arquivo "teste.txt" no modo de leitura ("r")
with open("teste.txt", "r") as arquivo:
    # Lê todoo o conteúdo do arquivo e armazena na variável 'conteudo'
    conteudo = arquivo.read()

# Imprime o tipo de dado da variável 'conteudo'
print("Tipo de dado da variável:", type(conteudo))

# Imprime o conteúdo do arquivo
print("\nConteúdo do arquivo:\n", conteudo)
