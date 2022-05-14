ciudad=input('Introduzca la ciudad')
N=input('Introduzca numero de veces que desea repewtir la ciudad:')
if (N.isdigit()):
    N=int(N)
    print("{}{}".format(ciudad, '\n')*N)
    #PRINT((ciudad+'\n')*N)
else:
    print('Entre un valor numerico valido')