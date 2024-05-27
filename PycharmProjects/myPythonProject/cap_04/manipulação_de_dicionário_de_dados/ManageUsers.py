from myPythonProject.cap_05.funcoes.Funcoes_Dicionarios import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "p" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    opcao = perguntar()
