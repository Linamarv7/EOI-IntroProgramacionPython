from random import randint

#personas=[]
#for n in range(1,101):
 #   personas.append(randint(0,125))

personas = [randint(0,125) for i in range(1,101)] #equivale a lineas 3 4 5
print(personas)
mayores_edad =len([persona for persona in personas if persona>=18]) #lista>=18 in lista len mirad
print(mayores_edad)
#clasificación
clasificacion_edades = {edad:0 for edad in personas} #creo un dict, y me elimina repeticiones porq en dict no se repite
for n in personas:
    clasificacion_edades[n]+=1 #aqui imprime todas las edades y q me diga cuantas hay de cada
print(clasificacion_edades)
edad_mayor=max(personas)
edad_menor=min(personas)

print("Número de personas con 18 o más años:",mayores_edad)
print("La edad más alta es:",edad_mayor)
print("La edad más baja es:",edad_menor)

for edad in clasificacion_edades:
    print('{:3} -> {:1.2f}%'.format(edad,clasificacion_edades[edad]))