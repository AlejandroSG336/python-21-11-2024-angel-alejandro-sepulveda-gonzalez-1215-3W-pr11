print("sepulveda gonzalez angel alejandro,1215,3W")
print("")
# Ejercicio 1: Clase Persona
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = value
    @property
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self, value):
        if not isinstance(value, str) or len(value) != 9:
            raise ValueError("El DNI debe ser una cadena de 9 caracteres.")
        self._dni = value
    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"
    def esMayorDeEdad(self):
        return self.edad >= 18
# Ejemplo de uso
try:
    persona = Persona(nombre="Juan", edad=25, dni="12345678Z")
    print(persona.mostrar())
    print("Es mayor de edad:", persona.esMayorDeEdad())
except ValueError as e:
    print(e)
