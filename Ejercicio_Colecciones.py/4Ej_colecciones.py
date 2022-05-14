from random import randint

def rellenar_lista_aleatoria(): #cidades_mes_temperatura
    lista_ciudades = [] 
    for n in range(1,21): 
        temperaturas = {}
        for mes in range(1,13):
            temp = randint(13,35)
            temperaturas[mes] = temp
        ciudad = {'nombre': f'CIUDAD {n:0>2.0f}', 'temperaturas': temperaturas}
        lista_ciudades.append(ciudad)

    return lista_ciudades


def media(lista_de_numeros):
    suma=0 #variable aux para almacenar
    for numero in lista_de_numeros:
        suma= suma+numero
    media = suma / len(lista_de_numeros)
    return media

ciudades = rellenar_lista_aleatoria()

ciudades_medias = {}

for ciudad in ciudades:
    nombre = ciudad.get('nombre')
    temperaturas = ciudad.get('temperaturas').values()
    media_temp = media(temperaturas)
    ciudades_medias[nombre] = media_temp

temp_max = None
ciudad_max = ''
temp_min = None
ciudad_min = ''
for ciudad, temp_media in ciudades_medias.items(): #items: devuelve k,v en tupla
    if temp_max is None or temp_max < temp_media:
        temp_max = temp_media
        ciudad_max = ciudad
    if temp_min is None or temp_min > temp_media:
        temp_min = temp_media
        ciudad_min = ciudad

print(f'{ciudad_max} tiene la media anual mas alta con {temp_max:.0f}º')
print(f'{ciudad_min} tiene la media anual mas baja con {temp_min:.0f}º')
print(f'Las ciudades y sus medias ordenadas son:')
#def mi_funcion(item):
#   return item[1]
#for k, v in sorted(ciudades_medias.items(), key=mi_funcion, reverse= True):
for k, v in sorted(ciudades_medias.items(), key=lambda item: item[1], reverse= True):
    print(f'{k} --> {v:0>2.0f}º')










    