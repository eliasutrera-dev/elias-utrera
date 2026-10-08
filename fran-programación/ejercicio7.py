numero = int(input("ingrese numero:  "))
if numero % 15 == 0:
    print("fizzBUZZ")
elif numero % 5 == 0:
    print ("BUZZ")
elif numero % 3 == 0:
    print("FIZZ")
else:
    print("numero no múltiplo")