# Necessário internet
# Ele não deixa rodar o código se não tiver internet

from pytube import YouTube, Playlist
from time import sleep as suspender
import sys
import urllib.request
import os
import banner

print()
os.system("clear")
mensagem_boas_vindas = "Seja bem vindo ao E-tube!"
for letra in mensagem_boas_vindas:
	print("\033[1;36m{}\033[m".format(letra), end='', flush=True)
	suspender(0.1)
suspender(1.1)
os.system("clear")

try:
	print("\033[1;31m[+] Verificando se você está conectado na internet...\033[m")
	suspender(1.4)
	connection = urllib.request.urlopen("https://www.google.com.br")
except:
	print("\n\033[1;31m[ERROR]: Você não está conectado a internet :( \033[m\n")
else:
	os.system("clear")
	while True:
		banner.change_banner()
		print("""

> Meu GitHub: https://github.com/lucas-Dk

MENU:

\033[1;31m[\033[1;32m 1 \033[m\033[1;31m]\033[m - Baixar um vídeo MP4
\033[1;31m[\033[1;32m 2 \033[m\033[1;31m]\033[m - Baixar uma playlist MP4
\033[1;31m[\033[1;32m 3 \033[m\033[1;31m]\033[m - Baixar uma música MP3
\033[1;31m[\033[1;32m 4 \033[m\033[1;31m]\033[m - Mudar cor do banner
\033[1;31m[\033[1;32m 5 \033[m\033[1;31m]\033[m - Fale comigo
\033[1;31m[\033[1;32m x \033[m\033[1;31m]\033[m - Sair
			""")
		try:
			user = input("\n\033[1;33mO que você deseja:\033[m ")
		except KeyboardInterrupt:
			print("\nSaindo...")
			suspender(1)
			sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
		if user.isnumeric():
			user = int(user)
			
			if user == 1:
				print("\n\033[1;32m[+] Opção 1 > Download de um video.mp4\n\033[m")
				print("\033[1;32m[+] O vídeo ficará salvo na pasta do script!\n\033[m")
				try:
					link = str(input("\033[1;33mUrl do vídeo:\033[m "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				url_video = link
				yt = YouTube(url_video)

				print("\n\033[1;31m[+] Buscando streams diponíveis para download...\033[m\n")

				for streams in yt.streams:
					print("\033[1;31m[Vídeo]\033[m \033[1;33m{}\033[m".format(streams))
					suspender(0.5)

				print("\n\033[1;32m[+] Baixando o vídeo com a maior qualidade disponível...\033[m")
				video = yt.streams.get_highest_resolution()
				video.download()
				print("\n\033[1;96m[+] Download completo do vídeo!\033[m")
				print("\n\033[1;35m[+] Voltando ao menu...\n\033[m")
				suspender(2)
				os.system("clear")

			elif user == 2:
				print("\n\033[1;32m[+] Opção 2 > Download de uma Playlist.mp4\033[m\n")
				print("\033[1;32m[+] Os vídeos ficarão salvos na pasta do script!\n\033[m")
				print("\n\033[1;31m[OBS]: Link quebrado = para o download!\033[m\n")
				try:
					link_play = str(input("\033[1;33mUrl do vídeo:\033[m "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				else:
					PLAYLIST_URL = link_play
					playlist = Playlist(PLAYLIST_URL)
					print("\n\033[1;32m[+] Baixando sua playlist...")
					print("[+] Isso pode demorar um pouco...\033[m\n")
					for url in playlist:
						video = YouTube(url)
						stream = video.streams.get_highest_resolution()
						try:
							stream.download(output_path='playlist')
						except:
							print("[ERROR]: Download parado por que encontrei uma url quebrada!")
						else:
							pass
					print("\n\033[1;32m[+] Download Completo da playlist! Verifique na pasta onde se encontra o script!\n\033[m")
					print("\n\033[1;35m[+] Voltando ao menu...\n\033[m")
					suspender(2)
					os.system("clear")

			elif user == 3:
				print("\n\033[1;32m[+] Opção 3 > Download de uma Musica.mp3\033[m\n")
				print("\033[1;32m[+] A música ficará salva na pasta do script!\n\033[m")
				print("\n\033[1;31m[OBS]: Essa opção não converte o vídeo para .MP3")
				print("Apenas baixa somente o audio!\033[m\n")
				try:
					link = str(input("\033[1;33mUrl do vídeo:\033[m "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				else:
					url_download = link
					yt = YouTube(url_download)
					print("\n\033[1;31m[+] Buscando streams diponíveis para download...\033[m\n")
					for streams in yt.streams:
						print("\033[1;31m[Música]\033[m \033[1;33m{}\033[m".format(streams))
						suspender(0.5)
					print("\n\033[1;92m[+] Fazendo o download...\033[m")
					musica = yt.streams.get_highest_resolution()
					try:
						musica.download()
					except:
						print("\n\033[1;31m[OPS]: Ocorreu um erro, verifique o link do vídeo...\033[m")
					else:
						print("\n\033[1;31m[+] Download completo!\033[m\n")
						print("\n\033[1;35m[+] Voltando ao menu...\n\033[m")
						suspender(2)
						os.system("clear")

			elif user == 4:
				os.system("clear")

			elif user == 5:
				os.system("clear")
				print("""
\033[1;33m[+] Para contato:\033[m

---------------------------------------------------------------
\033[1;4mE-mail:\033[m lucas2000bss@gmail.com
\033[1;4mFacebook:\033[m https://www.facebook.com/Walker.Lxrd/
---------------------------------------------------------------

[+] Fale comigo por uma dessas redes e terá contato comigo
				""")
				try:
					input("Dê enter para voltar ao menu... ")
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				os.system("clear")
			else:
				print("\033[1;31mOpção inválida! Tente novamente.\033[m")
				suspender(0.8)
				os.system("clear")

		elif user == 'X' or user == 'x':
			print("Saindo...")
			suspender(1)
			sys.exit()

		else:
			print("\033[1;31mOpção inválida! Tente novamente.\033[m")
			suspender(0.8)
			os.system("clear")

# Fim do script
