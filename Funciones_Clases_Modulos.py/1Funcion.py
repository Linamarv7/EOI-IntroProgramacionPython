#mayo 6
#nombre='Lina'
#print(f'hola {nombre}')
#nombre='Alejandro'
#print(f'hola {nombre}')

#Lo de arriba esta bien peor queremos algo mas eficiente por eso creamos la funcion def
#reducir errorr y no repetir tanto codigo
def saludar(nombre):
    #funcionalidad del tiempo
    print(f'hola {nombre}, buenos dias')

def sumar(a,b):
    return(a+b)

def addColores(colores,color):
    try:
        colores.append(color)
        return True #devuelve un bool , true
    except AttributeError:
        return False

saludar('Lina')
saludar('Ana')
saludar('Lina')

print(sumar(3,5))
print(sumar(5,5))

colores=[] # lista vacia no tiene elmentos
addColores(colores,'naranja')
addColores(colores,'amarillo')
addColores(colores,'verde')
addColores(colores,'morado')
saludar(colores)

if (addColores('Lina','naranja')==True): # equivalente addColors ()==True/ if(true==true): linea19
    print('Insertado color')
else:
    print('No insertado color')

if (addColores('color','naranja')==True): # texto'lina', colores=lista; llamando a la funcion con un texto o lista? por eso no inserta
    print('Insertado color')
else:
    print('No insertado color')
