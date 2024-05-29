import getpass
import platform
from datetime import datetime

print("Distribuição do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versão do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())
print("Usuario da Máquina..................: ", getpass.getuser())
print("Dia atual...........................: ", datetime.now().day)
print("Mês atual...........................: ", datetime.now().month)
print("Ano atual...........................: ", datetime.now().year)
print("Horario atual.......................: ", datetime.now())
