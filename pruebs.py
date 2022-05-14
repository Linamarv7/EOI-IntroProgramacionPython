x = 'Hola Mundo'
b = 10
c = 5.5

nota = 8

if nota >= 9:
    print('Sobresaliente')
elif nota >= 8:
    print('Notable')
elif nota >= 6:
    print('Bien')
elif nota >= 5:
    print('Suficiente')
elif nota < 5:
    print('Insuficiente')

saludo = "Hola mundo"
print("saludos" + saludo)
print(type(saludo))


print(5 + 5)
print('5' + '5')
print(int('5') + 5)
print('5' + str(5))
print("Mi numero favorito es el " + str(5))


#Format , f
x = "Hola"
x = "Adiós"
print(x)

edad = 29
nombre = 'Lina'
num_favorito = 3.333333333333333333333333333333
msg_concat = nombre + ' tiene ' +  str(edad) + ' años'
msg_format = '{} tiene {} años y su numero favorito es el {:j>10.4f}'.format(nombre,edad,num_favorito)
msg_format2 = f'{nombre} tiene {edad} años'
msg_format3 = '{n} tiene {e} años y su numero favorito es el {num:0<10.4f}'.format(n=nombre, e=edad,num=num_favorito )
print(msg_format2)
print(msg_concat)
print(msg_format)
print(msg_format3)

#z = input("Introduce tu edad\n")
#print("Tu edad es: {}".format(z))

a=10
b=10
if a>b:
    print(f"el número mayor es {a}")
elif b>a:
    print(f"el número mayor es {b}")
else:
    print("los dos números son iguales")

#for, in

nombres = ['ana', 'camila' , 'camilo', 'lina', 'yoshi']
for nombre in nombres:
    if nombre != 'ana':
        print(nombre)
    
#for, range
for n in range(6):
    print('hola')
for n in range(1,2):
    print(n)
for n in range(2,8,2):
    print(n)

#continue, break
#lista = [elementos]
numeros = [1, 4, 1, 6, 1, 9, 5]

for num in numeros:
    if num == 1:
        continue
    if num == 9:
        break
    if num % 2 == 0:
        print(f'el numero {num} es par')
    else:
        print(f'el numero {num} es impar')

    if num % 3 == 0:
       print(f'el numero {num} es multiplo de 3') 

print('fin del programa')


for num in numeros:
    if num != 1:
        #continue todo lo demas
#  if num == 1:
#continue
        if num % 2 == 0:
            print(f'el numero {num} es par')
        else:
            print(f'el numero {num} es impar')

        if num % 3 == 0:
            print(f'el numero {num} es multiplo de 3') 

print('fin del programa')

#while
num = 7
while num != 0: 
    print(num)
    num-= 1
else:
    print('el numero es 0')
print('fin programa')

# try 
frutas= ['mango', 'coco', 'papaya']
try:
    print(frutas[0])
except IndexError:
    print("Error de indice")
except ZeroDivisionError:
    print('no se puede dividir por cero')
except TypeError: #CONCATENACION  el programa espera una str y es int
    print("error de tipos")
except:
    print('error generico')
else:
    print('no ha fallado')
finally:
    print("fin del bloque try")
print(frutas[0])
print(frutas[1])
    

