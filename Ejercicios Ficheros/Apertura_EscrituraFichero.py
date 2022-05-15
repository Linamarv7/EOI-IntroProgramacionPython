file='file_600.txt'
fichero=open(file,"wt",encoding='UTF-8')
contenido="'árbol','limón','naranja'"
fichero.write(contenido)
fichero.close()
print('fin de la cita..')