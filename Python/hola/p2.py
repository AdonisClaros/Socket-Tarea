productos = {
0: {'Dulces':[0.05,'bolsa',30,"a" ]},
1: {'Pan':[0.15,'unidad',50,"b" ]},
2: {'Leche':[2.50,'galon',10,"c" ]},
3: {'Queso':[3.0,'libra',10,"d" ]},
4: {'Frijol':[0.78,'libra',200,"e" ]},
5: {'Arroz':[0.40,'libra',100,"f" ]},
6: {'Cereal':[3.40,'caja',100,"h" ]},
7: {'Jabon':[0.80,'unidad',30,"i" ]},
8: {'Embutidos':[1.20,'libra',55,"j" ]},
}

 
def buscar():
    valor=raw_input("buscar: ")
    for k1 in productos.keys():
        for k, v in productos[k1].iteritems():
            if k==valor:
                print k
                print "precio:", v[0]
                print "pos:", v[1]
                print "existencias:", v[3]  
                
while True:
    print "Almacen"
    print "1 - Registrar producto"
    print "2 - Modificar Producto"
    print "3 - Vender producto"
    print "4 - buscar producto por descripcion"
    print "5 - salir"
    
    opcion = int(raw_input("Seleccione opcion: "))                                  
    
    if opcion == 1:
        try:
            ID_Producto = str(raw_input("Producto: "))
            Descripcion = str(raw_input("Descripcion: "))
            precio_de_venta = int(raw_input("Precio de venta: "))
            Presentacion = str(raw_input("presentacion: "))
            Existencia = int(raw_input("Existencia: "))
        except:
            print "por fabor ingrese los datos del producto"

        
    elif opcion == 2: 
         modificar=raw_input("seleccione el producto:")
         for k1 in productos.keys():
             for k, v in productos[k1].iteritems():
                 if k==modificar: 
                     
         
                    print""

    elif opcion == 3:
        
        print "\n" ,productos
        
        producto_a_vender=raw_input("Digite el nombre del producto: ")
        venta_producto =  int(raw_input("Cantida a vender: "))
        for k1 in productos.keys():
            for k, v in productos[k1].iteritems():
                if k ==  producto_a_vender:
                    existencia = v[2]
                    venta = existencia - venta_producto
                    print "el total que queda del producto es:" ,venta 
                    
                    
    elif opcion == 4:
         descripcion=raw_input("ingrese descripcion: ")
         for k1 in productos.keys():
             for v, v[3] in productos[k1].iteritems():
                 if v==descripcion:
                     print v
                   
               
                        
    elif opcion == 5:  
        break                