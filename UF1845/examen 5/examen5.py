# Ejercicio 1

nombre = input("Introduce tu nombre: ")
print("En mayúsculas:", nombre.upper())
print("En minúsculas:", nombre.lower())
print("Número de caracteres:", len(nombre))
print("Sin espacios al inicio ni al final:", nombre.strip())


# Ejercicio 2

numeros = []

for i in range(5):
    num = float(input(f"Introduce el número {i+1}: "))
    numeros.append(num)

print("Lista completa:", numeros)
print("Número mayor:", max(numeros))
print("Número menor:", min(numeros))
print("Suma total:", sum(numeros))


# Ejercicio 3

nombre = input("Nombre: ")
edad = input("Edad: ")
ciudad = input("Ciudad: ")

persona = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

print(persona["nombre"], "tiene", persona["edad"], "años y vive en", persona["ciudad"] + ".")

# Ejercicio 4

def area_rectangulo(base, altura):
    return base * altura

base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))

if base > 0 and altura > 0:
    area = area_rectangulo(base, altura)
    print("El área del rectángulo es:", area)
else:
    print("La base y la altura deben ser positivos.")

# Ejercicio 5

inventario = {
    "manzanas": 10,
    "peras": 5,
    "naranjas": 8
}

while True:
    print("1. Mostrar inventario")
    print("2. Añadir producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(producto, ":", cantidad)

    elif opcion == "2":
        producto = input("Nombre del nuevo producto: ")
        cantidad = int(input("Cantidad: "))
        inventario[producto] = cantidad
        print("Producto añadido.")

    elif opcion == "3":
        producto = input("Actualizar: ")
        if producto in inventario:
            cantidad = int(input("Nueva cantidad: "))
            inventario[producto] = cantidad
            print("Cantidad actualizada.")
        else:
            print("El producto no existe.")

    elif opcion == "4":
        producto = input("Producto a eliminar: ")
        if producto in inventario:
            del inventario[producto]
            print("Producto eliminado.")
        else:
            print("El producto no existe.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")