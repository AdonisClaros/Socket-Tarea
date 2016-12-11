# -*- coding: utf-8 -*-

Datos_usuario = {}
def Datos_Usuarios(Usuario,Nombres,Apellidos,Direccion,Departamento,Telefono):
    Datos_usuario["Usuario"] = [Usuario] 
    Datos_usuario["Nombres"] = [Nombres]
    Datos_usuario["Apellidos"] = [Apellidos]
    Datos_usuario["Direccion"] = [Direccion]
    Datos_usuario["Departamento"] = [Departamento]
    Datos_usuario["Telefono"] = [Telefono]  
    
        
while True:
    print "Test"
    print "1 - Registrar nuevo usuario"
    print "2 - Iniciar cuestionario"
    print "3 - Interrumpir cuestionario"
    print "4 - Mostrar resultados"
    print "5 - Salir"
    
    opcion = int(raw_input("Seleccione opcion: "))
    
    if opcion == 1:
        try:
            usuario = str(raw_input("Nombre que tendra como usuario: "))
            nombre = str(raw_input("Escriba solo sus nombres: "))
            apellidos = str(raw_input("Escriba sus apellidos: "))
            direccion = str(raw_input("Escriba su direccion: "))
            departamento = str(raw_input("Escriba su departamento: "))
        except:
            print "Debe escribir solo letras"

        try:
            tel = int(raw_input("Escriba su numero de telefono: "))
        except:
            print "Debe escribir solo numeros"

        Datos_Usuarios(usuario,nombre,apellidos,direccion,departamento,tel)
   
    elif opcion == 2:

        print "INDICACIONES"
        print "Para seleccionar la primera opcion digite 0 = a"
        print "Para seleccionar la segunda opcion digite 1 = b"
        print "Para seleccionar la tercera opcion digite 2 = c"
        print "Para seleccionar la cuarta opcion digite 3 = d"
        print "Para seleccionar la quinta opcion digite 4 = e \n"
        
        
        
        pregunta1 = ("1) Cuales de estos son lenguaje de programacion? ")
        pregunta2 = ("2) Qué modificador de acceso hace que una clase sea pública en Java?")
        pregunta3 = ("3) ¿Quién fue el creador del lenguaje Java? ")
        pregunta4 = ("4) ¿En qué año se presentó el lenguaje Java?")
        pregunta5 = ("5) ¿Java es un lenguaje orientado a?")
        pregunta6 = ("6) La compañía Sun desarrolló la implementación de referencia original para los?")
        pregunta7 = ("7) Java fue diseñado para tener?")
        pregunta8 = ("8) Java es un programa?")
        pregunta9 = ("9) java es utilizado mas que todo en?")
        pregunta10 = ("10) abreviacion de Java?")
        pregunta11 = ("11) ¿Quién fue el creador del lenguaje Php?")
        pregunta12 = ("12) ¿En qué año se presentó el lenguaje php?")
        pregunta13 = ("13) php es un lenguaje orientado a? ")
        pregunta14 = ("14) seleccione una version de php")
        pregunta15 = ("15) para que se utilizado php?")
        pregunta16 = ("16) que animal simboliza python?")
        pregunta17 = ("17) quien creo python?")
        pregunta18 = ("18) en que año fue creado python?")
        pregunta19 = ("19) python es un lenguaje?")
        pregunta20 = ("20) cual es una caracteristica de python?")
        pregunta21 = ("21) como se declara una funcion en python?")
        pregunta22 = ("22) como mostrar datos en python?")
        pregunta23 = ("23) como se declaran lista en python?")
        pregunta24 = ("24) como declarar tuplas en python?")
        pregunta25 = ("25) que animal simboliza php?")
        pregunta26 = ("26) que simboliza java?")
        pregunta27 = ("27) como eliminar datos en python?")
        pregunta28 = ("28) como agregar datos en python?")
        pregunta29 = ("29) como ordenas datos en python?")
        pregunta30 = ("30) para que se utiliza el index?")

        Respuestas1 = ["Java","Python","Linux","Windoms","Ninguno"]
        Respuestas2 = ["Public","public","free","private","protected"]
        Respuestas3 = ["James Gosling","Dennis Ritchie","Bjarne Stroustrup","Rasmus Lerdorforf","literal a"]
        Respuestas4 = ["1990","1995","1997","1993","1980 e 1990"]
        Respuestas5 = ["Objetos","sisemas","computadoras","Mac's","Literal a"]
        Respuestas6 = ["Compiladores java","servidores","bases","literal a","la red"]
        Respuestas7 = ["muchos datos","pocas dependenias","literal b","muchas herramientas","ninguna"]
        Respuestas8 = ["privado","libre","de alto costo","literal b","ninguna"]
        Respuestas9 = ["Moviles","Pc","Mac's","ninguno","literal a"]
        Respuestas10 = ["JV","MC","PHP","AC","Literal a"]
        Respuestas11 = ["Rasmus Lerdorf","James Gosling","Literal A","Dennis Ritchie","ninguno"]
        Respuestas12 = ["1996","1994","literal b","1990","1998"]
        Respuestas13 = ["objetos","sistemas","computadoras","Mac's","Literal a"]
        Respuestas14 = ["php","php7","max","Pw","ninguna"]
        Respuestas15 = ["programacion movil","programacion web","ninguna","literal b","consola"]
        Respuestas16 = ["serpiente","leon","elefante","literal a","dragon"]
        Respuestas17 = ["steve jobs","Guido van Rossum","Rasmus Lerdorf","ninguno","literal a"]
        Respuestas18 = ["1990","1997","1997","1992","literal c"]
        Respuestas19 = ["multiplataforma","paginas web","orientado a objetos","ninguno","literal a"]
        Respuestas20 = ["Simple","pesado","de paga","minimalistico","ninguna"]
        Respuestas21 = ["int","def","else","literal b","if"]
        Respuestas22 = ["else","def","print","if","literal c"]
        Respuestas23 = ["parentesis","comillas","corchetes","comillas simples","literal c"]
        Respuestas24 = ["parentesis","comillas","corchetes","literal a","ninguna"]   
        Respuestas25 = ["serpiente","dragon","elefante","pez","literal c"]
        Respuestas26 = ["una taza","una botella","naranja","arbol","literal c"]
        Respuestas27 = ["pop","delete","remove","supp","ninguna"]
        Respuestas28 = ["append","count","supp","insert","ninguna"]
        Respuestas29 = ["append","short","delate","literal a","ninguna"]
        Respuestas30 = ["Devuelve el número de veces que x aparece en la lista ","Devuelve el índice en la lista del primer ítem cuyo valor sea x","eliminar datos","insertar datos","literal b"]
        
        print pregunta1, ":" ,Respuestas1
        respuesta1_1 = int(raw_input("Seleccione respuesta: "))
        respuesta1_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta2, ":" ,Respuestas2
        respuesta2_1 = int(raw_input("Seleccione respuesta: "))
        respuesta2_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta3, ":" ,Respuestas3
        respuesta3_1 = int(raw_input("Seleccione respuesta: "))
        respuesta3_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta4, ":" ,Respuestas4
        respuesta4_1 = int(raw_input("Seleccione respuesta: "))
        respuesta4_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta5, ":" ,Respuestas5
        respuesta5_1 = int(raw_input("Seleccione respuesta: "))
        respuesta5_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta6, ":" ,Respuestas6
        respuesta6_1 = int(raw_input("Seleccione respuesta: "))
        respuesta6_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta7, ":" ,Respuestas7
        respuesta7_1 = int(raw_input("Seleccione respuesta: "))
        respuesta7_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta8, ":" ,Respuestas8
        respuesta8_1 = int(raw_input("Seleccione respuesta: "))
        respuesta8_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta9, ":" ,Respuestas9
        respuesta9_1 = int(raw_input("Seleccione respuesta: "))
        respuesta9_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta10, ":" ,Respuestas10
        respuesta10_1 = int(raw_input("Seleccione respuesta: "))
        respuesta10_2 = int(raw_input("Seleccione otra  respuesta: ")) 
        print "\n" ,pregunta11, ":" ,Respuestas11
        respuesta11_1 = int(raw_input("Seleccione respuesta: "))
        respuesta11_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta12, ":" ,Respuestas12
        respuesta12_1 = int(raw_input("Seleccione respuesta: "))
        respuesta12_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta13, ":" ,Respuestas13
        respuesta13_1 = int(raw_input("Seleccione respuesta: "))
        respuesta13_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta14, ":" ,Respuestas14
        respuesta14_1 = int(raw_input("Seleccione respuesta: "))
        respuesta14_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta15, ":" ,Respuestas15
        respuesta15_1 = int(raw_input("Seleccione respuesta: "))
        respuesta15_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta16, ":" ,Respuestas16
        respuesta16_1 = int(raw_input("Seleccione respuesta: "))
        respuesta16_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta17, ":" ,Respuestas17
        respuesta17_1 = int(raw_input("Seleccione respuesta: "))
        respuesta17_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta18, ":" ,Respuestas18
        respuesta18_1 = int(raw_input("Seleccione respuesta: "))
        respuesta18_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta19, ":" ,Respuestas19
        respuesta19_1 = int(raw_input("Seleccione respuesta: "))
        respuesta19_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta20, ":" ,Respuestas20
        respuesta20_1 = int(raw_input("Seleccione respuesta: "))
        respuesta20_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta21, ":" ,Respuestas21
        respuesta21_1 = int(raw_input("Seleccione respuesta: "))
        respuesta21_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta22, ":" ,Respuestas22
        respuesta22_1 = int(raw_input("Seleccione respuesta: "))
        respuesta22_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta23, ":" ,Respuestas23
        respuesta23_1 = int(raw_input("Seleccione respuesta: "))
        respuesta23_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta24, ":" ,Respuestas24
        respuesta24_1 = int(raw_input("Seleccione respuesta: "))
        respuesta24_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta25, ":" ,Respuestas25
        respuesta25_1 = int(raw_input("Seleccione respuesta: "))
        respuesta25_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta26, ":" ,Respuestas26
        respuesta26_1 = int(raw_input("Seleccione respuesta: "))
        respuesta26_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta27, ":" ,Respuestas27
        respuesta27_1 = int(raw_input("Seleccione respuesta: "))
        respuesta27_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n" ,pregunta29, ":" ,Respuestas28
        respuesta28_1 = int(raw_input("Seleccione respuesta: "))
        respuesta28_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta29, ":" ,Respuestas29
        respuesta29_1 = int(raw_input("Seleccione respuesta: "))
        respuesta29_2 = int(raw_input("Seleccione otra respuesta: ")) 
        print "\n" ,pregunta30, ":" ,Respuestas30
        respuesta30_1 = int(raw_input("Seleccione respuesta: "))
        respuesta30_2 = int(raw_input("Seleccione otra respuesta: "))
        print "\n"

       
 
                                                                                                                                                                                                                                            
    elif opcion == 3:
        print "opcion no lista"
        
    elif opcion == 4:
        print "opcion no lista"
        
    elif opcion == 5:
        break    
        
    else:
        print "Opcion incorrecta"