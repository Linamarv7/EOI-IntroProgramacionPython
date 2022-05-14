nombre="lina"
print("Longitud de mi nombre: ", len(nombre))

print("Caracter almacenado en casa posicion: ")
print("0 -> ",nombre[0]) #l
print("1 -> ",nombre[1]) #i
print("2 -> ",nombre[2]) #n
print("3 -> ",nombre[3]) #a

print("Hay algun digito en mi nombre: ", nombre.isdigit())

print("Muestra los caracteres dentro del rango: ", nombre[0:3]) # La posición 3 no la introduce
print("Imprime el caracter en la posición -2: ", nombre[-2])
print(nombre[2:]) #del tercer caracter (incluido) al final
print(nombre[:2]) #del principio al tercer caracter (sin incluir)
print(nombre[2:3]) #del tercer caracter (incluido) al cuarto (sin incluir)
print("2: "+nombre[2])
print("-2: "+nombre[-2])
print(nombre[1:10])
print(nombre[-3]) #cuenta desde el final

#para la concatenacion, usar format es mucho mas eficiente que con +
nombre = "lina"
edad = 29
print("Mi nombre es {} y tengo {}".format(nombre, edad))


mensaje="ana"
ciudad= "palmira"
#para la concatenacion, usar format es mucho mas eficiente que con +
print("hola {m} de {c}".format(m=mensaje,c=ciudad))
print("hola "+mensaje+" de "+ciudad) #poco eficiente

numero = 10/3
print("El numero sin formato es: {}".format(numero))
print("El numero con formato es: {n:1.2f}".format(n=numero))
print(f"Hola {mensaje} de {ciudad}")