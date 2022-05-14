"""
lst1=[1,2,3,4,5]
#lst2=[]
#for n in lst1:
#   lst2.append(n)
lst2=[n for n in lst1]
print(lst2)
"""

#Ejercicio 2
rng=[]
for n in range(1200,2001,130):
    rng=range(1200,2001,130)
lst=[]
for x in rng:
    lst.append(x)

rng=range(1200,2001,130) # es equivalente a las lineas 12,13 y 14
lst=[x for x in rng] # es equivalente a las lineas 18,19 y 20
print(lst) # esto es igual a la linea 21

#Ejer 3
lst1 = [ 44 , 54 , 64 , 74 , 104 ]
lst2 = []
for n in lst1:
    lst2.append(n+6)
print(f"Versión larga: Lista 1: {lst1}\nLista 2: {lst2}")

lst1=[44,54,64,74,104]
lst2 = [n+6 for n in lst1]
print(f"Versión corta: Lista 1: {lst1}\nLista 2: {lst2} ")

#EJER 4
lst1 = [ 2 , 4 , 6 , 8 , 10 , 12 , 14 ]
lst2 = [(num**2) for num un lst1]
print(lst2)

#EJER 5
lst1 = [ 2 , 4 , 6 , 8 , 10 , 12 , 14 ]
for x in lst1:
    if (x**2)>50:
        lst2=lst1.append(x**2)
print(lst2)
lst2=[(x**2) for x in lst1 if (x**2)>50] #equivale a la linea 52,52 y 54 de billiy
print(lst2)

#ejer 6
dict = { "Susuke Ignis" : 985 , "Chevrolet park Activ" : 1100 , "Volkswagen CrossUP" : 1245 , "Masda CX-3" : 1254 , "Susuki Vitara" : 1245 , "Nissan Kicks" : 1310 , "Mazda CX-5" : 1672 , "Ford escape" : 1625 }
lst = [n.upper() for n in dict if dict[n]<1300] #dic n, obtengo el valor; n for n in dic: es la k

print( lst )

#ejer 7
lst = [ "Nueva York" , "FL" , "CA" , "VT" ] #recorrer la lista
lst=["NY", "FL", "CA", "VT"]
dict={}
for n in lst:
    #dict.setdefault(n,n) #crear elementos en mi dicc
    dict[n]=n #otra manera de crear o añadir elemento al dicc, añadimos valor para crear un dic
print(dict)

#version corta, con la lst de comprehensin
dic={n:n for n in lst} #primer n: dict n; 2 n: =n
print(dict)

# JER 8
rng=range(100,161,10)
dict={}
for x in rng:
    dict[x]=(x/100)
print(dict)

#Version with list comprehension
dict={x:x/100 for x in rng} # primer x es la k. Te crea una k, v. equivale a lineas 68 a 70
print(dict)

#EJER 9
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict2={} crear dic, k-v
for n in dict1:
    if dict1[n]>2000: # a la k le asigne  un valor , pero solo si [n] es >2000
        dict2[n]=dict1[n] # creee esta clave asignandole un v dict 1
print(dict2)

dict2={n:dict1[n] for n in dict1 if dict1[n]>2000} # RECOORRE DIC 1 Y SI LA K ES > A 2000 SE GUARDA
print(dict2)

#{"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}

#dict2={x:dict1.get(x) for x in dict1 if dict1.get(x) > 2000}

#print(dict2)
