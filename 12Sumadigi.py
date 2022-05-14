nro = ''
while not nro.isdigit():
    nro = input("Introduce un número: ")
    if nro.isdigit():
        suma = 0
        for cifra in nro: 
            #incremento = int(cifra)
            #suma = suma + incremento
            suma+= int(cifra)
        print(f"La suma total de los dígitos de {nro} es {suma}")
    else:
        print("El número introducido no es válido")