from pickle import TRUE


saludo = 'Hola'
saludo.upper()
print(saludo)
print(saludo.upper())
saludo = saludo.upper()
print(saludo)

#capitalize
c = 'hola mundo'
print(c.capitalize())

print('Hola'.replace('a','o'))

for n in 'a,b,c,d'.split(','):
    print(n)


print('Hola'.replace('a','o').count('lo'))

x = "  Hola, ¿que tal estas? "
print(x.strip().endswith('?'))

a = [23,6,78]
#a.sort() # [6, 23, 78] Ordena una lista de forma ascendente (por defecto)
#a.reverse() #false #[78, 6, 23] .algo es el nombre de la funciín (parametro)
#a.sort(reverse=False) # [6, 23, 78]
a.sort(reverse=True) # [78, 23, 6] Ordenar una lista de forma DESCENDENTE (especifando)

print(a)
a.pop()
#a.insert()

#set
a ='python'
print(f"\nEsto es una cadena")