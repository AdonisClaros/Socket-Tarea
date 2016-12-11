#! /usr/bin/env python
#-*- coding: utf-8 -*-
#herencia de clase
#operacion es la clase base
class Operacion:
	def cargar1(self,v1):
		self.valor1=v1
	def cargar2(self,v2):
		self.valor2=v2
	def imprimir(self):
		print self.resultado
		print ''
		
#clase heredada de la clase Operacion
class Suma(Operacion):
	def operar(self):
		self.resultado = self.valor1 + self.valor2			

class Resta(Operacion):
	def operar(self):
		self.resultado = self.valor1 - self.valor2				
		
s = Suma()
s.cargar1(10)
s.cargar2(20)
s.operar()
print "la suma es:"
s.imprimir()

r = Resta()
r.cargar1(10)
r.cargar2(2)
r.operar()
print "la resta es:"
r.imprimir()

