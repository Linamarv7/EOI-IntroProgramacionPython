#Numeros primos
numerodePrimos = input("Número de primos a mostrar: ")
if (numerodePrimos.isdigit()):
    numerodePrimos=int(numerodePrimos) #Convertir la entrada de tipo TECTO "3" a numero 3
    #iteracion
    for nro in range(1,numerodePrimos+1):  # numerodePrimos = 1 hasta numerodePrimos<(nro+1) sea menor que uno y paso 1     
                                            #FOR no es util aqui porque no mostraria los N numeros primos
 
        div = 2
        band = True
        if nro==1 :
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
    print('Por favor introduzca un número válido')