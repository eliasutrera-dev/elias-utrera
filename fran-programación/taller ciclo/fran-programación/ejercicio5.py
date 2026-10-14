año = int(input("ingrese año: "))
if  año % 4 == 0:
    if año  %  100 != 0:
        print("el año es bisiesto")
    elif año % 400 == 0: 
        print(" EL año es bisiesto")
    else:
        print("el año no es bisiesto")
else:
    print(("el año no es bisiesto"))   