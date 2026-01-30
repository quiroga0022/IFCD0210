# Caulcular el precio con IVA de un producto
precio_producto = 32.18
porcentaje_iva = 0.21
#precio_total = precio_producto + precio_producto * porcentaje_iva
precio_total = precio_producto * (1 + porcentaje_iva)
print("El precio total es: ", str(precio_total))
# --------------------------------------------------

#Convertir de grados Celsios a Fahrenheit
# F = C * 1,8 + 32

grados_celsius = 40 
grados_fh = grados_celsius * 1.8 + 32
#print(grados_celsius, '-->', grados_fh)
mensaje = str(grados_celsius) + " Grados Celsius son " + str(grados_fh) + "Grados fh"
print(mensaje)

# --------------------------------------------------

# Calcular el índice de masa corporal 
# IMC = Peso(kg) / altura **2
# imc < 18  --> Bajo
# 18 < imc < 25 --> Normal
# imc > 25 --> Sobrepeso

peso = 87
altura = 1.70
imc = peso / altura ** 2
print(imc)