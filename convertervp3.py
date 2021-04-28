import moviepy.editor as mp
import os
import sys
from time import sleep as suspender

def converter_video_para_mp3():
        os.system("clear")
        print("\033[1;94m=========================== CONVERTER PARA MP3 ===========================\033[m")
        print("\n\033[1;33m[SAIBA UTILIZAR ESSA FUNÇÃO LEIA ABAIXO]\033[m\n")
        print("\033[1;32m[+] Para converter o video para mp3 siga as instruções:\033[m")
        print("\033[1;32m[+] Pegue o caminho onde se encontra o vídeo. Exemplos:\033[m")
        print("\n----------------\n")
        print("\033[1;33m[+]\033[m Termux: /storage/downloads/E-tube/VideosConvertidos")
        print("\033[1;33m[+]\033[m Nome do arquivo Exemplo: /Whatever It Takes.mp4 [\033[1;31mO .mp4 NÃO PODE FALTAR!\033[m]")
        print("\033[1;33m[+]\033[m No nome do arquivo vocês sempre colocam uma / antes \033[1;31m( SEM ESPAÇO APÓS A / para usuários do Termux)\033[m")
        print("\n----------------\n")
        print("\033[1;33m[+]\033[m Pc: \\Users\Cliente\Downloads\E-tube\VideosConvertidos")
        print("\033[1;33m[+]\033[m Nome do arquivo Exemplo: \\Whatever It Takes.mp4 [\033[1;31mO .mp4 NÃO PODE FALTAR!\033[m]")
        print("\033[1;33m[+]\033[m \033[1;31m[IMPORTANTE] O caminho acima é um exemplo, na opção que pedir, cole o caminho certo!\033[m")
        print("\033[1;33m[+]\033[m No nome do arquivo vocês sempre colocam uma \ antes \033[1;31m( SEM ESPAÇO APÓS A \ para usuários do PC)\033[m\n")
        print("----------------\n")
        input("Enter para começar a conversão: ")
        print()
        print()
        try:
                caminho = input("Digite o caminho: ")
                nome_entrada = input("Nome do mp4 baixado: ")
                nome2 = caminho + nome_entrada
                nome = input("Nome de saída em mp3: ")
        except KeyboardInterrupt:
                print("\n\033[1;31mSaindo...\033[m")
                suspender(1)
                sys.exit() # Essa linha está aqui para evitar algum bug inesperado!
        else:
                meuclipe = mp.VideoFileClip(nome2)
                meuclipe.audio.write_audiofile(nome)
