# Autor: Nano-9                                                             |
# Meu github: https://github.com/nano-9                                     |
# Meu Telegram: https://t.me/rdzin9                                         |     \
# ////                                                                              By: Nano-9 E-tube
# Necessário internet                                                       |     /
# Ele não deixa rodar o código se não tiver internet                        |
# Meu telegram, copie esse código e cole no navegador: https://t.me/rdzin9  |

try:
	import sys
	from pytubefix import YouTube, Playlist
	from time import sleep as suspender
	import urllib.request
	import os
	import pafy
	import banner
	import re
	import instaloader
	import pyinsdownloader
	import downface
	import requests
	from bs4 import BeautifulSoup
	from historico import *
	from convertervp3 import *
	from time import strftime
	import moviepy.editor as mp
	from moviepy.video.fx.all import crop
	from pathlib import Path
	import datetime
except Exception as E:
	
	print(E)
	print("\n\033[1;31m[ERROR]: Ops aconteceu algo inesperado! Siga as instruções abaixo:\033[m")
	print("\n\033[1;33m[*] Digite esse comando:\033[m pip install -r requirements.txt")
	print("\n\033[1;33m[*] Digite esse comando:\033[m python3 setup.py")
	print("\n\033[1;31mE tente novamente!\033[m")
	sys.exit()
else:
	pass
print()
arquivo = "links"
if not existe(arquivo):
	criar(arquivo)
if existe(arquivo) == True:
	pass

#eventos
os.makedirs("Seus_GIFs",exist_ok=True)
os.makedirs("ImagensGoogle",exist_ok=True)
header = {"User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; SM-J250M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36"}
buscar_google = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"


previousprogress = 0
def validar_caminho(caminho):
	if "\\" in caminho:
		valid = re.search(r"^(?=\\([a-zA-Z0-9_\-\\\s]*)(\\)$)",caminho)
		return valid
	elif "/" in caminho:
		valid = re.search(r"^(?=\/([a-zA-Z0-9\/_\-\s]*)(\/)$)",caminho)
		return valid


def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        bytes_archive = int(bytes_remaining)
        print("\033[1;34m[+] Baixando:\033[m [{}]% | [{}] \033[1;34mMib/s\033[m \033[1;32mconcluído\033[m".format(liveprogress,bytes_archive))

os.system("clear")
mensagem_boas_vindas = "Seja bem vindo ao E-tube!"
for letra in mensagem_boas_vindas:
	print("\033[1;36m{}\033[m".format(letra), end='', flush=True)
	suspender(0.1)
suspender(0.4)
os.system("clear")

try:
	print("\033[1;31m[!] Verificando se você está conectado na internet...\033[m")
	suspender(1.4)
	connection = urllib.request.urlopen("https://www.google.com.br")
except:
	print("\n\033[1;31m[ERROR]: Você não está conectado a internet :( \033[m\n")
