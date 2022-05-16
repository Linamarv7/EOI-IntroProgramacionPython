from random import randint
from os import path

def rellenar_lista_aleatoria():
    lista_de_sexo = [] #metodo
    for n in range(100): 
        num = randint(0,1) #generar un numero entre 0 y 1
        if num == 0:
            lista_de_sexo.append("H")
        else:
            lista_de_sexo.append("M")
    return lista_de_sexo

def contar_elementos(lista): #(argumento, esto me lo va a devolver y contar)
    total_h = 0
    total_m = 0
    for valor in lista:
        if valor == "H":
            total_h += 1
        else: #elijo else xq es mas eficiente q el if/elif
            total_m += 1
    return total_h, total_m

def cargar_datos():
    try:
        file_name = 'Datos_ejercicioA1.txt'
        file_path = f'./Ejercicios Ficheros/{file_name}'
        if path.exists(file_path):
            print(f'El fichero {file_name} ya existe')
            file = open(file_path, 'rt', encoding='UTF-8') # ir a la ruta completa, file (objeto) representa al archive
            data = file.read() #data es contenido
            print(f'El contenido del fichero es:\n{data}')
        else:
            print(f'Se va a generar un fichero: {file_path}')
            data = ';'.join(rellenar_lista_aleatoria()) # convierte en cadena una lista
            file = open(file_path, "wt", encoding='UTF-8') # abrir mi archivo en modo escritura- wt
            file.write(data) # file es el archivo y escribo aqui (ejecutar la lista)
            print('Archivo guardado con éxito')
    except Exception as e:
        print(f'Exception:{e}') #E:write() argument must be str, not list
    finally:
        file.close()
    return data.split(';') #lista en str  separada por ;

def guardar_resultado(lista):
    try:
        file_name = 'Resultado_ejercicioA1.txt'
        file_path = f'./Ejercicios Ficheros/{file_name}'
        if path.exists(file_path):
            print(f'El fichero {file_name} está guardado')
            file = open(file_path, 'rt', encoding='UTF-8') # ir a la ruta completa, file (objeto) representa al archive
            data = file.read() #data es contenido
            print(f'El resultado guardado es:\n{data}')
        else:
            print("generando resultado...")
            total_h, total_m = contar_elementos(lista)
            resultado = generar_resultados(total_h, total_m)
            print(f'Guardando resultado del conteo en el fichero {file_path} ...')
            file = open(file_path, 'wt', encoding='UTF-8')
            data = file.write(resultado)
            print(f'El resultado generado es:\n{resultado}')
    except Exception as e:
        print(f'Exception:{e}') #E:write()
    finally:
        file.close()


def generar_resultados(hombres, mujeres):
    resultado = f"Hay {hombres} hombres y {mujeres} mujeres"
    if hombres > mujeres:
        resultado += "\nEl número de hombres es mayor"
    elif hombres < mujeres:
        resultado += "\nEl número de mujeres es mayor"
    else:
        resultado += "\nHay igual número de hombres y mujeres"
    return resultado



lista = cargar_datos()
guardar_resultado(lista)


