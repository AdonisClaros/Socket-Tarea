#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv 
import codecs
def count_votes(resultados):
	print ("Numero de Usuario para la carrera de " + resultados)
	count = 0
	for line in open('/home/user/Documentos/csv/borrowers_test.csv'):
		linea= line.split(",")
		voto = linea[6]
		if resultados in voto:
			count = count + 1
	return count
import csv
datos=[]
with open('/home/user/Documentos/csv/borrowers_test.csv', 'r') as archivo:
	lineas = archivo.read().splitlines()
	lineas.pop(0)
	for l in lineas:
		linea =l.split(',')
		datos.append(linea[0])
 


print "Menu"

while True:

    print "1- Mostrar cantidad de registros clasificando M o F"
    print "2- Buscar archivo"
    print "3- Mostrar cantidad de Usuarios por carrera"
    print "4- Mostrar cantidad de datos Erroneos"
    print "5- Agregar registro al final"
    print "6- Ordenar los registros por orden alfabético"
    print "7- Ordenar los registros por orden alfabético usando quicksort"
    print "8- Salir"

    elegir=int(raw_input("Ingrese opcion: "))
    
    if elegir == 1:
		n_c = []
		hombre = []
		mujer = []
		sexo_null = []
		sex_null = []
		for line in open('/home/user/Documentos/csv/borrowers_test.csv'):
			linea = line.split(',')
			sexo_h = linea[4]
			sexo_m = linea[4]
			carrera = linea[6]	
			if sexo_h == "M":
				hombre.append(sexo_h)
			elif sexo_m == "F":
				mujer.append(sexo_m)
			elif sexo_h or sexo_m == "NULL":
				sexo_null.append(sexo_h)
			elif sexo_m  == "":
				sex_null.append(sexo_m)
				
			suma = len(hombre) + len(mujer) + len(sexo_null) + len(sex_null)
				
            
		print "El numero de Hombres que hay es: ", len (hombre) 
		print "El numero de Mujeres que hay es: ",len (mujer)
		print "El numero de NULL en la columna de sexo es: ",len(sexo_null)
		print "El numero de espacio vacios en la colunma de sexo es: ",len(sex_null)
		print "Total: ", suma
		print ""
	
		
		
    elif elegir == 2:
		print "Selecione el metodo de busqueda"
		while True:
			print "1-busqueda lineal"
			print "2-busqueda secuencial"
			print "3-busqueda binaria"
			print "4-salir"
			seleccione=int(raw_input("Ingrese opcion: "))
			
			if seleccione == 1:
			
				L = datos
				x = raw_input ("ingrese el nombre: ")
				def linearSearch(L,x):
					for e in L:
						if e == x.upper() or e == x.lower():
							return True
					return False
				print linearSearch(L,x)
				
			elif seleccione == 2:
				datos=[]
				with open('/home/user/Documentos/csv/borrowers_test.csv', 'r') as archivo:
					lineas = archivo.read().splitlines()
					lineas.pop(0)
					for l in lineas:
						linea =l.split(',')
						datos.append(linea[0])

					lista = datos
					buscar = raw_input('ingrese el nombre: ')

					posicion = 0
					encontrado = False
					posicion_valor_buscar = 0

					for posicion in range(len(lista)):
						if lista[posicion]==buscar.lower() or lista[posicion]==buscar.upper():
							posicion_valor_buscar=posicion
							encontrado=True
						posicion=posicion+1
					if encontrado==True:
						print 'Valor '  + buscar + ' encontrado en posicion',posicion_valor_buscar
					else:
						print 'Valor no encontrado'
						
			elif seleccione == 3:
					datos=[]
					with open('/home/user/Documentos/csv/borrowers_test.csv', 'r') as archivo:
						lineas = archivo.read().splitlines()
						lineas.pop(0)
						for l in lineas:
							linea =l.split(',')
							datos.append(linea[0])

						lista = datos
						encontrado=False
						buscar=raw_input('Ingrese nombre: ')
						minimo=0
						maximo=len(lista)-1
						centro=0
						posicion=0
						while minimo <= maximo and not encontrado:
							centro=(minimo+maximo) // 2
							if lista[centro]==buscar:
								encontrado=True
								posicion=centro
							elif lista[centro] < buscar:
								minimo=centro+1
							else:
								maximo=centro-1
						print 'el nombre de ' +str(buscar)+' en la posicion: '+str(posicion)
			elif seleccione == 4:
				break
			print ""
		
    elif elegir == 3:
		print(count_votes ("Arquitectura"))
		print(count_votes ("INGENIERIA CIVIL"))
		print(count_votes ("Licenciatura en Anestesiología e Inhaloterapia"))
		print(count_votes ("Licenciatura en Sociología"))
		print(count_votes ("Doctorado en Medicina"))
		print(count_votes ("Licenciatura en Ciencias Jurídicas"))
		print(count_votes ("Licenciatura en Ciencias de la Educación en la Especialidad de Primero y Segundo Ciclo de Educación Básica"))
		print(count_votes ("LICENCIATURA EN ADMINISTRACION DE EMPRESAS"))
		print(count_votes ("Licenciatura en Fisioterapia y Terapia Ocupacional"))
		print(count_votes ("Licenciatura en  Contaduría Pública"))
		print(count_votes ("Ingeniería Industrial"))
		print(count_votes ("Licenciatura en Mercadeo Internacional"))
		print(count_votes ("Licenciatura en Matemática"))
		print(count_votes ("Especialidad Médica en Ginecología y Obstetricia"))
		print(count_votes ("Licenciatura en Laboratorio Clínico"))
		print(count_votes ("Ingeniería Agronómica"))
		print(count_votes ("LICENCIATURA EN PSICOLOGIA"))
		print(count_votes ("Ingeniería de Sistemas Informáticos"))
		print(count_votes ("LICENCIATURA EN ADMINISTRACION DE EMPRESAS"))
		print(count_votes("Licenciatura en Biología"))
		print(count_votes("Licenciatura en Letras"))
		print(count_votes("Profesorado en Educación Inicial y Parvularia"))
		print(count_votes("Licenciatura en Química y Farmacia"))
		print(count_votes("Licenciatura en Física"))
		print(count_votes("Profesorado en Matemática para Tercer Ciclo de Educación Básica y Educación Media"))
		print(count_votes("Profesorado en Idioma Inglés para Tercer Ciclo de Educación Básica y Educación Media"))
		print(count_votes("Licenciatura en Lenguas Modernas Especialidad en Francés e Inglés"))
		print(count_votes("Maestría en Administración Financiera"))
		print(count_votes("Licenciatura en Economía"))
		print(count_votes("Profesorado en Ciencias Sociales para Tercer Ciclo de Educación Básica y Educación Media"))
		print(count_votes("Maestría en Profesionalización de la Docencia Superior"))
		print(count_votes("Profesorado en Biología para Tercer Ciclo de Educación Básica y Educación Media"))
		print(count_votes("Profesorado en Educación Básica para Primero y Segundo Ciclos"))
		print(count_votes("Maestría en Gestión Ambiental"))
		print(count_votes("Maestría en Métodos y Técnicas de Investigación Social"))
		print""
		
    elif elegir == 4:
		nombre_null = []
		nombre_null1 = []
		apellido_null = []
		c_c_null = []
		fecha_null = []
		sexo1_null = []
		c_d_c_null = []
		n_c_null = []
		for line in open('/home/user/Documentos/csv/borrowers_test.csv'):
			linea = line.split(',')
			Nombre = linea[0]
			Apellido = linea[1]
			Codigo_Categoria = linea[2]
			Fecha = linea[3]
			Sexo = linea[4]
			Codigo_Carrera = linea[5]
			Nombre_Carrera = linea[6]	
			if Nombre == "NULL":
				nombre_null.append(Nombre)
			elif Sexo == "":
				sexo1_null.append(Sexo)
			elif Apellido  == "NULL":
				apellido_null.append(Apellido)
			elif Nombre_Carrera == "":
				n_c_null.append(Nombre_Carrera)
			elif Codigo_Categoria == "NULL":
				c_c_null.append(Codigo_Categoria)
			elif Fecha == "":
				fecha_null.append(Fecha)
			elif Codigo_Carrera == "":
				c_d_c_null.append(Codigo_Carrera)
				
		print "El numero de datos vacios en la columna de Nombre es: ",len(nombre_null)
		print "El numero de datos vacios en la columna de Apellido es: ",len(apellido_null)
		print "El numero de datos vacios en la columna de sexo es: ",len(sexo1_null)
		print "El numero de datos vacios en la columna de Nombre de carrera es: ",len(n_c_null)
		print "El numero de datos vacios en la columna de Codigo de Categoria es: ",len(c_c_null)
		print "El numero de datos vacios en la columna de Fecha es: ",len(fecha_null)
		print "El numero de datos vacios en la columna de Codigo de Carrera es: ",len(c_d_c_null)
		print""
		
    elif elegir == 5:
		f = open('/home/user/Documentos/csv/borrowers_test.csv','a')
		nombre=raw_input("nombre: ")
		apellido=raw_input("apellido: ")
		c_c=raw_input("codigo categoria: ")
		fecha=raw_input("fecha: ")
		sexo=raw_input("sexo: ")
		codigo_c=raw_input("codigo de carrera: ")
		carrera=raw_input("carrera: ")
		f.write(nombre,apellido,c_c,fecha,sexo,codigo_c,carrera)
		
		f.close
		print "Datos ingresados"
		
		print""
		
    elif elegir == 6:
		
	
		print ""
		
    elif elegir == 7:
		fh = codecs.open('/home/user/Documentos/csv/borrowers_test.csv')
		orden = []
		print"Ordenar datos de Nombres =1 y Apellidos = 0"
		c=int(raw_input("ingrese la columna a ordenar: "))
		for line in fh:
			linea = line.split(',')
			nombre = linea[c]
			orden.append(nombre)
		
		def quickSort(alist):
			quickSortHelper(alist,0,len(alist)-1)

		def quickSortHelper(alist,first,last):
		   if first<last:

			   splitpoint = partition(alist,first,last)

			   quickSortHelper(alist,first,splitpoint-1)
			   quickSortHelper(alist,splitpoint+1,last)


		def partition(alist,first,last):
		   pivotvalue = alist[first]

		   leftmark = first+1
		   rightmark = last

		   done = False
		   while not done:

			   while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
				   leftmark = leftmark + 1

			   while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
				   rightmark = rightmark -1

			   if rightmark < leftmark:
				   done = True
			   else:
				   temp = alist[leftmark]
				   alist[leftmark] = alist[rightmark]
				   alist[rightmark] = temp

		   temp = alist[first]
		   alist[first] = alist[rightmark]
		   alist[rightmark] = temp


		   return rightmark
		alist = orden
		quickSort(alist)
		print(alist)
		
		print""
    elif elegir == 8:
		break
