from datetime import datetime

datenow1 = datetime.now().date() #fecha actual
print("Fecha1: ",datenow1)
print("Año1:",datenow1.year)
print("Mes1:",datenow1.month)
print("Dia1:",datenow1.day)
#print(f"Hora:{datenow2.hour}:{datenow2.minute}") No esta disponivle porque la variable solo contiene la fecha

datenow2 = datetime.now() #fecha completa y hora
print("Fecha2: ",datenow2) #con la ',', se concatena. mas eficiente que '+'
print("Año2:",datenow2.year)
print("Mes2:",datenow2.month)
print("Dia2:",datenow2.day)
print(f"Hora2:{datenow2.hour}:{datenow2.minute}")
print("Hora2:",datenow2.hour)
print("MInuto2:",datenow2.minute)
print("Segundos2:",datenow2.second)
print("Microsegundos2:",datenow2.microsecond)

datenow3 = datetime.now() 
print("Fecha3: ",datenow3) 
print("Año3:",datenow3.year)
print("Mes3:",datenow3.month)
print("Dia3:",datenow3.day)
print(f"Hora3:{datenow3.hour}:{datenow3.minute}")
print("Hora3:",datenow3.hour)
print("MInuto3:",datenow3.minute)
print("Segundos3:",datenow3.second)
print("Microsegundos3:",datenow3.microsecond)


#parse fechas
fecha = "10-11-2022" # esta cadena tiene que ser una fechas numerica
fecha1 = datetime.strptime(fecha,'%m-%d-%Y').date() #sin hora  #strptime: variable para convertir texto en fecha
print("Fecha1:",fecha1)
print(f"Fecha1 {fecha1.day}/{fecha1.month}/{fecha1.year}")

fecha2=datetime.strptime(fecha,'%m-%d-%Y')
print("Fecha2:",fecha2)


#conversion fechas
fecha3=datetime.now()
print("Fecha3:",fecha3)
print("Fecha3:",fecha3.strftime("%A %d %b %Y"))

#para que salga en castellano, hay que darle la ubicación
import locale
locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')

fechacastellano = datetime.now()
print(fechacastellano) #ojo, sale en formato numerico
print("fecha castellano:",fechacastellano.strftime("%A %d %b %Y"))