# -*- coding: utf-8 -*-
def interes():
    n = 0
    anhos = int(raw_input("años del prestamo: "))
    prestamo =float(raw_input("monto del prestamo: "))
    interes = float(raw_input("monto interes: "))
    tasa_interes = interes /100
    cal_interes = prestamo * tasa_interes
    prestamo_final = cal_interes + prestamo 
    deuda = []
    while n < anhos:
        deuda.append(prestamo_final)
        print "el prestamo final es:", prestamo_final
        n +=1
        print deuda
   