else:
	os.system("chmod + e-tube.py")
	os.system("clear")
	while True:
		banner.change_banner()
		print("""
.----------------------------.
| Teleg: https://t.me/rdzin9 |
'----------------------------'
    ^      (\_/) \033[1;32m[INFO]\033[m Coded by: Nano-9
    '----- (O.o) \033[1;32m[INFO]\033[m Meu GitHub: https://github.com/nano-9
           (> <) \033[1;32m[INFO]\033[m Reporte erros: https://t.me/rdzin9

MENU:

\033[1;31m[\033[1;32m 01 \033[m\033[1;31m]\033[m - Baixar um vídeo MP4
\033[1;31m[\033[1;32m 02 \033[m\033[1;31m]\033[m - Baixar uma playlist MP4
\033[1;31m[\033[1;32m 03 \033[m\033[1;31m]\033[m - Baixar uma música MP3
\033[1;31m[\033[1;32m 04 \033[m\033[1;31m]\033[m - Baixar vídeos/fotos do instagram
\033[1;31m[\033[1;32m 05 \033[m\033[1;31m]\033[m - Baixar vídeos do Facebook
\033[1;31m[\033[1;32m 06 \033[m\033[1;31m]\033[m - Converter vídeos para MP3
\033[1;31m[\033[1;32m 07 \033[m\033[1;31m]\033[m - Cortar vídeos
\033[1;31m[\033[1;32m 08 \033[m\033[1;31m]\033[m - Criar um GIF
\033[1;31m[\033[1;32m 09 \033[m\033[1;31m]\033[m - Baixar imagens do Google
\033[1;31m[\033[1;32m 10 \033[m\033[1;31m]\033[m - Mudar cor do banner
\033[1;31m[\033[1;32m 11 \033[m\033[1;31m]\033[m - Reparar erros do script
\033[1;31m[\033[1;32m 12 \033[m\033[1;31m]\033[m - Fale comigo
\033[1;31m[\033[1;32m xx \033[m\033[1;31m]\033[m - Sair
			""")
		try:
			user = input("\n\033[1;33mO que você deseja:\033[m ")
		except KeyboardInterrupt:
			print("\nSaindo...")
			suspender(1)
			sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
		else:
			
			if user == "01" or user == "1":

				print()
				print("\033[1;32m[+] Opção 1 > Download de um video.mp4\033[m")
				print("\033[1;32m[+] O vídeo ficará salvo na pasta do script!\033[m")
				print()

				print("""
########## Formas de download: ##########
\033[1;33m
[1] Pafy
[2] Pytube\033[m\n""")
				try:
					tecle = str(input("\033[1;32m[+] Com qual forma de download você deseja continuar: \033[m"))
					print()
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()
				else:
					if tecle.isnumeric():
						tecle = int(tecle)
						os.makedirs("Videos_pafy",exist_ok=True)
						if tecle == 1:
							if sys.platform == "win32":

								local = Path.home() / r"Downloads\E-tube"

								print("\033[1;32m[+] Você escolheu baixar com o Pafy!")
								print("O vídeo será salvo dentro da pasta: Videos_pafy\033[m\n")
								link_video_youtube = str(input("\033[1;32m[+] Link do vídeo: \033[m")).strip()

								video_tube = pafy.new(link_video_youtube)
								stream = video_tube.streams
								videos_info = video_tube.getbest()

								print("\n\033[1;33m[*] Fazendo download do vídeo: [{}]\n".format(video_tube.title))
								os.chdir(local)
								os.chdir("Videos_pafy")
								with open("Videos_pafy", "wb") as play_video:
									os.path.join("Videos_pafy" + "/" + str(videos_info.download()))
									play_video.close()
								for arquivo in os.listdir(str(local)+"\\Videos_pafy"):
									if arquivo.endswith(".mp4"):
										pass
									else:
										os.remove(arquivo)

								print("\n\033[1;32m[*] Download completo")
								suspender(1.3)
								
								os.system("clear")

							elif sys.platform == "linux":

								local = Path.home() / "Downloads/E-tube"

								print("\033[1;32m[+] Você escolheu baixar com o Pafy!")
								print("O vídeo será salvo dentro da pasta: Videos_pafy\033[m\n")
								link_video_youtube = str(input("\033[1;32m[+] Link do vídeo: \033[m")).strip()

								video_tube = pafy.new(link_video_youtube)
								stream = video_tube.streams
								videos_info = video_tube.getbest()

								print("\n\033[1;33m[*] Fazendo download do vídeo: [{}]\n".format(video_tube.title))
								os.chdir(local)
								os.chdir("Videos_pafy")
								with open("Videos_pafy", "wb") as play_video:
									os.path.join("Videos_pafy" + "/" + str(videos_info.download()))
									play_video.close()
								for arquivo in os.listdir(str(local)+"/Videos_pafy"):
									if arquivo.endswith(".mp4"):
										pass
									else:
										os.remove(arquivo)
								print("\n\033[1;32m[*] Download completo")
								suspender(1.3)

						elif tecle == 2:
							try:
								link = str(input("\033[1;33mUrl do vídeo:\033[m "))
								adicionar_links(arq=arquivo,dados=link,arg="[LINKS DE VIDEOS]")
							except KeyboardInterrupt:
								print("\nSaindo...")
								suspender(1)
								sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
							url_video = link
							yt = YouTube(url_video)

							print("\n\033[1;31m[!] Buscando streams diponíveis para download...\033[m\n")

							for streams in yt.streams.filter(file_extension="mp4"):
								print("\033[1;31m[Vídeo]\033[m \033[1;33m{}\033[m".format(streams))
								suspender(0.5)

							print("\n\033[1;32m[+] Iniciando o download...\033[m")
							try:
								video = yt.streams.get_highest_resolution()
								yt.register_on_progress_callback(on_progress)
								video.download(output_path="Videos-baixados")
							except VideoUnavailable:
								print("\033[1;31mO vídeo:\033[m [{}] \033[1;31mse encontra indísponivel para download...\033[m ")
							except KeyboardInterrupt:
								print("\033[1;31m[OPS]: Ocorreu alguma interrupção! Fechando o script...\033[m")
								suspender(1)
								sys.exit()

							print("\n\033[1;96m[!] Download completo do vídeo!\033[m")
							print("\033[1;35m[+] Voltando ao menu...\033[m")
							suspender(2)
							os.system("clear")

			elif user == "02" or user == "2":

				print()
				print("\033[1;32m[+] Opção 2 > Download de uma Playlist.mp4\033[m")
				print("\033[1;32m[+] Os vídeos ficarão salvos na pasta 'playlist' do script!\n\033[m")
				print()

				print("""
########## Formas de download: ##########
\033[1;33m
[1] Pafy
[2] Pytube\033[m\n""")
				try:
					informar = str(input("\033[1;32m[+] Com qual forma de download você deseja continuar: \033[m"))
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit()
				else:

					if informar == "1":
						if sys.platform == "win32":

							os.makedirs("Videos_pafy",exist_ok=True)
							local_playlist = Path.home() / r"Downloads\E-tube"
							print("\033[1;32m[+] Opção de baixar com Pafy! O vídeo ficará salvo na pasta: Video_pafy\033[m")

							nome = str(input("\n\033[1;33m[+] Nome para a sua playlist: ")).strip()
							quantidade = str(input("\033[1;33m[+] Quantos vídeos você deseja baixar de uma vez: \033[m"))
							nome_playlist = nome+".txt"

							print()
							for links in range(int(quantidade)):
								link = str(input("\033[1;33m[+] Link do vídeo: ")).strip()
								with open(nome_playlist,"at") as file:
									file.write(f"{link}\n")
							print()
							for arquivo in os.listdir(str(local_playlist)):
								if arquivo.startswith(nome):
									with open(arquivo,"rt") as youtube_links:
										resultado = youtube_links.readlines()
										for links_arqv in resultado:
											video_youtube = pafy.new(links_arqv)
											stream = video_youtube.streams
											baixar = video_youtube.getbest()

											os.chdir(local_playlist)
											os.chdir("Videos_pafy")

											print("\n------------------------------------------------")
											print("\033[1;36mINFORMAÇÕES SOBRE O VÍDEO:\033[m {}\n".format(video_youtube.title))
											print(f"""
\033[1;33mTítulo do vídeo:\033[m {video_youtube.title}
\033[1;33mDuração do vídeo:\033[m {video_youtube.duration}
\033[1;33mAutor do vídeo:\033[m {video_youtube.author}
\033[1;33mQuantidade de likes:\033[m {video_youtube.likes}
\033[1;33mQuantidade de visualizações:\033[m {video_youtube.viewcount}
	""")
											with open("Videos_pafy","wb") as videos_t:
												os.path.join("Videos_pafy" + "/" + str(baixar.download())).strip()
												videos_t.close()
											print("------------------------------------------------")
									os.chdir(local_playlist)
									os.chdir("Videos_pafy")

									for naovideo in os.listdir(str(local_playlist)+"\\Videos_pafy"):
										if naovideo.endswith(".mp4"):
											pass
										else:
											os.remove(naovideo)

							os.chdir(local_playlist)

							for arqvs in os.listdir(str(local_playlist)):
								if arqvs.endswith(".txt"):
									if arqvs == "requirements.txt":
										pass
									else:
										os.remove(arqvs)
						elif sys.plaform == "linux":

							os.makedirs("Videos_pafy",exist_ok=True)
							local_playlist = Path.home() / "Downloads/E-tube"
							local_playlist2 = Path.home() / "Downloads/E-tube/Videos_pafy"
							print("\033[1;32m[+] Opção de baixar com Pafy! O vídeo ficará salvo na pasta: Video_pafy\033[m")

							nome = str(input("\n\033[1;33m[+] Nome para a sua playlist: ")).strip()
							quantidade = str(input("\033[1;33m[+] Quantos vídeos você deseja baixar de uma vez: \033[m"))
							nome_playlist = nome+".txt"

							print()
							for links in range(int(quantidade)):
								link = str(input("\033[1;33m[+] Link do vídeo: ")).strip()
								with open(nome_playlist,"at") as file:
									file.write(f"{link}\n")
							print()
							for arquivo in os.listdir(str(local_playlist)):
								if arquivo.startswith(nome):
									with open(arquivo,"rt") as youtube_links:
										resultado = youtube_links.readlines()
										for links_arqv in resultado:
											video_youtube = pafy.new(links_arqv)
											stream = video_youtube.streams
											baixar = video_youtube.getbest()

											os.chdir(local_playlist)
											os.chdir("Videos_pafy")

											print("\n------------------------------------------------")
											print("\033[1;36mINFORMAÇÕES SOBRE O VÍDEO:\033[m {}\n".format(video_youtube.title))
											print(f"""
\033[1;33mTítulo do vídeo:\033[m {video_youtube.title}
\033[1;33mDuração do vídeo:\033[m {video_youtube.duration}
\033[1;33mAutor do vídeo:\033[m {video_youtube.author}
\033[1;33mQuantidade de likes:\033[m {video_youtube.likes}
\033[1;33mQuantidade de visualizações:\033[m {video_youtube.viewcount}
	""")
											with open("Videos_pafy","wb") as videos_t:
												os.path.join("Videos_pafy" + "/" + str(baixar.download())).strip()
												videos_t.close()
											print("------------------------------------------------")
									os.chdir(local_playlist)
									os.chdir("Videos_pafy")

									for naovideo in os.listdir(str(local_playlist)+"/Videos_pafy"):
										if naovideo.endswith(".mp4"):
											pass
										else:
											os.remove(naovideo)

							os.chdir(local_playlist)

							for arqvs in os.listdir(str(local_playlist)):
								if arqvs.endswith(".txt"):
									if arqvs == "requirements.txt":
										pass
									else:
										os.remove(arqvs)

					elif informar == "2":
						try:
							link_play = str(input("\033[1;33mUrl da playlist:\033[m "))
							adicionar_links(arq=arquivo,dados=link_play,arg="[LINKS DAS PLAYLISTS]")
						except KeyboardInterrupt:
							print("\nSaindo...")
							suspender(1)
							sys.exit()# Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
						else:
							PLAYLIST_URL = link_play
							playlist = Playlist(PLAYLIST_URL)
							tamanho_da_playlist = 0
							for videos in playlist:
								tamanho_da_playlist += 1
							print()
							print("\n\033[1;32mSobre a sua playlist:\033[m\n")
							print("\033[1;31m[*] Nome:\033[m {}".format(playlist.title))
							print("\033[1;31m[*] Tamanho da sua playlist:\033[m {} \033[1;31mvídeos!\033[m".format(tamanho_da_playlist))
							print("\033[1;31m[*] link quebrado:\033[m o vídeo é pulado!")
							print("\033[1;31m[*] Local de armazenamento:\033[m pasta playlist")
							print()
							print("\033[1;92m[+] Iniciando o download dos vídeos...\033[m\n")
							tamanho_da_playlist = 0
							for numero_play, url in enumerate(playlist):
								print("\033[1;33m[+] Baixando o [{}]º video:\033[m {}".format(numero_play+1,url))
								video = YouTube(url)
								stream = video.streams.get_highest_resolution()
								print("\033[1;31mStatus:\033[m \033[1;32m[COMPLETO]\033[m")
								try:
									stream.download(output_path="playlist")
								except VideoUnavailable:
									print("\033[1;31mStatus:\033[m \033[1;33m[PULADO]\033[m")
									print("\n\033[1;91mO video foi pulado porque o o link está quebrado!\033[m")
									time.sleep(2)
								except KeyboardInterrupt:
									print("\n\033[m[ERROR]: Download quebrado porque o usuário saiu!\033[m")
								else:
									pass
							convertermp3 = str(input("\033[1;32m[+] Deseja converter todos os vídeos da playlist para o formato MP3? [S/N]:\033[m ")).upper()
							while convertermp3 not in "S" and convertermp3 not in "N":
								convertermp3 = str(input("\033[1;32m[+] Deseja converter todos os vídeos da playlist para o formato MP3? [S/N]:\033[m ")).upper()
							if convertermp3 == "S":
								converter_video_para_mp3(fun="cheio")
							elif convertermp3 == "N":
								print("\n\033[1;32m[!] Download Completo da playlist! Verifique na pasta: Playlist YT !\n\033[m")
								print("\n\033[1;35m[+] Voltando ao menu...\n\033[m")
								suspender(2)
								os.system("clear")
							else:
								print("\033[1;31m[!] Opção vazia não é permitida!\033[m")
								suspender(2)
								os.system("clear")
			elif user == "03" or user == "3":

				print("\n\033[1;32m[+] Opção 3 > Download de uma Musica.mp3\033[m")
				print("\033[1;32m[+] Os vídeos que serão convertidos para um MP3 ficarão dentro da pasta > VideosConvertidos\033[m")
				print("\033[1;32m[+] O áudio.mp3 que foi feito do vídeo, ficará salvo fora das pastas mas dentro da pasta E-tube\n\033[m")
				try:
					link = str(input("\033[1;33mUrl do vídeo:\033[m "))
					adicionar_links(arq=arquivo,dados=link,arg="[LINKS DE VIDEOS]")
				except KeyboardInterrupt:
					print("\nSaindo...")
					suspender(1)
					sys.exit() # Essa linha não seria necessária, mas se ocorrer um bug inesperado, ela sai do programa
				else:
					url_download = link
					yt = YouTube(url_download)
					print("\n\033[1;31m[!] Buscando streams diponíveis para download...\033[m\n")
					for streams in yt.streams.filter(only_audio=True):
						print("\033[1;31m[Música]\033[m \033[1;33m{}\033[m".format(streams))
						suspender(0.5)
					print("\n\033[1;92m[+] Fazendo o download...\033[m")
					try:
						musica = yt.streams.get_highest_resolution()
						yt.register_on_progress_callback(on_progress)
						musica.download(output_path="VideosConvertidos")
					except:
						print("\033[1;31m[OPS]: Ocorreu alguma interrupção! Verifique se está tudo bem com a sua")
						print("conexão com a internet e tente novamente! Caso persista esse erro, acione a opção 5.\033[m")
						print("\n\033[1;31mFechando o script...\033[m")
						suspender(1)
						sys.exit()
					else:
						print("\n\033[1;32m[!] Download completo!\033[m\n")
						try:
							converte = str(input("\033[1;33mDeseja converter esse vídeo para .mp3? [Y/N]:\033[m ")).upper()[0]
							while converte not in "Y" and converte not in "N":
								print("\033[1;31m[ERROR]:\033[m Por favor, digite uma opção válida!")
								converte = str(input("\033[1;33m[!] Deseja converter esse vídeo para .mp3? [Y/N]:\033[m ")).upper()[0]
						except IndexError:
								print("\033[1;91m[ATENÇÃO]: Essa opção não pode ficar vazia! Tente novamente!\033[m")
								print("\n\033[1;31mSaindo...\033[m\n")
								suspender(0.5)
								sys.exit()
						else:
							if converte == "Y":
								converter_video_para_mp3()
							elif converte == "N":
								print("\n\033[1;35m[+] Voltando ao menu...\n\033[m")
								suspender(2)
								os.system("clear")
			elif user == "04" or user == "4":
				print()
				print("\033[1;32m[+] Opção 4 > Download de vídeos/fotos do instagram!\033[m")
				print("\033[1;32m[+] O vídeo ficará salvo na pasta do script!\033[m\n")
				print()
				suspender(2)
				pyinsdownloader.baixar_videos_instagram()

			elif user == "05" or user == "5":
				print()
				print("\033[1;32m[+] Opção 5 > Download de um video.mp4 do facebook\033[m")
				print("\033[1;32m[+] O vídeo ficará salvo na pasta do script!\033[m")
				print()
				print("\033[1;34m[+] Opção de download iniciada!\033[m\n")
				suspender(2.2)
				downface.iniciar_download()
				os.system("clear")

			elif user == "06" or user == "6":
				print()
				print("\033[1;32m[+] Opção de conversão de vídeos para MP3!\n\033[m")
				print("\033[1;33m[!] Essa opção armazena os vídeos na pasta do script!\033[m")
				print("\033[1;33m[+] Exemplo de caminho a ser colocado abaixo:\033[m " + r"\Users\Cliente\Downloads\Musicas\n")

				try:
					print()
					caminho1 = input("\033[1;32m[*] Informe o caminho onde os vídeos estão:\033[m ").strip()
					while not validar_caminho(caminho1):
						if sys.platform == "win32":
							print("\033[1;31m[!] Está faltando uma contra barra -> \\ adicione ela ao final do caminho!\033[m")
							caminho1 = input("\033[1;32m[*] Informe o caminho onde os vídeos estão:\033[m ").strip()
						elif sys.platform == "linux":
							print("\033[1;31m[!] Está faltando uma barra -> / adicione ela ao final do caminho!\033[m")
							caminho1 = input("\033[1;32m[*] Informe o caminho onde os vídeos estão:\033[m ").strip()
				except FileNotFoundError:
					print("\033[1;31m[ERROR] Não foi possível localizar esse caminho:\033[m {}\n".format(caminho1))
				else:
					correto1 = input("\033[1;36m[!] Esse caminho está correto? [S/N]:\033[m ").strip().upper()
					while correto1 not in "S" and correto1 not in "N":
						correto1 = input("\033[1;36m[!] Esse caminho está correto? [S/N]:\033[m ").strip().upper()
					if correto1 == "S":
						tipo = input("\033[1;33m[+] Qual a extensão dos vídeos [.mp4/.webm/.mov ...]:\033[m ").strip().lower()
						while "." not in tipo:
							print("\033[1;31m[!] Coloque um . antes da extensão!\033[m")
							tipo = input("\033[1;33m[+] Qual a extensão dos vídes [.mp4/.webm/.mov ...]:\033[m ").strip().lower()
						hora_start = strftime("%H:%M:%S")
						start = datetime.datetime.now()
						print("\n\033[1;32m[*] Conversão iniciada as:\033[m [{}]\n".format(hora_start))
						for item in os.listdir(str(caminho1)):
							if item.endswith(str(tipo)):
									seuvideo1 = item
									seuvideo2 = caminho1 + seuvideo1
									seuvideo3 = item.replace(tipo,".mp3")
									convert = mp.VideoFileClip(seuvideo2)
									if convert:
										try:
											os.chdir("SUAS_MÚSICAS")
											os.path.join("SUAS_MÚSICAS" + "/" + str(convert.audio.write_audiofile(seuvideo3)))
										except:
											os.path.join("SUAS_MÚSICAS" + "/" + str(convert.audio.write_audiofile(seuvideo3)))
						finish = datetime.datetime.now() - start
						tempo = str(finish)
						print("\n\033[1;36m[+] Abaixo está o tempo que o programa levou para converter:\033[m")
						print("\033[1;32m[*] Conversão finalizada com:\033[m [{}]".format(tempo[0:7]))
						print("\n\033[1;36m[+] Voltando ao menu...\033[m")
						suspender(1.3)
						os.system("clear")
					
			elif user == "07" or user == "7":
				os.makedirs("Videos_cortados",exist_ok=True)
				def minuto_para_segundo(minuto_video):
					separar_minuto = minuto_video.split(":")
					minuto = int(separar_minuto[0])
					segundo = int(separar_minuto[1])

					cortar_video_segundo = (minuto * 60) + segundo
					return cortar_video_segundo

				caminho_video = str(input("[+] Informe o caminho do vídeo: ")).strip()
				while not validar_caminho(caminho=caminho_video):
					if sys.platform == "win32":
						print("\033[1;31m[ATENÇÃO]:\033[m Está faltando uma contra barra -> \\ no final do caminho!")
					elif sys.platform == "linux":
						print("\033[1;31m[ATENÇÃO]:\033[m Está faltando uma barra -> / no final do caminho!")
					caminho_video = str(input("[+] Informe o caminho do vídeo: ")).strip()

				nome_video = str(input("[+] Informe o nome do vídeo e sua extensão. Ex: [VIDEO.MP4]: ")).strip()

				arquivos_video = mp.VideoFileClip(caminho_video+nome_video)
				minuto_inicial = str(input("[+] Informe o minuto inicial para cortar o vídeo. Ex: [01:10]: ")).strip()
				minuto_final = str(input("[+] Informe o minuto final para cortar o vídeo. Ex: [01:20]: ")).strip()

				minuto_inicio = minuto_para_segundo(minuto_video=minuto_inicial)
				minuto_fim = minuto_para_segundo(minuto_video=minuto_final)

				cortar_video = arquivos_video.subclip(minuto_inicio,minuto_fim)
				os.chdir("Videos_cortados")
				os.path.join("Videos_cortados"+"/"+str(cortar_video.write_videofile("cortado"+nome_video)))
				print("Vídeo cortado com sucesso, salvo em -> Videos_cortados")
				suspender(2)
				os.system("clear")

			elif user == "08" or user == "8":
				print("\n\033[1;32m[+] Opção de criação de GIF!")
				print("[+] O GIF é armazenado na pasta do E-tube.\033[m")
				print()
				caminho = str(input("\033[1;32m[+] Informe o caminho onde está(ão) o(s) vídeo(s):\033[m ")).strip()
				while not validar_caminho(caminho=caminho):
					print("\033[1;32m[!] Está faltando uma contra barra -> \\ adicione ao final do caminho!\033[m")
					caminho = str(input("\033[1;32m[+] Informe o caminho onde está(ão) o(s) vídeo(s):\033[m ")).strip()
				extensao = str(input("\033[1;32m[+] Extensão do(s) vídeo(s) [.mp4/.webm/.wmv ...]:\033[m ")).strip().lower()
				while "." not in extensao:
					print("\033[1;31m[!] Coloque um . no começo da extensão do arquivo!\033[m")
					extensao = str(input("\033[1;32m[+] Extensão do(s) vídeo(s) [.mp4/.webm/.wmv ...]:\033[m ")).strip().lower()
				partir_de = int(input("\033[1;32m[+] Informe o minuto/segundo para começar:\033[m "))
				parar_no = int(input("\033[1;32m[+] Informe o minuto/segundo para parar:\033[m "))
				larguragif = int(input("\033[1;32m[+] Informe a largura que deseja o GIF:\033[m "))
				alturagif = int(input("\033[1;32m[+] Informe a altura que deseja o GIF:\033[m "))
				print()
				hora = strftime("%H:%M:%S")
				print("\033[1;32m[*] Criação do GIF iniciada as:\033[m {}\n".format(hora))
				start = datetime.datetime.now()
				for item in os.listdir(str(caminho)):
					if item.endswith(str(extensao)):
						receberarquivo = item
						concatenararqv = caminho + receberarquivo
						saidaemgifarqv = receberarquivo.replace(extensao,".gif")
						dadosdoarquivo = mp.VideoFileClip(concatenararqv)
						fpsdoarquivogf = dadosdoarquivo.reader.fps
						try:
							os.chdir("Seus_GIFs")
							gerandoogifarq = dadosdoarquivo.subclip(partir_de,parar_no)
							gerandoogifarq = gerandoogifarq.resize(width=larguragif,height=alturagif)
							os.path.join("Seus_GIFs" + "/" + str(gerandoogifarq.write_gif(saidaemgifarqv)))
						except:
							os.path.join("Seus_GIFs" + "/" + str(gerandoogifarq.write_gif(saidaemgifarqv)))
				finish = datetime.datetime.now() - start
				endfun = str(finish)
				print("\033[1;32m[*] Criação de GIF concluída!\033[m")
				print("\033[1;36m[+] Tempo que levou para criar o seu GIF:\033[m {}".format(endfun[0:7]))
				suspender(2)
				os.system("clear")

			elif user == "09" or user == "9":
				horario = strftime("%H:%M:%S")
				starting = datetime.datetime.now()
				print("\n\033[1;32m[+] Opção de baixar imagens do Google!")
				print("[+] O download da imagem fica salvo na pasta:\033[m ImagensGoogle\n")

				evento = requests.Session()

				evento_pesquisar = str(input("\033[1;36m[+] O que deseja pesquisar:\033[m ")).capitalize()
				print()
				print("\033[1;32m[*] Download iniciado!\n\033[m")
				evento_google = buscar_google + "q=" + evento_pesquisar
				evento_informacoes = evento.get(evento_google, headers=header)

				if evento_informacoes.status_code == 200:

					evento_html = evento_informacoes.text
					html_soup = BeautifulSoup(evento_html,"html.parser")
					evento_de_busca = html_soup.find_all("img",{"class":"rg_i Q4LuWd"})
					if evento_de_busca:
						imagem_nomes = []
						for links in evento_de_busca:
							armazenamento = links.get("data-src")
							if armazenamento != None:
								imagem_nomes.append(armazenamento)
						for indice, buscas in enumerate(imagem_nomes):
							print("\033[1;34m[{}]\033[m \033[1;32m[info]\033[m Download da {}ª imagem: {}.jpg".format(horario,indice+1,evento_pesquisar))
							evento_download_bytes = evento.get(buscas)
							evento_salvar_fotos = os.path.join("ImagensGoogle" + "/" + evento_pesquisar + str(indice+1) + ".jpg")
							with open(evento_salvar_fotos,"wb") as file:
								file.write(evento_download_bytes.content)
								file.close()
						finish = datetime.datetime.now() - starting
						finishing = str(finish)
						print("\n\033[1;32m[*] Download completo!")
						print("[+] Tempo que o programa fez o download:\033[m {}\n".format(finishing[0:7]))
						print("\033[1;34m[+] Voltando ao menu...\033[m")
						suspender(2.2)
						os.system("clear")

			elif user == "10":
				os.system("clear")
				
			elif user == "11":
				sistema = sys.platform
				if sistema == "Linux" or "Linux2":
					print()
					print("\033[1;32m[+] Opção 7 > Reparo do script automático!\033[m")
					print()
					print("\n\033[1;32m[!] Atenção: Caso o erro continue entre em contato comigo:\033[m ")
					print("> https://t.me/rdzin9\n ")
					try:
						seguir_reparo = str(input("\033[1;33m[!] Enter para seguir com o reparo:\033[m "))
					except KeyboardInterrupt:
						print("\n\033[1;31m[!] Saindo...\033[m")
						suspender(1)
						sys.exit()

					else:
						os.system("clear")
						# comandos para reparar o erro do E-tube
						print("\n\033[1;31m[+] Reparando o script...\033[m\n")

						os.system("pip install --upgrade pip")
						os.system("pip uninstall pytube -y")
						os.system("pip install -r requirements.txt")

						print("\n\033[1;32m[!] Reparação completa!\033[m")
						print("\033[1;32m[+] Abrindo o E-tube...\033[m")
						suspender(1.4)
						os.system("clear")
				else:
					print("\033[1;31m[!] Desculpe! O seu sistema pode apresentar falhas com esse patch\033[m")
					print("\033[1;33m[!] Entre em contato comigo e irei resolver:\033[m https://t.me/rdzin9\n")
					sys.exit()

			elif user == "12":
				print()
				print("""
\n\033[1;33m[+] Para contato:\033[m
---------------------------------------------------------------
\033[1;4mTelegram:\033[m https://t.me/rdzin9
\033[1;4mInstagram:\033[m @nanoxsec
---------------------------------------------------------------
\033[1;92m[+] Fale comigo por uma dessas redes e terá contato comigo\n\033[m
				""")

				try:
					back_menu = input("Enter para voltar ao menu: ")
					os.system("clear")

				except KeyboardInterrupt:
					print("\n\033[1;31mSaindo...\033[m")
					suspender(1)
					sys.exit()
				else:
					pass


			elif user == 'X' or user == 'x' or user == "XX" or user == "xx":
				print("Saindo...")
				suspender(1)
				sys.exit()

			else:
				print("\033[1;31mOpção inválida! Tente novamente.\033[m")
				suspender(0.8)
				os.system("clear")
# Fim do script
