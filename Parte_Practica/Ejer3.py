"""3. Escribir un programa para gestionar los errores en Python (3 ptos):

Reglas:

- El programa deberá tener una función para ingresar dos datos
por consola.

- Deberá tener una función en el caso haya una división entre cero
mencionar el error.

- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error

- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.

- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente."""

def ingreso_datos():
    while True:
        try:
            var_1 = int(input("Ingrese el primer valor: "))
            var_2 = int(input("Ingrese el segundo valor: "))
            return var_1, var_2
        except ValueError:
            print("El número no es válido. Ingrese otro.")

def division():
    while True:
        try:
            var_1, var_2 = ingreso_datos()
            resultado = var_1 / var_2
            print("El resultado de la división es: {}".format(resultado))
            break
        except ZeroDivisionError:
            print("No se puede dividir entre cero. Pruebe otro número.")

def suma():
    while True:
        try:
            var_1, var_2 = ingreso_datos()
            resultado2 = var_1 + var_2
            print("El resultado de la suma es: {}".format(resultado2))
            break
        except TypeError:
            print("No se puede sumar un string con un dato tipo int. Pruebe otro número.")

def numero_datos():
    n = int(input("Ingrese el número de datos a ingresar en la lista: "))
    datos = []
    for i in range(n):
        while True:
            try:
                dato = float(input(f"Ingrese el dato {i+1}: "))
                datos.append(dato)
                break
            except ValueError:
                print("El número no es válido. Ingrese otro número.")

    while True:
        try:
            indice = int(input("Ingrese el índice para mostrar el dato correspondiente: "))
            print("El dato en el índice", indice, "es:", datos[indice-1])
            break
        except IndexError:
            print("El índice ingresado no está en el rango de la lista. Pruebe otro.")
        except ValueError:
            print("Ingrese un número válido para el índice.")

division()
suma()
numero_datos()