class Persona:
    def __init__(self,nombres,apellidos): #una clase
        self.Nombres = nombres
        self.Apellidos = apellidos

class Alumno(Persona):
    Curso = None
    def __init__(self, nombres, apellidos, curso): #otra clase
        self.Curso = curso
        super().__init__(nombres, apellidos)    