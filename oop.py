class Pokemon(object):
	""" Esta clase crea pokemones Pachuqueños """
	def __init__(self,nombre='toño'):

		self.size = .5
		self.weight = 20
		self.nombre = nombre
		self.vida = 100


	def hablar(self):
		""" Este metodo imprime el nombre en pantalla """
		print(self.nombre[:4],self.nombre)

	def checar_vida(self):
		if self.vida <=0:
			print('Me petatie')

class TipoFuego(Pokemon):
	""" Esta clase hereda de Pokemon y agrega escupir """
	def escupir(self,atacado):
		""" escupe lumbre """
		print('Toma tu lumbre!')
		atacado.vida -=30
		atacado.checar_vida()

	def apachurrar(self,atacado):
		if self.vida <50:
			print('como se mata el gusano?')
			atacado.vida -=50
			atacado.checar_vida()
		else:
			print('no puedo')


class TipoAgua(Pokemon):
	def chorriar(self,atacado):
		print('mojate!')
		atacado.vida -=30
		atacado.checar_vida()






