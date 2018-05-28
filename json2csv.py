import json
import sys

usuarios = 0

def abrirData(path):
	with open(str(path)) as f:
		data = json.load(f)
	global usuarios
	usuarios = data['users']

def transformarJsonEmCsv():
	f = open('dados.csv', 'w')
	f.write('email;ratingType;movie;rate;duration\n')
	# É necessário abrir loops de for até o nível mais
	# profundo do arquivo. E então usar as variáveis criadas
	# nos 'for's.
	# O segredo é que você precisa chegar no nível mais fundo
	# antes de querer dar write em qualquer valor.
	for user in usuarios:
		for ava in usuarios[user]['rates']:
			f.write(str(usuarios[user]['email']) + ';') # email
			f.write(str(usuarios[user]['ratingType']) + ';') # rating type
			f.write(str(ava['movieId']) + ';') # movie
			f.write(str(ava['rate']) + ';') # rate
			f.write(str(ava['duration'])) # duration
			f.write('\n')
	f.close()
	print('Conversão pronta.')

#####################################################################

if __name__ == '__main__':
	abrirData(sys.argv[1])
	transformarJsonEmCsv()
	
