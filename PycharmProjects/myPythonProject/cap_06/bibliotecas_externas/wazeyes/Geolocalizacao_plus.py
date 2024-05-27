# Importa a classe Nominatim do módulo geopy.geocoders
from geopy.geocoders import Nominatim

# Cria uma instância do geolocator usando Nominatim com o user_agent definido como "wazeyes"
geolocator = Nominatim(user_agent="wazeyes")

# Solicita ao usuário que digite um endereço completo (com número e cidade) e armazena o valor na variável 'endereco'
endereco = input("Digite um endereco com número e cidade => Exemplo: avenida paulista, 100 São Paulo:\n")

# Usa o geolocator para obter a geocodificação do endereço fornecido
# Converte o resultado para string e o divide em uma lista usando a vírgula como delimitador
resultado = str(geolocator.geocode(endereco)).split(",")

# Verifica se o primeiro elemento do resultado não é 'None'
if resultado[0] != 'None':
    # Imprime o endereço completo
    print("Endereço completo.: ", resultado)
    # Imprime o segundo dado (geralmente o bairro ou a área)
    print("Bairro............: ", resultado[1])
    # Imprime o terceiro dado (geralmente a cidade)
    print("Cidade............: ", resultado[2])
    # Imprime o quarto dado (geralmente a região ou o estado)
    print("Regiao............: ", resultado[3])
