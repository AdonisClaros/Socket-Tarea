#!/usr/bin/python
 # -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('datos_empleados.db')
print "Conexion a Base de datos establecida"

conn.execute("UPDATE empleado set salario = 25000.00 where id=16")
conn.commit
print "Numero de filas afectadas :", conn.total_changes

cursor = conn.execute("SELECT id, nombre, salario  from empleado where id='16'")
for row in cursor:
   print "ID = ", row[0]
   print "NOMBRE = ", row[1]
   print "SAlARIO = ", row[2], "\n"
print "Operación realizada con exito";
conn.close()
