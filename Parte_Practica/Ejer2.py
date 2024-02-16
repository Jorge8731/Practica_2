"""2. Usando el concepto de herencia y encapsulación (para saldo) para crear
el siguiente programa (3 ptos):

Reglas:

- Agregar un atributo saldo a la clase persona (ejercicio anterior).

- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada

- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas."""

from datetime import datetime

class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo
        self.nacionalidad = nacionalidad

    def mostrar_saldo(self):
        return self.__saldo

    def transferencia(self, persona_a_transferir, monto):
        if self.__saldo >= monto:
            self.__saldo -= monto
            persona_a_transferir.__saldo += monto
            print("Transferencia exitosa.")
        else:
            print("Saldo insuficiente.")

persona_1 = Persona("Carlos", 19, 4000, "peruana")
persona_2 = Persona("Julia", 25, 6500, "peruana")

monto_a_transferir = 3000

print("Saldo de la primera persona antes de la transferencia: {}".format(persona_1.mostrar_saldo()))
print("Saldo de la segunda persona antes de la transferencia: {}".format(persona_2.mostrar_saldo()))

persona_1.transferencia(persona_2, monto_a_transferir)
print("Saldo de la primera persona después de la transferencia: {}".format(persona_1.mostrar_saldo()))
print("Saldo de la segunda persona después de la transferencia: {}".format(persona_2.mostrar_saldo()))