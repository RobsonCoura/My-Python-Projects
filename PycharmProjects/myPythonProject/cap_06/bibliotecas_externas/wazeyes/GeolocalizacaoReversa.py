# Importa a classe Nominatim do módulo geopy.geocoders
from geopy.geocoders import Nominatim

# Cria uma instância do geolocator usando Nominatim com o user_agent definido como "wazeyes"
geolocator = Nominatim(user_agent="wazeyes")

# Solicita ao usuário que digite a latitude e armazena o valor como um float
latitude = float(input("Digite a latitude...: "))

# Solicita ao usuário que digite a longitude e armazena o valor como um float
longitude = float(input("Digite a longitude.: "))

# Usa o geolocator para obter o endereço reverso com base na latitude e longitude fornecidas
# Converte o resultado para string e o divide em uma lista usando a vírgula como delimitador
resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")

# Verifica se o primeiro elemento do resultado não é 'None'
if resultado[0] != 'None':
    # Imprime o endereço completo
    print("Endereço completo.: ", resultado)
    # Imprime o primeiro dado (parte do endereço)
    print("Dado 1............: ", resultado[0])
    # Imprime o segundo dado (parte do endereço)
    print("Dado 2............: ", resultado[1])
    # Imprime o terceiro dado (parte do endereço)
    print("Dado 3............: ", resultado[2])
