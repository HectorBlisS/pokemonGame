class Pokemon(object):
	""" Esta clase crea pokemones Pachuqueños """
	def __init__(self,nombre='toño'):

		self.size = .5
		self.weight = 20
		self.nombre = nombre
		self.vida = 100
		self.furia = 0

	def hablar(self):
		""" Este metodo imprime el nombre en pantalla """
		print(self.nombre[:4],self.nombre)

	def golpear(self,atacado):
		""" Metodo del golpe mas simple de todos """ 
		self.checar_vida()
		print("Golpeee!!!")
		atacado.vida -= 10
		atacado.furia += 10
		atacado.checar_vida()

	def apachurrar(self,atacado):
		""" """
		if self.vida <50 and self.furia>50:
			self.checar_vida()
			print('como se mata el gusano?')
			atacado.vida -= 50
			self.furia -= 50
			atacado.furia += 50
		else:
			print('no puedo')
		atacado.checar_vida()

	def fatality(self,atacado):
		if self.vida <= 5 and self.furia>=100:
			atacado.vida -= 80
			self.furia -= 80
			print("Fataliiiiityyyyy")
			atacado.checar_vida()
		else:
			print("No puedo")

	def burlarse(self, atacado):
		print("Ni cosquillas me haces :P")
		atacado.furia += 15
		self.vida += 10

	def checar_vida(self):
		if self.vida <=0:
			print('Me petatie')
		else:
			print(self.nombre.capitalize(),"\n    Vida:",self.vida,"\n    Furia:",self.furia)

class TipoFuego(Pokemon):
	""" Esta clase hereda de Pokemon y agrega escupir """
	def escupir(self,atacado):
		""" escupe lumbre """
		self.checar_vida()
		print('Toma tu lumbre!')
		atacado.vida -=30
		atacado.furia += 30
		atacado.checar_vida()

class TipoAgua(Pokemon):
	def chorriar(self,atacado):
		self.checar_vida()
		print('mojate!')
		atacado.vida -=30
		atacado.furia +=30
		atacado.checar_vida()






