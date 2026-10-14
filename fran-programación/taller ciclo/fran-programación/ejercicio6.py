letra = input("ingrese letra: ")
if len(letra) == 1:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print("es vocal")
    else:
        print("no es vocal")
else:
    print("dato no procesado")