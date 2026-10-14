dia = input("Ingrese día de la semana: ")
DD = int(input("Ingrese día del mes: "))
MM = int(input("Ingrese mes: "))

if DD < 1 or DD > 31:
    print("Se produjo un error")

elif MM < 1 or MM > 12:
    print("Se produjo un error")

elif dia == "lunes":
    print("Clase: nivel inicial")

    examen = input("¿Hubo exámenes? si/no: ")

    if examen == "si":
        aprobados = int(input("Ingrese alumnos aprobados: "))
        no_aprobados = int(input("Ingrese alumnos no aprobados: "))

        porcentaje = aprobados * 100 / (aprobados + no_aprobados)

        print("Porcentaje de aprobados:", porcentaje, "%")

    else:
        print("No hubo exámenes")

elif dia == "martes":
    print("Clase: nivel intermedio")

    examen = input("¿Hubo exámenes? si/no: ")

    if examen == "si":
        aprobados = int(input("Ingrese alumnos aprobados: "))
        no_aprobados = int(input("Ingrese alumnos no aprobados: "))

        porcentaje = aprobados * 100 / (aprobados + no_aprobados)

        print("Porcentaje de aprobados:", porcentaje, "%")

    else:
        print("No hubo exámenes")

elif dia == "miércoles":
    print("Clase: nivel avanzado")

    examen = input("Hubo exámenes? si/no: ")

    if examen == "si":
        aprobados = int(input("Ingrese alumnos aprobados: "))
        no_aprobados = int(input("Ingrese alumnos no aprobados: "))

        porcentaje = aprobados * 100 / (aprobados + no_aprobados)

        print("Porcentaje de aprobados:", porcentaje, "%")

    else:
        print("No hubo exámenes")

elif dia == "jueves":
    print("Clase: práctica hablada")

    asistencia = float(input("Ingrese porcentaje de asistencia: "))

    if asistencia > 50:
        print("Asistió la mayoría")

    else:
        print("No asistió la mayoría")

elif dia == "viernes":
    print("Clase: inglés para viajeros")

else:
    print("Se produjo un error")