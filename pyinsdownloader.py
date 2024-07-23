# partição do script que baixa videos/fotos do instagram
# by: Nano-9

import re
import os
import sys
import instaloader
import getpass
from time import sleep as suspender
from instaloader import Post


def validar_links_instagram(links):
	valid = re.search(r"^(?=(https://)(\w+)(\.)(instagram)(\.)(com)(\/p)(\/)((.){11})(\/)$)",links)
	return valid
def baixar_videos_instagram():
	os.system("clear")
	instancia = instaloader.Instaloader()
	try:
		user = str(input("\033[1;33m[*]\033[m Nome de usuário ou e-mail: "))
		password = getpass.getpass("Senha: ")
		print("Logando na sua conta...")
		instancia.login(user=user,passwd=password)
	except:
		print("\n\033[1;31mX\033[m Usuário ou senha inválidos!")
		suspender(1.3)
		os.system("clear")
	else:
		print("\033[1;92m✔\033[m Logado")
		print("\033[1;92m✔\033[m Sua conta foi confirmada e pode prosseguir com os downloads!")
		suspender(1.3)
		os.system("clear")
		while True:
			print("""
MENU:

\033[1;36m[\033[m \033[1;31m1\033[m \033[1;36m]\033[m - Baixar uma foto
\033[1;36m[\033[m \033[1;31m2\033[m \033[1;36m]\033[m - Baixar a foto de algum perfil
\033[1;36m[\033[m \033[1;31m3\033[m \033[1;36m]\033[m - Baixar um vídeo
\033[1;36m[\033[m \033[1;31mx\033[m \033[1;36m]\033[m - Cancelar e sair
\n		""")
			user_escolhe = str(input("\033[1;33mO que você deseja fazer:\033[m "))
			if user_escolhe.isnumeric():
				user_escolhe = int(user_escolhe)
				if user_escolhe == 1:
					print()
					link_post = str(input("\033[1;33m[+]\033[m Url da foto: "))
					print()
					if validar_links_instagram(links=link_post):
						fatiar_urls = link_post[28:39]
						post_instagram = Post.from_shortcode(instancia.context, fatiar_urls)
						print("\033[1;31m[+] Iniciando o download da imagem...\033[m")
						instancia.download_post(post_instagram,target="Post")
						print("\n\033[1;32m[*] Download completo!\n\033[m")
						print("\033[1;36mVoltando ao menu...\033[m")
						suspender(1)
						os.system("clear")
						break
					else:
						print("\033[1;31m[!] Essa url não é válida ou está quebrada!\033[m")
						suspender(1.3)
						os.system("clear")
						break

				elif user_escolhe == 2:
					print("\033[1;33m[!] Esse processo salva a foto em uma pasta com o")
					print("nome de usuário!\n\033[m")
					nome_usuario_perfil = str(input("\033[1;33m[*] Nome de usuário:\033[m "))
					print("\n\033[1;31m[+] Iniciando o download da foto de perfil...\n\033[m")
					instancia.download_profile(nome_usuario_perfil, profile_pic_only=True)
					print("\n\033[1;32m[*] Download completo!")
					print("\033[1;36mVoltando ao menu...\033[m")
					suspender(1)
					os.system("clear")
					break

				elif user_escolhe == 3:
					print()
					link_post = str(input("\033[1;33m[+]\033[m Url do vídeo: "))
					if validar_links_instagram(links=link_post):
						print()
						fatiar_urls = link_post[28:39]
						post_instagram = Post.from_shortcode(instancia.context, fatiar_urls)
						print("\033[1;31m[+] Iniciando o download da imagem...\n\033[m")
						instancia.download_post(post_instagram,target="Post")
						print("\n\033[1;32m[*] Download completo!")
						print("\033[1;36mVoltando ao menu...\033[m")
						suspender(1)
						os.system("clear")
						break
					else:
						print("\033[1;31m[!] Essa url não é válida ou está quebrada!\033[m")
						suspender(1)
						os.system("clear")

				else:
						print("\033[1;31m[!] Opção inválida!\033[m")
						suspender(1)
						os.system("clear")
			else:
				if user_escolhe == "X" or user_escolhe == "x":
					print("\n\033[1;31mSaindo...\033[m")
					suspender(1)
					sys.exit()
				else:
					print("\033[1;31m[!] Opção inválida!\033[m")
