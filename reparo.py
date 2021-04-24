import os
from time import sleep as s
# comandos para reparar o erro do E-tube
print("\033[1;31mReparando o script...\033[m\n")

os.system("pip uninstall pytube -y")
os.system("pip install -r requirements.txt")

print("\n\033[1;32mReparação completa!\033[m")
s(1.5)
os.system("clear")
os.syste("ls")
