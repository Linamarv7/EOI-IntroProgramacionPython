#CON LA DESCEREALIZACION PODRE RECORRER EL JSON, LISTA
import json
jsonventas='{"departamento": 8,"nombredepto":"Ventas","director":"Juan Rodriguez","empleados:[{"nombre":"Camilo","apellido":"Vasquez"}'
print(jsonventas)
datosDepartamento=json.dumps(jsonventas) #esto ya es un str, lo q me devuelve DUMPS SIEMPRE DEVUELVE STR
print("json 1",datosDepartamento)
print(type(datosDepartamento)) #gestion del str, devolver un str