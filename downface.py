# script importacoes
# by lucas-Dk
try:
    import re
    import os
    import sys
    import requests
    from tqdm import tqdm
    from time import strftime
    from time import sleep as el
except:
    hora = strftime("%H:%M:%S")
    print("\033[1;36m[{}]\033[m \033[1;33m[!]\033[m Digite esse comando: pip install -r requirements.txt\n".format(hora))
else:

    hora = strftime("%H:%M:%S")

    def validar_link(link):
        valid = re.search(r"^(?=(https://www.facebook.com\/)(.*)(\/videos)((\/)[0-9]{16})$)",link)
        return valid
# essa função é que baixa o video:
    def iniciar_download():
        def baixar_video(qualidade):
            el(1)
            print("\n\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Baixando o seu video com a qualidade: \033[1;33m{}\033[m\n".format(hora,qualidade))
            url_do_video = re.search(rf'{qualidade.lower()}_src:"(.+?)"', html).group(1)
            tamanho_arquivo_requisitar = requests.get(url_do_video, stream=True)
            tamanho_arquivo = int(tamanho_arquivo_requisitar.headers['Content-Length'])
            tamanho_bloqueado = 1024
            nome_arquivo = "VideoFacebook"
            tqdm_dados = tqdm(total=tamanho_arquivo,unit="Kb",desc="\033[1;34mBaixando\033[m")
            with open(nome_arquivo + ".mp4","wb") as baixar:
                for dados in tamanho_arquivo_requisitar.iter_content(tamanho_bloqueado):
                    tqdm_dados.update(len(dados))
                    baixar.write(dados)
            tqdm_dados.close()
            print("\n\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m O seu video foi baixado com sucesso!\n".format(hora))

        while True:
            os.system("clear")
            try:
                url = str(input("\n\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Url do video: ".format(hora)))
            except KeyboardInterrupt:
                print("\n\033[1;36m[{}]\033[m \033[1;31m[!]\033[m Programa encerrado!".format(hora))
                sys.exit()
            else:
                #encontrar = re.match(r"^(?=(https://www.facebook.com\/)(.*)(\/videos)((\/)[0-9]{16})$)",url)
                if validar_link(link=url):
                    html = requests.get(url).content.decode("utf-8")

                    qualidade_HD = re.search(r'hd_src:"https',html)
                    qualidade_SD = re.search(r'sd_src:"https',html)
                    hd = re.search(r'hd_src:null',html)
                    sd = re.search(r'sd_src:null',html)

                    lista = []

                    lista_resolucao = [qualidade_HD,qualidade_SD,hd,sd]

                    for idd,val in enumerate(lista_resolucao):
                        if val != None:
                            lista.append(idd)

                    if len(lista) == 2:
                        if 0 in lista and 1 in lista:
                            qualidade_baixar = input("\n\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Qual qualidade deseja baixar ~> [HD/SD]: ".format(hora)).upper()
                            while qualidade_baixar not in "HD" and qualidade_baixar not in "SD":
                                qualidade_baixar = input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Qual qualidade deseja baixar ~> [HD/SD]: ".format(hora)).upper()
                            if qualidade_baixar == "HD":
                                baixar_video("HD")
                            elif qualidade_baixar == "SD":
                                baixar_video("SD")
                            elif qualidade_baixar == "":
                                print("\033[1;31mOpção inválida! Fechando o progra...\033[m")
                                el(1)
                                sys.exit()

                            voltar_ao_menu = str(input("\033[1;36m[{}] [INFO]\033[m Deseja voltar ao menu ou baixar outro vídeo? [M/V]: ".format(hora))).upper()
                            while voltar_ao_menu not in "M" and voltar_ao_menu not in "V":
                                print("\033[1;36m[{}]z033[m \033[1;32m[INFO]\033[m Por favor, digite uma opção válida!\033[m")
                                voltar_ao_menu = str(input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Deseja voltar ao menu ou baixar outro vídeo? [M/V]: ".format(hora))).upper()
                            if voltar_ao_menu == "M":
                                el(1)
                                break
                            elif voltar_ao_menu == "V":
                                pass
                            elif voltar_ao_menu == "":
                                print("\033[1;31m[{}] \033[1;32m[INFO]\033[m Desculpe essa opção não é uma opção válida!".format(hora))
                                sys.exit()

                    if len(lista) == 2:
                        if 1 in lista and 2 in lista:
                            qualidade_baixada = input("\n\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Esse video não tem versão \033[1;33mHD\033[m, deseja baixar assim mesmo? ~> [S/N]: ".format(hora)).upper()
                            while qualidade_baixada not in "S" and qualidade_baixada not in "N":
                                qualidade_baixada = input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Esse video não tem versão \033[1;33mHD\033[m, deseja baixar assim mesmo? ~> [S/N]: ".format(hora)).upper()
                            if qualidade_baixada == "S":
                                baixar_video("SD")
                            elif qualidade_baixada == "N":
                                sys.exit()
                            elif qualidade_baixada == "":
                                print("\033[1;31mOpção inválida! Fechando o progra...\033[m")
                                el(1)
                                sys.exit()

                            voltar_ao_menu = str(input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Deseja voltar ao menu ou baixar outro vídeo? [M/V]: ".format(hora))).upper()
                            while voltar_ao_menu not in "M" and voltar_ao_menu not in "V":
                                print("\033[1;31m[!] Por favor, digite uma opção válida!\033[m")
                                voltar_ao_menu = str(input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Deseja voltar ao menu ou baixar outro vídeo? [M/V]: ".format(hora))).upper()
                            if voltar_ao_menu == "M":
                                el(1)
                                break
                            elif voltar_ao_menu == "V":
                                pass
                            elif voltar_ao_menu == "":
                                print("\033[1;31m[{}] \033[1;32m[INFO]\033[m Desculpe essa opção não é uma opção válida!".format(hora))
                                sys.exit()


                    if len(lista) == 2:
                        if 0 in lista and 3 in lista:
                            qualidade_baixadas = input("\n\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[mEsse video não tem versão \033[1;33mSD\033[m, deseja baixar assim mesmo? ~> [S/N]: ".format(hora)).upper()
                            while qualidade_baixadas not in "S" and qualidade_baixadas not in "N":
                                qualidade_baixadas = input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Esse video não tem versão \033[1;33mSD\033[m, deseja baixar assim mesmo? ~> [S/N]: ".format(hora)).upper()
                            if qualidade_baixadas == "S":
                                baixar_video("HD")
                            elif qualidade_baixadas == "N":
                                sys.exit()
                            elif qualidade_baixadas == "":
                                print("\033[1;31mOpção inválida! Fechando o progra...\033[m")
                                el(1)
                                sys.exit()

                            voltar_ao_menu = str(input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Deseja voltar ao menu ou baixar outro vídeo? [M/V]: ".format(hora))).upper()
                            while voltar_ao_menu not in "M" and voltar_ao_menu not in "V":
                                print("\033[1;31m[!] Por favor, digite uma opção válida!\033[m")
                                voltar_ao_menu = str(input("\033[1;36m[{}]\033[m \033[1;32m[INFO]\033[m Deseja voltar ao menu ou baixar outro vídeo? [M/V]:  ".format(hora))).upper()
                            if voltar_ao_menu == "M":
                                el(1)
                                break
                            elif voltar_ao_menu == "V":
                                pass
                            elif voltar_ao_menu == "":
                                print("\033[1;31m[{}] \033[1;32m[INFO]\033[m Desculpe essa opção não é uma opção válida!".format(hora))
                                sys.exit()
                else:
                    print("\033[1;36m[{}]\033[m \033[1;31m[+] Essa url não pode ser aberta porque não condiz com url de vídeo!\033[m".format(hora))
                    print("\033[1;32m[!] Escolha uma url válida...\033[m")
                    el(2)
