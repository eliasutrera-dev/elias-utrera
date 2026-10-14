# Ejercicio 1 

toppings = ["Sin topping", "Frutas", "Granola", "Oreo", "Brownie"]
precios = [0.00, 0.50, 1.50, 1.00, 0.75]

continuar = "si"
contador = 0
total = 0

while continuar == "si" or continuar == "si":

    print("Menu de helados")
    print("0. Sin topping")
    print("1. Frutas")
    print("2. Granola")
    print("3. Oreo")
    print("4. Brownie")

    opcion = int(input("Seleccione un topping (0-4): "))

    if opcion >= 0 and opcion <= 4:

        topping = toppings[opcion]
        precio = 1.90 + precios[opcion]

        print("Topping elegido:", topping)
        print("Precio del pedido:", precio)

        total = total + precio
        contador = contador + 1

    else:
        print("Opcion incorrecta")

    continuar = input("Desea hacer otro pedido? (s/n): ")

print("Cantidad de pedidos:", contador)
print("Total a pagar:", round(total, 2))
print("Gracias por su compra")