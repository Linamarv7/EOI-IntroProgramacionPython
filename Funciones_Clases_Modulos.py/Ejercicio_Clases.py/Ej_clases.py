class Persona: #def clase con dos variables
    Nombres="" #cuales objetos voy a tener?
    Apellidos=""

    def _init_(self,nombres,apellidos): #parametro, hacer ref al objeto q esta creando la clase
        self.Nombres = nombres
        self.Apellidos = apellidos
    def caminar(self):
        print('caminando')

a = 1
profesor = Persona("Billy","Vanegas") #asignacion atributos o propiedades
# profesor.Nombres="Billy" #setter, asignar a
# profesor.Apellidos="Vanegas"

print(type(profesor.Nombres))

estudiante = Persona("Lina","Vásquez") #perso: variable tipo pers
estudiante.Nombres="Lina"
estudiante.Apellidos="Vasquez"

admon = Persona("Oscar","León")
admon.Nombres="Oscar"
admon.Apellidos="León"

#a = 1
#print(type(a))
print("el profesor es: {} {}".format(profesor.Nombres,profesor.Apellidos)) #getter, lo q saco
print("la estudiante es: {} {}".format(estudiante.Nombres,estudiante.Apellidos))
print("el admon es: {} {}".format(admon.Nombres,estudiante.Apellidos))

print("El estudiante: ",estudiante)
profesor.caminar() # no se pone print porq esta arriba