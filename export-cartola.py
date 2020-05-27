import sys

def getValue(linha, teve):
	palavra = ""
	for i,c in enumerate(linha): 
		if(c == ">" and teve):
			while(linha[i] != "<"):
				i = i + 1
				palavra = palavra + linha[i]
			break
		elif(c == ">" and not(teve)):
			teve = True
	return palavra[:-1]

def getMargen(valor):
	saida = ""
	val = round(float(valor))
	if(val < 1):
		saida = "<1"
	elif(val > 20):
		saida = ">20"
	elif(val>=15 and val<=20):
		saida = "15-20"
	elif(val>=10 and val<15):
		saida = "10-14"
	elif(val>=5 and val<10):
		saida = "5-9"
	elif(val>=1 and val<5):
		saida = "1-4"
	return saida

delimitador = ";"
f = open(sys.argv[1], "r")
out = open("C:/users/romul/Desktop/out.csv", "w")
#out.write("nome" + delimitador + "time" + delimitador + "posicao" + delimitador + "valor" + delimitador + "ultimo_ponto" + delimitador + "media" + delimitador + "gols" + delimitador + "assistencias" + delimitador + "finalizacao_trave" + delimitador + "finalizacao_defendida" + delimitador + "finalizacao_fora" + delimitador + "falta_sofrida" + delimitador + "penalti_perdido" + delimitador + "impedimento" + delimitador + "passe_errado" + delimitador + "jogos_sem_sofrer_gol" + delimitador + "defesa_penalti" + delimitador + "defesa_dificil" + delimitador + "roubada_bola" + delimitador + "gol_contra" + delimitador + "cartao_vermelho" + delimitador + "cartao_amarelo" + delimitador + "gol_sofrido" + delimitador + "falta_cometida;nada\n")
out.write("time" + delimitador + "posicao" + delimitador + "valor" + delimitador + "ultimo_ponto" + delimitador + "media" + delimitador + "gols" + delimitador + "assistencias" + delimitador + "finalizacao_trave" + delimitador + "finalizacao_defendida" + delimitador + "finalizacao_fora" + delimitador + "falta_sofrida" + delimitador + "penalti_perdido" + delimitador + "impedimento" + delimitador + "passe_errado" + delimitador + "jogos_sem_sofrer_gol" + delimitador + "defesa_penalti" + delimitador + "defesa_dificil" + delimitador + "roubada_bola" + delimitador + "gol_contra" + delimitador + "cartao_vermelho" + delimitador + "cartao_amarelo" + delimitador + "gol_sofrido" + delimitador + "falta_cometida;nada\n")

jogadores = []
ofensive = []
defensive = []
nome = ""
sigla = ""
valor = ""
posicao = ""
ult = ""
media = ""
for line in f:
	if "atleta.apelido" in line:
		nome = getValue(line, True)
	if "[atleta.clube_id]['abreviacao']" in line:
		sigla = getValue(line, False)
	if "time.posicoes[atleta.posicao_id]['nome']" in line:
		posicao = getValue(line, False)
	if "atleta.preco" in line:
		valor = getValue(line, True)
	if "atleta.pontos" in line:
		ult = getValue(line, True)
	if "atleta.media" in line:
		media = getValue(line, True)
	############################## ofensive
	if "atleta.scout.G\">" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.A\">" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.FT" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.FD" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.FF" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.FS" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.PP" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.I" in line:
		ofensive.append(getValue(line, True))
	if "atleta.scout.PE" in line:
		ofensive.append(getValue(line, True))
	################################## defensive
	if "atleta.scout.SG" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.DP" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.DD" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.RB" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.GC" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.CV" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.CA" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.GS" in line:
		defensive.append(getValue(line, True))
	if "atleta.scout.FC" in line:
		defensive.append(getValue(line, True))

	if(nome!="" and sigla!="" and posicao!="" and valor!="" and ult!="" and media!="" and len(ofensive)==9 and len(defensive)==9):
		out.write("'"+nome+"'" + delimitador)
		out.write("'"+sigla+"'" + delimitador)
		out.write("'"+posicao+"'" + delimitador)
		out.write("'"+getMargen(valor)+"'" + delimitador)
		out.write(ult + delimitador)
		out.write(media + delimitador)
		for ofe in ofensive:
			out.write(ofe + delimitador)
		for defen in defensive:
			out.write(defen + delimitador)
		out.write('\n')

		ofensive = []
		defensive = []
		nome = ""
		sigla = ""
		valor = ""
		posicao = ""
		ult = ""
		media = ""
f.close()
out.close()