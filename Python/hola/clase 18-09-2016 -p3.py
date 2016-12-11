print "Menu"

while True:

    print "1- Suma"
    print "2- area de un circulo"
    print "3- volumen de un cono"
    print "4- mayor de 3 numeros"
    print "5- tipo de datos"
    print "6- salir"


    elegir=int(raw_input("Ingrese opcion: "))
    
    if elegir ==1:
        try:
            
                a = int(raw_input("ingrese valor: "))
                b = int(raw_input("ingrese valor: "))
                suma = a + b
                print "el resultado es: ",suma
        except:        
                print "debe ingresar numeros "
    
    
    elif elegir ==2:
           try:
                r = int(raw_input("ingrese valor: "))
                radio = 3.14 * r * r 
                print  "el resultado es: ", radio 
           except:
                print "debe ingresar numeros "
    
    elif elegir ==3:
            try:
                 r = int(raw_input("ingrese valor: "))
                 a = int(raw_input("ingrese valor: "))
                 volumen = 3.14 * r * r * a
                 print volumen
            except:
                print "debe ingresar numeros "
    
    elif elegir ==4:
    
            def mayor(a,b,c):
                        if a > c:
                                print "el mayor numero es: " , a
                        if b > c:
                                print "el mayor numero es: " , b
                        else:
                                print "el mayor numero es: ", c  
       
    elif elegir ==5: 

                def dato(tdd):
                    print type(tdd)
    
    elif elegir ==6:
      break
      
    else: 
            print "Ingrese un valor valido"
