"""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):

Reglas:

- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.

- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.

- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).

- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""

from datetime import datetime

class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = nacionalidad
        self.fecha_regis = None

    def solicitar_nombre_edad(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("La edad no es válida. Ingrese otra edad.")

    def cumpleaños(self):
        self.edad += 1

    def fecha_registro(self):
        if self.fecha_regis is None:
            now = datetime.now()
            self.fecha_regis = now.strftime("%Y/%m/%d %H:%M")
        return self.fecha_regis


persona_1 = Persona("", 0, 4000, "peruana")
persona_1.solicitar_nombre_edad()
persona_2 = Persona("", 0, 6500, "peruana")
persona_2.solicitar_nombre_edad()

persona_1.cumpleaños()
print("La edad actualizada de la primera persona es: {}".format(persona_1.edad))
fecha_regis = persona_1.fecha_registro()
print("La fecha de resgistro de la primera persona es: {}".format(fecha_regis))

persona_2.cumpleaños()
print("\nLa edad actualizada de la segunda persona es: {}".format(persona_2.edad))
fecha_regis = persona_2.fecha_registro()
print("La fecha de resgistro de la segunda persona es: {}".format(fecha_regis))