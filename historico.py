# partição do arquivo que armazena os links no arquivo links

def existe(arq):
	resultado = False
	try:
		fil = open(arq, "rt")
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

def adicionar_links(arq, dados, argumentos=None):
	try:
		file = open(arq, "at")
	except:
		print("Impossível abrir esse arquivo!")
	else:
		try:
			if argumentos != None:
				if argumentos == "Playlist"
					file.write("{}:\n{}\n".format(argumentos,dados))
				elif argumentos == "Video solo":
					file.write("{}:\n{}\n".format(arqgumentos,dados))
			else:
				return False
		except:
			return False
		else:
			return True
