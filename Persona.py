
#super clase, clase padre
class persona():
    def __init__(self, clave,nombre, edad):
        self.clave = clave
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print("Dejando ver los datos de la super-clase")
        print("CLAVE:", self.clave)
        print("NOMBRE:", self.nombre)
        print("EDAD: ", self.edad)