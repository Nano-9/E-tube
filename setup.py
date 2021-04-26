# setup para rodar o E-tube corretamente
import os
from time import sleep

def instalar_bibliotecas_necessarias():
	os.system("clear")
	print("\033[1;31m[Atenção]: Usuários do termux, esse processo pode dar errado devido a versão ou espaço no disco\033[m\n")
	input("Enter para continuar a instalação: ")
	os.system("clear")
	print("\033[1;31m[+] Iniciando a instalação...\033[m")
	sleep(1.2)
	os.system("clear")
	os.system("pip install --upgrade pip")
	os.system("pip install ffmpeg moviepy")

instalar_bibliotecas_necessarias()
