# no es necesario list comprehensionp orq es solo una lista
# from random import randint
# mujeres=[]
# hombres=[]

# for n in range(1,101):
#     genero=randint(0,1)
#     if (genero==1):
#         mujeres.append(randint(0,101))
#     else:
#         hombres.append(randint(0,101))
#las sgtes 3 lineas son equivalente a las lineas
genero = [randint(0,1) for n in range(1,101)]
mujeres = [randint(0,101) for ng in genero if g==1]
hombres = [randint(0,101) for g in genero if g==0]
print(mujeres)
print(hombres)

mujeres_mayoresedad=len([n for n in mujeres if n>=18])
print("El nº de mujeres mayores de edad es:",mujeres_mayoresedad)
hombres_menoresedad=len([n for n in hombres if n<18])
print("El nº de hombres menores de edad es:",hombres_menoresedad)

edadmenor_mujer=min(mujeres)
print(f"La mujer con menor edad tiene {edadmenor_mujer} años")
edadmenor_hombre=min(hombres)
print(f"El hombre con menor edad tiene {edadmenor_hombre} años")

edadmayor_mujer=max(mujeres)
print(f"La mujer con mayor edad tiene {edadmayor_mujer} años")
edadmayor_hombre=max(hombres)
print(f"El hombre con mayor edad tiene {edadmayor_hombre} años")

promedio_edadmujeres=0
for i in mujeres:
    promedio_edadmujeres+=i
print("La edad promedio en las mujeres es:",promedio_edadmujeres//len(mujeres))

promedio_edadhombres=0
for i in hombres:
    promedio_edadhombres+=i
print("La edad promedio en los hombres es:",promedio_edadhombres//len(hombres))