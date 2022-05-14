from random import randint  # modul, y funci (randint), q me va a permitir rellenar
  
personas=[]
for n in range(1,101):
    genero=randint(0,1) #0 H y 1 M
    if (genero ==1):
        personas.append("H")
    else:
        personas.append("M")
print(personas)
#buscar cuantas H y cuantos M son
num_chicos= personas.count("H")
num_chicas= personas.count("M")
print(f'El número de chicos es {num_chicos} y el de chicas es {num_chicas}') 

if num_chicos == num_chicas:
    print('Hay igualdad entre chicos y chicas')
elif num_chicos >num_chicas:
    print('Hay mas chicos que chicas')
else:
    print("Hay mas chicas que chicos")

print(f'El porcenjate de chicos es: {num_chicos}% y el de chicas es: {num_chicas}%')