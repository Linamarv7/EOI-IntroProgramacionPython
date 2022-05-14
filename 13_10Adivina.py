palabra_magica= 'lina'
win =  False # condicion de salida del bucle
print("Adivina la palabra")
muestra = []
for n in range(len(palabra_magica)): #longitud de la palabra 4
    muestra.append('_') #relleno con _  la lista q se llama muestra, donde voy adivinar cada palabra
while not win:
    print(muestra)
    letra = input("introduce una letra para averiguar la palabra: ")
    if letra in palabra_magica:
        i = palabra_magica.index(letra) # función, paso un elemento diciéndome la posición
        muestra[i] = letra #uso el index para rellenar la muestra
    if '_' not in muestra:
        win = True #si no quedan __ es porq ha ganado
else:
    print('Has ganado, la palabra es: ')
    print(''.join(muestra))



