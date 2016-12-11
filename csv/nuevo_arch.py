import os
from subprocess import call
import csv
'''
fh = open('/home/user/Documentos/csv/archivo.txt','w')
fh.write('william,perez,22,78954755')
fh.write('Juan,Martines,23,78945211')
fh.close

fh = open('/home/user/Documentos/csv/archivo.txt')
for line in fh:
	linea = line.split(',')
	nombre = linea[0]
	apellido = linea[1]
	print nombre, apellido
	fh.close'''
'''
f = open('/home/user/Documentos/csv/archivo.csv','w')
f.write('william,perez,22,78954755\n'),
f.write('Juan,Martines,23,78945211\n')
f.close
'''
'''
f = open('/home/user/Documentos/csv/archivo.csv')	
lns = csv.reader(f,delimiter=',')
for line in lns:
	nombre = line[0]
	apellido = line[1]
	print nombre,apellido
f.close	'''
'''
f = open('eggs.csv','w') 
obj = csv.writer(f,delimiter =' ',quotechar='|',quoting = csv.QUOTE_ALL)
obj.writerow(['nombres','apellidos','edad'])
f.close'''

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

