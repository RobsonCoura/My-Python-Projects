# Importando todas as funções do módulo ftplib
from ftplib import *

# Definindo o modo de conexão do FTP (ativo ou passivo). Nesse caso, é passivo (False).
ftp_ativo = False

# Criando um objeto FTP e conectando ao servidor FTP especificado
ftp = FTP('ftp.ibiblio.org')

# Imprimindo a mensagem de boas-vindas recebida do servidor FTP
print(ftp.getwelcome())

# Encerrando a conexão com o servidor FTP
ftp.quit()
