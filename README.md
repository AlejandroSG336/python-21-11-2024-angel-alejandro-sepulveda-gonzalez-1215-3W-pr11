# python-21-11-2024-angel-alejandro-sepulveda-gonzalez-1215-3W-pr11

1-

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

![image](https://github.com/user-attachments/assets/0b6464c3-c8e2-4216-90b6-14b0efb1b98d)
![image](https://github.com/user-attachments/assets/c02388bd-764a-475c-8b32-ec5e0e3a952d)
![image](https://github.com/user-attachments/assets/939526f2-5b65-4c1d-acbb-4dff138b91e7)


2-

print("sepulveda gonzalez angel alejandro,1215,3W")
print("")
# Ejercicio 2: Clase Cuenta
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


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        # Validar que titular sea una instancia de Persona
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una instancia de la clase Persona.")
        self.titular = titular
        self._cantidad = float(cantidad)

    @property
    def cantidad(self):
        return self._cantidad

    def ingresar(self, cantidad):
        # Solo permite ingresar cantidades positivas
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        # Permite retirar cualquier cantidad, incluso dejando saldo negativo
        self._cantidad -= cantidad

    def mostrar(self):
        # Devuelve un mensaje con los datos de la cuenta
        return f"Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad:.2f}"


# Ejemplo de uso
try:
    persona1 = Persona("Juan Pérez", 30, "12345678A")
    cuenta = Cuenta(persona1, 500.0)

    print(cuenta.mostrar())  # Mostrar datos iniciales
    cuenta.ingresar(200)     # Ingresar 200
    cuenta.retirar(100)      # Retirar 100
    print(cuenta.mostrar())  # Mostrar datos actualizados
except Exception as e:
    print(f"Error: {e}")

![image](https://github.com/user-attachments/assets/ae431f1b-2925-44b5-aec4-2a18e0f5641e)
![image](https://github.com/user-attachments/assets/95fce7cb-ba42-478a-b2b7-2021f752f896)
![image](https://github.com/user-attachments/assets/f8a87c37-5eac-4c78-947c-0e4bbc5bae52)
![image](https://github.com/user-attachments/assets/35c02044-61a3-4396-9c88-89c8f0187983)

3-

print("sepulveda gonzalez angel alejandro,1215,3W")
print("")
# Ejercicio 3: Clase CuentaJoven 
# Clase Persona
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


# Clase Cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una instancia de la clase Persona.")
        self.titular = titular
        self._cantidad = float(cantidad)

    @property
    def cantidad(self):
        return self._cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad

    def mostrar(self):
        return f"Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad:.2f}"


# Clase CuentaJoven
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("La bonificación debe ser un número positivo.")
        self._bonificacion = value

    def esTitularValido(self):
        return self.titular.esMayorDeEdad() and self.titular.edad < 25

    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            raise PermissionError("El titular no es válido para retirar dinero.")

    def mostrar(self):
        return (f"Cuenta Joven\nTitular: {self.titular.mostrar()}, "
                f"Cantidad: {self.cantidad:.2f}, Bonificación: {self.bonificacion}%")

# Ejemplo de uso
try:
    persona1 = Persona("Ana López", 22, "87654321B")  # Titular válido
    cuenta_joven = CuentaJoven(persona1, 1500.0, 5.0)  # Creación de Cuenta Joven

    print(cuenta_joven.mostrar())  # Mostrar datos iniciales
    cuenta_joven.ingresar(500)     # Ingresar 500
    cuenta_joven.retirar(300)      # Retirar 300
    print(cuenta_joven.mostrar())  # Mostrar datos actualizados

    persona2 = Persona("Carlos Sánchez", 30, "12345678C")  # Titular no válido
    cuenta_joven_no_valida = CuentaJoven(persona2, 2000.0, 3.0)
    cuenta_joven_no_valida.retirar(100)  # Esto generará un error
except Exception as e:
    print(f"Error: {e}")

![image](https://github.com/user-attachments/assets/a6a1c79f-3333-49a0-89ba-8eafeb379df9)
![image](https://github.com/user-attachments/assets/df3e5afa-5b7c-4b5d-97d6-16ce8c75913c)
![image](https://github.com/user-attachments/assets/26ba9b8a-c433-47f3-8546-d8f2e0472430)
![image](https://github.com/user-attachments/assets/b9c50373-2489-4cd8-b9b3-400659823eba)
![image](https://github.com/user-attachments/assets/bfae306d-32f4-4322-ad42-40c2fc996e94)
