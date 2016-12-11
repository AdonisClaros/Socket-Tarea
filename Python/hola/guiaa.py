from os import popen
import os
import webbrowser
print "Menu"

while True:

    print "1- Crear Directorio de Trabajo"
    print "2- Descarga sitio html"
    print "3- Descarga archivos con extencion de imagenes"
    print "4- Buscar archivos html"
    print "5- Mostrar la capacidad en Mega bite"
    print "6- salir"


    elegir=int(raw_input("Ingrese opcion: "))
    
    if elegir == 1:
		
	  nueva = raw_input( "ingrese directorio: ")
	  os.mkdir(nueva)
	  print "directorio creado"
	  direccion = raw_input("ingrese directorio que quiere comprobar: ")
	  if os.path.exists(direccion):
                print "El directorio ya existe"
	  else:
		  print "no existe dicho directorio"                
             

    elif elegir == 2:
		url = raw_input("ingrese url de sitio: ")
		renombrar = raw_input("nombre: ")
		guardar_html = '/home/user/Documentos/html/'
		args = ['wget','-r', '-l1','-np','-nd','-A.html','-N','-P' , guardar_html, url,renombrar]
		output = popen(' '.join(args))
		
	
		
    elif elegir == 3:
		url = raw_input("ingrese url de la imagen: ")
		guardar_img = '/home/user/Documentos/IMG/'
		arch = ['wget','-r', '-l','1','-np','-nd','-A.jpg,.png,.gif','-N','-P' , guardar_img, url]
		output = popen(' '.join(arch))
		
		
		
    elif elegir == 4:
		directorio = raw_input("ingrese direcion de directorio: ")
		for base, dirs, files in os.walk(directorio):
		  print files
		  archivo = raw_input("nombre archvio: ")
		  url = archivo
		  nav = webbrowser.get("Iceweasel")
		  nav.open_new(url)
		
    elif elegir == 5:
		directorio = raw_input("ingrese direcion de directorio:")
		os.path.getsize(directorio)
		print os.path.getsize(directorio) 
		
    elif elegir == 6:
		break
		
