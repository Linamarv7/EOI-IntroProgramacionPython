for numero in range(3):
    print(numero)

for numero in range(1,4):
    print(numero)

for numero in range(1,20,2):
    print(numero)

contadornumero =0
for numero in range(1,21,2):
    contadornumero +=1
    if (contadornumero<5):
        continue # salte a la linea 2
    print(numero)


contadordenumerosenlaserie =0
for numero in range(1,21,2):
    contadordenumerosenlaserie +=1
    #if (contadordenumerosenlaserie>5):
    if (contadordenumerosenlaserie<=5):
        continue # salte a la linea for
    print(numero)
    #print("otra instruccion 1")
    #print("otra instruccion 2")
    #print("otra instruccion 3")
    #print("otra instruccion 4")
print("Numeros de la serie:", contadordenumerosenlaserie)