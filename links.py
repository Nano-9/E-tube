# parte de log do script

from time import sleep as s
import sys
import getpass
import os


comandos = sys.argv

if len(comandos) == 2:
	login = sys.argv[1]
	if login == "--visualizar" or "--v":
		print("Abrindo arquivo de log...")
		s(1)
		os.system("clear")
		print("================== HISTÓRICO DE DOWNLOADS ==================\n")
		os.system("cat links")
		s(0.2)
		print("\n==========================================================\n")
else:
	print("\033[1;31m[info] Use python links.py --visualizar ou --v\033[m")
