#Numeros primos
nro = input('Ingrese un número: ')
if (nro.isdigit()):
    nro = int(nro) #convertir la entrada de tipo texto "3" a numero 3
    div = 2
    band = True #boolean para comprobar si el numero es primo o no
    if nro ==1 :
        print ('Es primo')
    else:
        while band == True and (nro>div) : #band == true equivalente band
            if nro % div == 0 :
                band = False
                break
            #FinSi
            div += 1 #div = div +1
        #FiMientras
        if band == True :                  #band == true equivañente band
            print('Es primo')
        else:
            print('No es primo')
        #FinSi
    #FinSi
else:
    print("Por favor entre un número válido")