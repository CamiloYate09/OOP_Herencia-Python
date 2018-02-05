from Persona import *

#creando la herencia de la super clase persona
class trabajador(persona):
    def __init__(self,clave, nombre, edad, sueldo):
        self.clave = clave
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo