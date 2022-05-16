from random import randint
from os import path

def rellenar_lista_aleatoria():
    lista_de_edades = [] 
    for n in range(100): #iteracciones
        num = randint(15,22) #generar un numero entre 15 y 22
        lista_de_edades.append(num) #agrego el num alea a la  lista

    return lista_de_edades #devuelve la lista

def calcular_conteos(lista_edades): #(parametro)
    mayores_edad = 0
    menores_edad = 0
    edad_max = 0
    for edad in lista_edades:
        if edad >= 18:
            mayores_edad += 1
        else:
            menores_edad += 1
        if edad > edad_max:
            edad_max = edad
    resultado = f"{mayores_edad} son mayores de edad\n"
    resultado += f"{menores_edad} son menores de edad\n"
    resultado += f"La edad máxima es {edad_max}\n"

    return resultado

def porcentajes(lista_edades):
    valores_unicos = list(set(lista_edades)) # dejar en una variable solo valores unicos, quitar los repetidos, luego vuelvo a convertir en list
    edades_porcentaje = {} # llaves,  voy a crear un diccionario, lo dejo vacio. Edad es clave y porcentaje es el valor
    for edad in valores_unicos:
        numero_personas = lista_edades.count(edad) # aqui pretendo contar en la lista de edades, el numero de personas con su eddad (cuantas personas tienen esa edad)
        porcentaje = numero_personas / len(lista_edades) * 100 # porcentaje: num de personas dividido entre la longitud de la lista(cantidad max)
        edades_porcentaje[edad] = f"{porcentaje:.0f}%" #  en el dicc edad_porc, con la clave edad le añado el procenatajeel porcentaje para cada edad en [acceder al indice de la clave q es edad], el formato del porcentaje es sin decimales(float)
    
    resultado = "Los porcentajes por edades son:\n" 
    for edad, porcentaje in edades_porcentaje.items(): # recorrer el dicc uso el items porq dicc no es lista items: devuelve clave y valor en forma de lista dicc c:edad, v:%
        resultado += f" - {edad} años --> {porcentaje}\n"
    return resultado


def cargar_datos():
    try:
        file_name = 'Datos_ejercicioA2.txt'
        file_path = f'./Ejercicios Ficheros/{file_name}'
        if path.exists(file_path):
            print(f'El fichero {file_name} ya existe')
            file = open(file_path, 'rt', encoding='UTF-8') # ir a la ruta completa, file (objeto) representa al archive
            data = file.read() #data es contenido
            print(f'El contenido del fichero es:\n{data}')
        else:
            print(f'Se va a generar un fichero: {file_path}')
            lista_edades = map(lambda x: str(x), rellenar_lista_aleatoria())
            data = ';'.join(lista_edades) # convierte en cadena una lista
            file = open(file_path, "wt", encoding='UTF-8') # abrir mi archivo en modo escritura- wt
            file.write(data) # file es el archivo y escribo aqui (ejecutar la lista)
            print('Archivo guardado con éxito')
    except Exception as e:
        print(f'Exception:{e}') #E:write() argument must be str, not list
    finally:
        file.close()
    return list(map(lambda x: int(x), data.split(';'))) #lista en str  separada por ;

def guardar_resultado(lista):
    try:
        file_name = 'Resultado_ejercicioA2.txt'
        file_path = f'./Ejercicios Ficheros/{file_name}'
        if path.exists(file_path):
            print(f'El fichero {file_name} está guardado')
            file = open(file_path, 'rt', encoding='UTF-8') # ir a la ruta completa, file (objeto) representa al archive
            data = file.read() #data es contenido
            print(f'El resultado guardado es:\n{data}')
        else:
            print("generando resultado...")
            resultado = calcular_conteos(lista)
            resultado += porcentajes(lista)
            print(f'Guardando resultado del conteo en el fichero {file_path} ...')
            file = open(file_path, 'wt', encoding='UTF-8')
            data = file.write(resultado)
            print(f'El resultado generado es:\n{resultado}')
    except Exception as e:
        print(f'Exception:{e}') #E:write()
    finally:
        file.close()

lista = cargar_datos()
guardar_resultado(lista)
