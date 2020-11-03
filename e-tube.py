# Necessário internet
# Ele não deixa rodar o código se não tiver internet

from pytube import YouTube, Playlist
from time import sleep as suspender
import sys
import urllib.request
import os
import banner

mensagem_boas_vindas = "Seja bem vindo ao E-tube!"
for letra in mensagem_boas_vindas:
	print(letra, end='', flush=True)
	suspender(0.1)
os.system("clear")

try:
	print("\033[1;31mVerificando se você está conectado na internet...\033[m")
	suspender(1.2)
	connection = urllib.request.urlopen("https://www.google.com.br")
except:
	print("\n\033[1;31mERROR: Você não está conectado a internet :( \033[m\n")
else:
	os.system("clear")
	while True:
		banner.change_banner()
		print("""
Menu:

\033[1;31m[\033[1;32m1\033[m\033[1;31m]\033[m - Baixar um vídeo MP4
\033[1;31m[\033[1;32m2\033[m\033[1;31m]\033[m - Baixar uma playlist MP4
\033[1;31m[\033[1;32m3\033[m\033[1;31m]\033[m - Baixar uma música MP3
\033[1;31m[\033[1;32m4\033[m\033[1;31m]\033[m - Mudar cor do banner
\033[1;31m[\033[1;32m5\033[m\033[1;31m]\033[m - Fale comigo
\033[1;31m[\033[1;32mx\033[m\033[1;31m]\033[m - Sair
			""")
		try:
			user = input("Faça sua escolha: ")
		except KeyboardInterrupt:
			print("\nSaindo...")
			suspender(1)
			sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
		if user.isnumeric():
			user = int(user)
			
			if user == 1:

				print("\nOpção de baixar apenas um vídeo está executando...\n")
				try:
					link = str(input("Url do vídeo: "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				print("Buscando streams...")
				url_video = link
				yt = YouTube(url_video)

				print("\033[1;31mMostrando todas as streams disponivel para download...\n")
				print("Buscando a melhor e baixando a mesma...\033[m\n")

				for streams in yt.streams:
					print(streams)
					suspender(0.6)

				print("\033[1;32mFazendo download da stream com a melhor qualidade disponível...\033[m")
				video = yt.streams.get_highest_resolution()
				video.download()
				print("\nDownload completo do vídeo! Verifique na pasta onde se encontra o script!")
				print("Voltando ao menu...\n")
				suspender(1.3)

			elif user == 2:
				print("\nOpção de baixar uma playlist está executando...\n")

				print("\033[1;31mOBS: Confira se nenhum link está quebrado para que o download ocorra corretamente!\033[m\n")
				print("\033[1;4mO que acontece se tiver um link quebrado?\033[m\n")
				print("Ele vai baixando video por vídeo, quando chegar no video")
				print("com a url quebrada, ele para de baixar os vídeos!\n")
				input("Se entendeu dê enter para continuar")
				print() # Espaço
				try:
					link_play = str(input("Url da playlist: "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				else:
					PLAYLIST_URL = link_play
					playlist = Playlist(PLAYLIST_URL)
					print("\n\033[1;32mBaixando sua playlist!")
					print("Isso pode demorar um pouco...\033[m\n")
					for url in playlist:
						video = YouTube(url)
						stream = video.streams.get_highest_resolution()
						try:
							stream.download(output_path='playlist')
						except:
							print("ERROR: Download quebrado por que encontrei uma url quebrada!")
						else:
							pass
					print("\nDownload Completo da playlist! Verifique na pasta onde se encontra o script!\n")
					suspender(1.6)

			elif user == 3:
				print("\nVocê escolheu a opção de baixar uma música!")
				print("\n\033[1;4mOBS\033[m: Essa opção não converte o vídeo para .MP3")
				print("apenas baixa somente o audio!\n")
				try:
					link = str(input("Url do vídeo: "))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				else:
					url_download = link
					yt = YouTube(url_download)
					print("\n\033[1;31mBuscando streams correspondentes...\033[m")
					for streams in yt.streams:
						print(streams)
						suspender(1)
					print("\n\033[1;92mFazendo o download....")
					musica = yt.streams.get_highest_resolution()
					try:
						musica.download()
					except:
						print("Ocorreu um erro, verifique o link do video...")
					else:
						print("\nDownload completo\033[m\n")
						print("Voltando ao menu...")
						suspender(1)
						os.system("clear")

			elif user == 4:
				os.system("clear")

			elif user == 5:
				os.system("clear")
				print("""
Para contato:
---------------------------------------------------------------
\033[1;4mE-mail:\033[m lucas2000bss@gmail.com
\033[1;4mFacebook:\033[m https://www.facebook.com/Walker.Lxrd/
---------------------------------------------------------------

fale comigo por uma dessas redes e terá contato comigo
				""")
				try:
					input("Dê enter para voltar ao menu... ")
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				os.system("clear")
			else:
				print("Opção inválida! Tente novamente.")
				suspender(0.8)
				os.system("clear")

		elif user == 'X' or user == 'x':
			print("Saindo...")
			suspender(1)
			sys.exit()

		else:
			print("Opção inválida! Tente novamente.")
			suspender(0.8)
			os.system("clear")

# Fim do script
