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

def Adicionar_links(arq, dados):
	try:
		file = open(arq, "at")
	except:
		print("Impossível abrir esse arquivo!")
	else:
		try:
			file.write("{}\n".format(dados))
		except:
			print("Impossível escrever no arquivo!")
		else:
			pass
