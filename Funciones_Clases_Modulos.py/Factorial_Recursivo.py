#en py las funciones van de primero
def Factorial(N):
    if (N<=0):
        raise #generar una excepción
    if (N<=1):
        print('return') #hacer un llamado para ver laoa pasos
        return 1
    else:
        print('return {} Factorial({}-1)'.format(N,N))
        return N * Factorial(N-1)

n=input("Desea calcular el favotrial de (Entre un número): ")
try:
    n=int(n)
    r=Factorial(n)
    print("El factorial de:", n," es",r)
except TypeError:
    print('Entre un núm válido')