#***
def ProcesoInicial():
    print('Buscar una hoja de papel')

def ProcesoDos():
    print('Doblar la hoja')

def SaludarATodos(*nombres):
    for i in nombres:
        print(f'hola:{i}')

def SaludarATodos(**nombres):
    for i in nombres:
        print(f'hola:{i} {nombres[i]}')


ProcesoInicial()
ProcesoDos()

SaludarATodos('Ana')
SaludarATodos('Cami','Alex','Maria')
SaludarATodos('Crist','Sam','Lu')
SaludarATodos()

