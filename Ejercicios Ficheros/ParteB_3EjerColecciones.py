from random import randint
from os.path import exists

def lee_o_crea_fichero(file, personas):
    try:
        if exists(file):
            fichero = open(file, 'rt', encoding='UTF-8')
            print("Contenido de fichero:\n{}".format(fichero.read()))
        else:
            fichero = open(file, 'wt', encoding='UTF-8')
            fichero.write(str(personas))
            print(f"Fichero creado")
    except Exception as e:
        print("ERROR: {e}".format(e))
    finally:
        fichero.close()

fichero1 = './Ejercicios Ficheros/Datos_chicos3.csv'
fichero2 = './Ejercicios Ficheros/Datos_chicas3.csv'
file1 = open(fichero1, "rt", encoding='UTF-8')
file2 = open(fichero2, "rt", encoding='UTF-8')


def devolver_lista(cadena):
    cadena = cadena.strip()
    cadena = cadena.strip('[')
    cadena = cadena.strip(']')
    return [int(x) for x in cadena.split(',')]

chicos = devolver_lista(file1.read())
chicas = devolver_lista(file2.read())
file1.close()
file2.close()

def media(lista_de_numeros):
    suma=0 #variable aux para almacenar
    for numero in lista_de_numeros:
        suma= suma+numero
    media = suma / len(lista_de_numeros)
    return media

def calcular_conteos(lista_edades): #(parametro)
    mayores_edad = 0
    menores_edad = 0
    edad_max = 0
    edad_min = 1000
    media_edad = media(lista_edades)
    for edad in lista_edades:
        if edad >= 18:
            mayores_edad += 1
        else:
            menores_edad += 1
        if edad > edad_max:
            edad_max = edad
        if edad < edad_min:
            edad_min = edad
    
    conteos = {
                'mayores_edad': mayores_edad,
                'menores_edad': menores_edad,
                'edad_maxima': edad_max,
                'edad_minima': edad_min, 
                'promedio_edad': media_edad
              }

    return conteos

mujeres = []
hombres = []

genero = [randint(0,1) for n in range(1,101)]
mujeres = [randint(0,101) for g in genero if g==1]
hombres = [randint(0,101) for g in genero if g==0]

file1 = './Ejercicios Ficheros/Datos_chicos3.csv'
file2 = './Ejercicios Ficheros/Datos_chicas3.csv'

lee_o_crea_fichero(file1, mujeres)
lee_o_crea_fichero(file2, hombres)

conteos_hombres = str(calcular_conteos(hombres))
conteos_mujeres = str(calcular_conteos(mujeres))

file_res1 = './Ejercicios Ficheros/Resul_chicos3.csv'
file_res2 = './Ejercicios Ficheros/Resul_chicas3.csv'

fichero_res1 = open(file_res1, 'wt', encoding='UTF-8')
fichero_res1.write(conteos_hombres)
print(f"Fichero hombres creado")
fichero_res1.close()

fichero_res2 = open(file_res2, 'wt', encoding='UTF-8')
fichero_res2.write(conteos_mujeres)
print(f"Fichero mujeres creado")
fichero_res2.close()