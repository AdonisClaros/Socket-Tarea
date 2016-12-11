#!/usr/bin/python
# -*- coding: utf-8 -*-
import platform
import socket
import sys
from thread import *  #agregamos paquete para la programacion por hilo

HOST = ''#Escucha por todas las interfaces
PORT = 8800 #Usamos un puerto de numeracion alta para no interferi

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Creado'

try:
	s.bind((HOST, PORT))
except socket.error, msg:
	print 'Error al crear socket.Error code: '  +str(msg[0]) + ', mensaje de error ' + msg[1]
	sys.exit()
	
print 'Enlace via Socket Activo' 

s.listen(10) #Encolara un maximo de 5 conexiones
print 'Socket escuchando en puerto '+str(PORT)

#Espera y acepta las conexiones
conn, addr = s.accept()

#muestra informacion del cliente
print 'Conectado con ' +addr[0] + ':' +str(addr[1])

def hilo_cliente(conn):
	#enviar un mensaje al cliente cuando se conecte
	conn.send('Bienvenido al serve. Esriba algo y precione intro'),
	

	#Espera comunicacion con cliente	
	while True:
		#espera y acepta las conexiones del cliente
		#conn, addr = s.accept()
		#print 'Conectado con ' +addr[0] + ':' +str(addr[1])
		data = conn.recv(1024)
		if not data:
			break
		elif data =='q':
			print 'rcibi '+data + ' tome un accion'
		elif data == 'Hola como estas?':
			respuesta = 'Muy bien y tu?'
		elif data == 'Muy bien serve y que haces?':
			respuesta = 'Pues aqui no mas almacenando info.... y que me cuentas?'
		elif data == 'Pues nada, no mas jugando videos juegos y programandote':
			respuesta = 'oya veo que la has pasado bien'
		elif data == 'Juguemos te pregunto cosas y me respodones':
			respuesta = 'Excelente juguemos!!'
		elif data == 'Ram':
			respuesta = 'Este equipo tiene 3GB de Ram'
		elif data == 'Procesador':
			respuesta = platform.processor()
		elif data == 'Red asociada':
			respuesta = platform.node()
		elif data == 'Sistema':
			respuesta = platform.system()
		elif data == 'Tipo de maquina':
			respuesta = platform.machine()
		elif data == 'Plataforma subyacente':
			respuesta = platform. platform()
		elif data == 'Numero de versión del sistema':
			respuesta =  platform. release() 
		elif data == 'Aplicacion usada en python':
			respuesta = platform.python_implementation()
		elif data == 'Version de python':
			respuesta = platform.python_version()
		elif data == 'Version del sistema':
			respuesta = platform.version()
		elif data == 'Python':
			respuesta = 'Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible. Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional.'
		elif data == 'Pupusa':
			respuesta = 'Una pupusa (del pipil pupusawa) es la pronunciación españolizada de popotlax, una conjugación de las palabras en el idioma Náhuatl popotl, que significa grande, relleno, abultado, y de tlaxkalli o tortilla. Es una tortilla de maíz o arroz gruesa hecha a mano (a base de masa de maíz o de arroz, una masa de harina de maíz o masa de arroz usada en la cocina criolla) que está rellena con uno o más de los siguientes ingredientes: queso (normalmente un queso fresco muy común en ciertos países llamado quesillo), chicharrón, ayote, frijoles refritos o queso con loroco.'
		elif data == 'Debian':
			respuesta = 'Debian o Proyecto Debian (en inglés: Debian Project ) es una comunidad conformada por desarrolladores y usuarios, que mantiene un sistema operativo GNU basado en software libre. El sistema se encuentra precompilado, empaquetado y en formato deb para múltiples arquitecturas de computador y para varios núcleos.'
		elif data == 'Chicha':
			respuesta = 'Chicha es el nombre que reciben diversas variedades de bebidas alcohólicas derivadas principalmente de la fermentación no destilada del maíz y otros cereales originarios de América: aunque también en menor medida, se suele preparar a partir de la fermentación de diferentes frutos.'
		elif data == 'Chimichanga':
			respuesta = 'La chimichanga es un plato consumido principalmente en el norte de México y texas , habiendo diferencias notables de preparación y consumo en los diferentes estados. En los Estados de Chihuahua, Baja California, Sonora y Sinaloa es un burrito frito en aceite o manteca generalmente.'
		elif data == 'Transformers':
			respuesta = 'Transformers es una franquicia de entretenimiento (juguetes, series animadas, películas, cómic, videojuegos, etc) co-producida entre las empresas de juguetes Hasbro y Takara Tomy. El hilo argumental de esta franquicia se basa en dos razas robóticas, los Autobots y los Decepticons, originarias del planeta Cybertron.'
		elif data == 'Zeus':
			respuesta = 'Zeus, en la mitología griega, dios del cielo y soberano de los dioses olímpicos. Zeus corresponde al dios romano Júpiter.Según Homero, se consideraba a Zeus padre de los dioses y de los mortales. No fue el creador de los dioses y de los hombres; era su padre, en el sentido de protector y soberano tanto de la familia olímpica como de la raza humana. Señor del cielo, dios de la lluvia y acumulador de nubes blandía el terrible rayo. Su arma principal era la égida, su ave, el águila, su árbol, el roble.'
		elif data == 'Excalibur':
			respuesta = 'Excalibur es el nombre más aceptado de la espada legendaria del Rey Arturo, a la que se le han atribuido diferentes propiedades extraordinarias a lo largo de las numerosas versiones del mito y las historias subsiguientes.'
		elif data == 'Megalodon':
			respuesta = 'El Megalodon fue un pez de entre 10 o 18 metros, uno de los mayores depredadores del océano, del mismo género que el actual tiburón blanco. Era lo suficientemente grande para comer cachalotes y para tragarse a una persona de un bocado.'
		elif data == 'Halo':
			respuesta = 'Halo es una franquicia de videojuegos de ciencia ficción creada y desarrollada por Bungie Studios hasta Halo: Reach, y gestionada ahora por 343 Industries, propiedad de Microsoft Studios. La serie se centra en una guerra interestelar entre la humanidad y una alianza teocrática de alienígenas conocidos como Covenant o Pacto, y más tarde, se encontrarán más amenazas como los Flood y los Prometeos.'
		else:
			respuesta = '“No Puedo procesar su termino, intente con otra función o termine la comunicación.”'
			
		conn.sendall(respuesta)
		
		
	conn.close()

while 1:
	#espera para aceptar conexiones
	conn, addr = s.accept()
	print 'Conectado con ' +addr[0]+ ':' +str(addr[1])
	
	#inicia un nuevo hilo el cual recibe 2 parametros el hilo 
	start_new_thread(hilo_cliente ,(conn,))

s.close()
