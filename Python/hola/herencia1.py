class SistemasOperativos: #clase padre
	print "Sistemas Operativos mas usados"
	def __init__(self,tipo,arch):
		self.tipo=tipo
		self.arch=arch

class Linux(SistemasOperativos): #clase heredada
	def nombre(self,nombre,tipo,arch):
		print "Mi sistema es", nombre,"de la familia", tipo, "y su arquitectura", arch
	def seguro(self,seguridad):
		print(seguridad)
		
class Windows(SistemasOperativos):
	def nombre(self,nombre,tipo,arch):
		print "Mi sistema es:",nombre,"de la familia", tipo, "y su arquitectura", arch
	def seguro(self,seguridad):
		print(seguridad)			

class BSD(SistemasOperativos):
	def nombre(self,nombre,tipo,arch):
		print "Mi sistema es:",nombre,"de la familia", tipo, "y su arquitectura", arch
	def seguro(self,seguridad):
		print(seguridad)			
		
new = Linux("GNU/Linux")
new.nombre("Ubunto",new.tipo)
new.seguro("Muy seguro")

redhat = Linux("Redhat")
redhat.nombre("Fedora cora",redhat.tipo)

seven = Windows("Windows")
seven.nombre("7 ultimate",seven.tipo)
		
