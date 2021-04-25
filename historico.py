# partição do arquivo que armazena os links no arquivo links

def existe(arq):
	resultado = False
	try:
		file = open(arq, "rt")
	except:
		resultado = False
		return resultado
	else:
		resultado = True
		return resultado

def criar(arq):
	try:
		file = open(arq, "wt+")
	except:
		print("Impossível criar esse arquivo!")
	else:
		return True

def adicionar_links(arq, dados, arg):
	try:
		file = open(arq, "at")
	except:
		print("Impossível abrir esse arquivo!")
	else:
		try:
			if arg == "[LINKS DAS PLAYLISTS]":
				file.write("\n{}:\n{}\n".format(arg,dados))
			elif arg == "[LINKS DE VIDEOS]":
				file.write("\n{}:\n{}\n".format(arg,dados))
		except:
			print("Impossível escrever no arquivo!")
		else:
			pass

