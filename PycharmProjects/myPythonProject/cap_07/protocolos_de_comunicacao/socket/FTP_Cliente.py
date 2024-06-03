# Importando todas as funções do módulo ftplib
from ftplib import *

# Definindo o modo de conexão do FTP (ativo ou passivo). Nesse caso, é passivo (False).
ftp_ativo = False

# Criando um objeto FTP e conectando ao servidor FTP especificado
ftp = FTP('ftp.ibiblio.org')

# Imprimindo a mensagem de boas-vindas recebida do servidor FTP
print(ftp.getwelcome())

# Solicitando ao usuário que digite o nome de usuário para login no servidor FTP
usuario = input("Digite o usuario: ")

# Solicitando ao usuário que digite a senha para login no servidor FTP
senha = input("Digite a senha: ")

# Realizando login no servidor FTP com o nome de usuário e senha fornecidos
ftp.login(usuario, senha)

# Imprimindo o diretório atual de trabalho no servidor FTP
print("Diretório atual de trabalho: ", ftp.pwd())

# Alterando o diretório de trabalho para 'pub' no servidor FTP
ftp.cwd('pub')

# Imprimindo o novo diretório de trabalho após a mudança
print("Diretório corrente: ", ftp.pwd())

# Listando os arquivos e diretórios no diretório atual e imprimindo a lista
print(ftp.retrlines('LIST'))

# Encerrando a conexão com o servidor FTP
ftp.quit()
