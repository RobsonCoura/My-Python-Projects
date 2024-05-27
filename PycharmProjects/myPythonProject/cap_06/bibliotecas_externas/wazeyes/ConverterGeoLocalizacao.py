# Importa a classe Nominatim do módulo geopy.geocoders para geocodificação
import lista
from geopy.geocoders import Nominatim

# Importa as funções ler_arquivo e gravar_arquivo do módulo Funcoes.Funcoes_JSON
from myPythonProject.cap_05.funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo

# Cria uma instância do geolocator usando Nominatim com o user_agent definido como "wazeyes"
geolocator = Nominatim(user_agent="wazeyes")

# Lê o conteúdo do arquivo "entrada.json" e armazena o resultado em um dicionário
dicionario = ler_arquivo("entrada.json")

# Verifica se a chave "endereco" está presente no dicionário e se a lista possui ao menos 5 elementos
if "endereco" in dicionario and len(dicionario["endereco"]) >= 5:
    # Extrai os componentes do endereço
    endereco_lista = dicionario["endereco"]

    # Verifica se a lista de endereços possui ao menos 5 elementos
    if endereco_lista and len(endereco_lista) >= 5:
        # Extrai os componentes individuais do endereço
        rua = endereco_lista[0]
        numero = endereco_lista[1]
        bairro = endereco_lista[2]
        cidade = endereco_lista[3]
        estado = endereco_lista[4]

        # Constrói o endereço para a geocodificação de rua e número
        endereco_rua_numero = f"{rua}, {numero}, {cidade}, {estado}, Brasil"
        # Constrói o endereço para a geocodificação de bairro
        endereco_bairro = f"{bairro}, {cidade}, {estado}, Brasil"

        try:
            # Tenta obter as coordenadas para o endereço de rua e número
            location_rua_numero = geolocator.geocode(endereco_rua_numero)
            if location_rua_numero:
                # Se a geocodificação for bem-sucedida, obtenha as coordenadas
                saida_rua_numero = {"coordenadas": (location_rua_numero.latitude, location_rua_numero.longitude)}
                gravar_arquivo(saida_rua_numero, "saida_rua_numero.json")
                print("Coordenadas do endereço de rua e número salvas com sucesso.")
            else:
                print(f"Não foi possível obter as coordenadas para o endereço de rua e número: {endereco_rua_numero}")

            # Tenta obter as coordenadas para o endereço do bairro
            location_bairro = geolocator.geocode(endereco_bairro)
            if location_bairro:
                # Se a geocodificação for bem-sucedida, obtenha as coordenadas
                saida_bairro = {"coordenadas": (location_bairro.latitude, location_bairro.longitude)}
                gravar_arquivo(saida_bairro, "saida_bairro.json")
                print("Coordenadas do endereço do bairro salvas com sucesso.")
            else:
                print(f"Não foi possível obter as coordenadas para o endereço do bairro: {endereco_bairro}")

        except Exception as e:
            # Trata qualquer exceção que ocorra durante a geocodificação
            print(f"Ocorreu um erro ao tentar obter as coordenadas: {e}")

    else:
        print("O formato do endereço no arquivo 'entrada.json' é inválido.")
