#Realizar media entre 3 números //04 mayo
#def, define una funcion
def media(lista_de_numeros):
    suma=0 #variable aux para almacenar
    for numero in lista_de_numeros:
        suma= suma+numero
    media = suma / len(lista_de_numeros)
    return media

def imprimir_msj(nombre,edad):
    print(f"{nombre} tiene {edad} años")

imprimir_msj(nombre='lina', edad='29')
imprimir_msj('pepe', '45')


#colocar los 3
num1 = int(input("Introduce número 1: "))

num2 = int(input("Introduce número 2: "))

num3 = int(input("Introduce número 3: "))

media_entrenum= media([num1,num2,num3])

print(f"la nota media es {media_entrenum}")

# 2. Realizar un programa que pida dos numeros, y diga si es par o no, o ambos
#num1 = int(input("Introduce número 1: "))
#num2 = int(input("Introduce número 2: "))

l1 = [12, 5, 5, 8, 52, 6, 96, 4, 1, 66, 25, 23, 7]
x = media(l1)
print(f"la media de l1 es {x}")

# si el numero es par:
#entonces
#sino 