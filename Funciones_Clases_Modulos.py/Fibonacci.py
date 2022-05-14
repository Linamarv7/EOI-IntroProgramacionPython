def Fibonacci(N):
    if(N==1):
        return 0
    elif(N==2):
        return 1
    else:
        return Fibonacci(N-1)+Fibonacci(N-2)

n=input('Qué num de la seria de Fibonacci quiere?')
try:
    n=int(n)
    serie_Fibonacci=[]
    for i in range(1,n+1):
        r=Fibonacci(i)
        serie_Fibonacci.append(r)
    print(f"el num en esa posición es {r}")
    print("La serie es:",*serie_Fibonacci)
except TypeError:
    print("Num no válido")
else:
    print('error')

