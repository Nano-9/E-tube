import moviepy.editor as mp
import os

def converter_video_para_mp3():
	os.system("clear")
	print("=========================== CONVERTER PARA MP3 ===========================")
	print("\n\033[1;33m[SAIBA UTILIZAR ESSA FUNÇÃO LEIA ABAIXO]\033[m")
	print("\n\033[1;32m[+] Para converter o video para mp3 siga as instruções:\033[m\n")
	print("\033[1;32m[+] Pegue o caminho onde se encontra o vídeo. Exemplos:\033[m")
	print("\n----------------\n")
	print("\033[1;33m[+]\033[m Termux: /storage/downloads/E-tube/Músicas")
	print("nome do arquivo Exemplo: /Survivor - Eye Of The Tiger (Official HD Video).mp4")
	print("\033[1;33m[+]\033[m No nome do arquivo vocês sempre colocam uma / antes \033[1;31m( SEM ESPAÇO APÓS A / para usuários do Termux)\033[m")
	print("\n----------------\n")
	print("\033[1;33m[+]\033[m Pc: \\Users\Cliente\Downloads\E-tube\Músicas")
	print("nome do arquivo Exemplo: \\Survivor - Eye Of The Tiger (Official HD Video).mp4")
	print("\033[1;33m[+]\033[m No nome do arquivo vocês sempre colocam uma \ antes \033[1;31m( SEM ESPAÇO APÓS A \ para usuários do PC)\033[m\n")

	input("Enter para começar a conversão: ")

	caminho = input("Digite o caminho: ")
	nome_entrada = input("Nome do mp4 baixado: ")
	nome2 = caminho + nome_entrada
	nome = input("Nome de saída em mp3: ")
	meuclipe = mp.VideoFileClip(nome2)
	meuclipe.audio.write_audiofile(nome)
