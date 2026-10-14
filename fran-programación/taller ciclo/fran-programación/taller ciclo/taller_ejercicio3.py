# Ejercicio 3-Subcadenas

palabra = input("Escriba una palabra: ")

longitud = 1

while longitud <= len(palabra):

    inicio = 0

    while inicio <= len(palabra) - longitud:
        subcadena = palabra[inicio:inicio + longitud]
        print(subcadena)

        inicio = inicio + 1

    longitud = longitud + 1