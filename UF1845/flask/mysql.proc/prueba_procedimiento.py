import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3360',
    password='password_que_quieras_para_root',
    database='jardineria'
)

cursor=conexion.cursor()
# cursor.execute('call oficina_ciudad()')
cursor.callproc('oficina_ciudad',)

resultado = cursor.fetchall()

cursor.close()
conexion.close()

for fila in resultado:
    print(fila)

