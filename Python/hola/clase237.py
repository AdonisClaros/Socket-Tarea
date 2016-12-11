#! /usr/bin/env python
#-*- coding: utf-8 -*-
class Persona:
	def __init__(self):
		self.nombre= ""
		self.color = ""
	def asignarNombre(self):
		self.nombre=raw_input("digite su nombre:")
	def asignarColor(self):
		self.color=raw_input("digite su color de piel:")
	def saludo(self):
		print "¡Hola, mundo! Soy %s." % self.nombre , "y mi color de piel es %s." %self.color
		
persona = Persona()
persona.asignarNombre()
persona.asignarColor()
persona.saludo() 				
