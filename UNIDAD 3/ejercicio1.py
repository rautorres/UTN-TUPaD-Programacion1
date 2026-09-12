print("=== CAJA DEL KIOSCO ===")

# Nombre del cliente
nombre = input("Cliente: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Cliente: ")


# Cantidad de productos
cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: Ingrese una cantidad válida.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)


# Variables para los cálculos
total_sin_descuentos = 0
total_con_descuentos = 0


# Ingreso de productos
for i in range(cantidad):

    precio = input("Producto " + str(i + 1) + " - Precio: ")

    while not precio.isdigit():
        print("Error: El precio debe ser un número entero.")
        precio = input("Producto " + str(i + 1) + " - Precio: ")

    precio = int(precio)

    descuento = input("Descuento (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: Ingrese S o N.")
        descuento = input("Descuento (S/N): ")

    total_sin_descuentos += precio

    if descuento.lower() == "s":
        precio_con_descuento = precio * 0.90
        total_con_descuentos += precio_con_descuento
    else:
        total_con_descuentos += precio


# Cálculos finales
ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos / cantidad)


# Resultados
print()
print("=== RESUMEN DE LA COMPRA ===")
print("Cliente:", nombre)
print("Total sin descuentos: $", total_sin_descuentos)
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
