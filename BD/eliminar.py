 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('/home/user/Documentos/BD/datos_empleados.db')
print "Conexion a Base de datos establecida"

conn.execute("DELETE FROM empleado where id=17")
conn.commit
print "Numero de filas afectadas :", conn.total_changes

cursor = conn.execute("SELECT id, nombre, direccion, salario  FROM empleado")
for row in cursor:
   print "ID = ", row[0]
   print "NOMBRE = ", row[1]
   print "DIRECCION = ", row[2]
   print "SALARIO= ", row[3], "\n"

print "Operación realizada con exito"
conn.close()


