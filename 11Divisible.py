# Si un número ingresado es primo o no. (Un número es primo si es divisible únicamente por 1 y por sí mismo).
num = 0
while num < 2:
    inp = input('Introduce un número: ')
    if inp.isdigit():
        num = int(inp)
    if num > 1:
        #n: divisores q voy probando
        n = 2
        while n < num:
            if num % n == 0:
                print(f'{num} no es un número primo. Es divisible por {n}') 
                break
            n+= 1
        else: 
            print(f'{num} es un número primo')
    else:
        print('El número introducido no es válido')