#Hacer un programa que procese las temperaturas mensuales de 20 ciudades. Deberá sacar cuál de las ciudades tiene en promedio anual la temperatura más alta y cual la más baja.

#También deberá sacar la lista de las 20 ciudades con el promedio de temperaturas anuales desde la más alta hasta la más baja.



from optparse import Values

from random import randint



ListaCiudades = ['Malaga','Alava','Albacete','Alicante','Almería','Asturias','Avila','Badajoz','Barcelona','Burgos','Cáceres','Cádiz','Cantabria','Castellón','Ceuta','Ciudad Real','Córdoba','Cuenca','Formentera','Girona']

dicc = {}



for ciudad in ListaCiudades: # Recorremos la lista de ciudades

    listatemperaturas = [] # Creamos o "Reseteamos" la lista de temperaturas en cada recorrido del bucle, para que sean diferentes en cada ciudad.



    for i in range(0,12): 

        temperaturas = randint(0,50) # Generamos temperaturas comprendidas entre 0 y 50ºC

        listatemperaturas.append(temperaturas) #Almacenamos las temperaturas en una lista.

    

    dicc[ciudad] = listatemperaturas #Almacenamos en un diccionario el nombre de la ciudad junto a una lista con las temperaturas de enero a diciembre (12)



DiccPromedioAnual={} 



for clave,valor in dicc.items(): # Recorremos el diccionario

    print(f'{clave} -> {valor}') # Mostramos en pantalla los nombres de la ciudad junto a la lista de temperatura de todo el año

    tuplatemperaturas = tuple(valor) # Creamos una tupla con los valores del diccionario

    MediaAnuales = (round(sum(tuplatemperaturas)/12 ,2)) # Hacemos una media de las temperaturas anuales de cada ciudad

    DiccPromedioAnual[clave] = MediaAnuales # Creamos un nuevo diccionario con la ciudad y la temperatura media anual.



MaxProAnual = max(DiccPromedioAnual.values()) # Almacenamos el valor maximo del promedio anual

MinProAnual = min(DiccPromedioAnual.values()) # Almacenamos el vlaor minimo del promedio anual



#Convertimos a lista las claves y valores del diccionario para posteriormente hacer una busqueda del valor del prom max anual.

print(f'\n La ciudad con el promedio anual mas ALTO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MaxProAnual)]} con un promedio de: {MaxProAnual} ºC')



#Convertimos a lista las claves y valores del diccionario para posteriormente hacer una busqueda del valor del prom min anual.

print(f'\n La ciudad con el promedio anual mas BAJO es {list(DiccPromedioAnual.keys())[list(DiccPromedioAnual.values()).index(MinProAnual)]} con un promedio de: {MinProAnual} ºC \n') 





ListaPromedioAnual = list(DiccPromedioAnual.items()) #Convertimos el diccionario en una lista



ListaPromedioAnual.sort(key = lambda x: x[1], reverse=True) # Ordenamos la lista de mayor a menor



print(f'La lista de las ciudades ordenadas es :\n{ListaPromedioAnual}')