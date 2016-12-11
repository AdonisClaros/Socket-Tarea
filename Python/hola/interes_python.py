prestamo_inicial=1000
plazo =5
tasa_interes=10.0/100.0
prestamo_final=0
pago_prestamo_anual=0
pago_anual=[]
for i in range(plazo):
    interes = prestamo_inicial * tasa_interes
    pago_prestamo_anual = interes * prestamo_inicial
    pago_anual.append(pago_prestamo_anual)
    
    print i, pago_prestamo_anual
    prestamo_inicial = pago_prestamo_anual
print pago_anual