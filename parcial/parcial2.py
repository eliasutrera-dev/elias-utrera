print("Bienvenido a la sala de juegos")

edad = int(input("Ingrese su edad: "))

if edad < 5:
    print("Bienvenido")

else:
    if edad >= 5 and edad <= 18:
        print("Monto a pagar: $5")

    else:
        if edad > 18:
            print("Monto a pagar: $10")

print("Fin del programa")