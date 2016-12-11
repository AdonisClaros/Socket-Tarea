from collections import deque
clientes=deque([])

print "Wellcome Wallmark"

while True:

    print "Seleccione una opcion"
    print "1- Llenar pila"
    print "2- Proximo cliente"
    print "3- Numero de clientes"
    print "4- Salir"
    
    pregunta=int(raw_input("Ingrese opcion: "))
    
    if pregunta ==1:
        try:
         x = raw_input("Nombre Cliente: ")
         clientes.append(x)
         print clientes,
        except:         
         print "solo acepta cadenas"
        
    elif pregunta ==4:
        break
        
    elif pregunta ==2:
        clientes.pop()
        print "cliente atendido", clientes[-1]
        
    elif pregunta ==3:
        print "El numero de clientes es: ", len(clientes),
        print "El ultimo cliente es: ". clientes[-1]
        

        
        
    else: 
            print "Ingrese un valor valido"