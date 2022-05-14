# 5 de mayo, colecciones combinacón ##la descerealizacion me devuelve un obj y la sere: un str #tengo q saber si me devuelve si es una cadena de caracreres o una lista q me deveulve un objeto
#impor json, pasar la coleccion al json. para serializar: pasar de obje a json: dumps
import json
#crear lista
citricos=["limon", "naranja", "pomelo", "lima"]
#creo otra variable para pasar, q se conviera en json
citricosJSON=json.dumps(citricos) #pasar dumps serealizacion 
print("json de citricos: ",citricosJSON)
listacitricos = json.loads(citricosJSON) # descerealizacion de dumps a obj, DEVUELVE OBJ
print(listacitricos)
print(type(listacitricos))

# ' ' comillas sencillas me inicia y termina, para poder hacer la represntacion del js. deptosempleados.json
