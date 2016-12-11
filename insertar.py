#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

conexion = sqlite3.connect('/home/user/Documentos/BD/datos_empleados.db')
print "Conexion a Base de datos establecida "
id1=50
dui='0086757589-2'
nombre="Ludwin Hernandez"
edad=33
direcc="San Miguel"
nit='1312-310891-103-2'
id_depto=2
salario=1000.0

conexion.execute("INSERT INTO empleado (dui,nombre,edad,direccion,nit,salario,id_depto) VALUES (?,?,?,?,?,?,?)",  (dui,nombre,edad,direcc,nit,salario,id_depto))

conexion.commit()

print "Registros creados con exito"
conexion.close()
