while True:
    bolsa = input("¿Hay una bolsa disponible? (si/no): ").lower()

    if bolsa == "si":
        print("Vaciando el arroz en la bolsa...")
        print("Sellando la bolsa...")
        print("Empacando la bolsa en una caja...")

    elif bolsa == "no":
        print("No hay bolsa disponible.")
        print("Esperando para volver a verificar...")

    else:
        print("Opción incorrecta. Escriba si o no.")