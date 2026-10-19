print("Bienvenido a La Calle El Muerto")

menu = {
    1: ("Hamburguesa", 12000),
    2: ("Perro caliente", 9000),
    3: ("Papas fritas", 5000),
    4: ("Pizza personal", 10000),
    5: ("Gaseosa", 3000)
}

total = 0
respuesta = "si"

while respuesta == "si":

    print("\n--- MENU DE LA CALLE EL MUERTO ---")
    print("1 - Hamburguesa - $12000")
    print("2 - Perro caliente - $9000")
    print("3 - Papas fritas - $5000")
    print("4 - Pizza personal - $10000")
    print("5 - Gaseosa - $3000")

    opcion = int(input("Seleccione un producto (1-5): "))

    if opcion in menu:
        cantidad = int(input("¿Cuantas unidades desea?: "))

        if cantidad > 0:
            nombre = menu[opcion][0]
            precio = menu[opcion][1]

            subtotal = precio * cantidad
            total = total + subtotal

            print("Producto:", nombre)
            print("Subtotal: $", subtotal)

            respuesta = input(
                "¿Desea pedir otro producto? (si/no): "
            ).lower()

        else:
            print("La cantidad debe ser mayor que cero.")

    else:
        print("¡Uy! Ese producto no existe ni en el mas alla.")
        print("Seleccione una opcion del 1 al 5.")

print("Total a pagar: $", total)
print("Gracias por visitar La Calle El Muerto.")