from myPythonProject.cap_04.manipulação_de_dicionário_de_dados.Funcoes import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "p" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
opcao = perguntar()
