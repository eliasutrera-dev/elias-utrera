#  Ordenar una lista

numeros = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10]

print("Lista original:")
print(numeros)

i = 0

while i < len(numeros):
    j = 0

    while j < len(numeros) - 1:
        if numeros[j] > numeros[j + 1]:
            auxiliar = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = auxiliar

        j = j + 1

    i = i + 1

print("Lista ordenada:")
print(numeros)
