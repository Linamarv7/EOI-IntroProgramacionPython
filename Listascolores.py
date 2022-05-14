colores=["Red", "Yellow", "Green"]
print(colores[1])
colores.append('Black')
colores.insert(2,'Orange')
print('Lista de colores:',colores)
try:
    color=input('Entre el color para saber su posición:')
    print("Posición del color en la lista ",colores.index(color))
except ValueError:
    print('el color no esta en la lista')

colores.remove


print('Lista de colores actualizada: ',colores)

print('Color en la posición 2:',colores[2])

