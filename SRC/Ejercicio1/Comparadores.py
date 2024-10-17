# Programa: Comparadores.py
# Objetivo: Definir una serie de comparadores para la Lista Ordenada
# Autor: Gerardo
# Fecha: 11-09-2024

import clasePersona as cP


# Ejemplos de comparadores
def edad_ascendente(a: cP.Persona, b: cP.Persona) -> int:
    """
    Método para determinar la relación de los Empleados con respecto a la edad
    :param a: El primer Empleado a comparar por edad
    :param b: El segundo Empleado a comparar por edad
    :return: Valor positivo si la edad de a es menor que b, cero si son iguales,
             negativo en otro caso
    """
    if a == b:
        return 0
    elif a is None:
        return -1
    elif b is None:
        return 1
    else:
        return a.edad() - b.edad()


def salario_descendente(a: cP.Persona, b: cP.Persona) -> float:
    """
    Método para determinar la relación de los Empleados con respecto al salario
    :param a: El primer Empleado a comparar por salario
    :param b: El segundo Empleado a comparar por salario
    :return: Valor positivo si el salario de b es mayor que a, cero si son iguales,
             negativo en otro caso
    """
    if a == b:
        return 0
    elif a is None:
        return -1
    elif b is None:
        return 1
    else:
        return b.salario - a.salario


def salario_nombre(a: cP.Persona, b: cP.Persona):
    """
    Método para determinar la relación de los Empleados con respecto al salario y nombre
    :param a: El primer Empleado a comparar
    :param b: El segundo Empleado a comparar
    :return: Valor positivo si el salario de a es mayor que b, negativo si el salario de
             b es mayo que a. Si es el mismo salario, regresa la relación de orden de los
             Empleados con respecto al orden natural de las cadenas.
    """
    if a == b:
        return 0
    elif a is None:
        return -1
    elif b is None:
        return 1
    else:
        dif_salario = a.salario - b.salario
        if dif_salario == 0:
            fullname1 = a.nombre + " " + a.apellidos
            fullname2 = b.nombre + " " + b.apellidos
            return __compare_strings(fullname1, fullname2)
        else:
            return dif_salario


def edad_nombre(a: cP.Persona, b: cP.Persona):
    """
    Método para determinar la relación de los Empleados con respecto a la edad y nombre
    :param a: El primer Empleado a comparar
    :param b: El segundo Empleado a comparar
    :return: Valor positivo si la edad de a es mayor que b, negativo si la edad de
             b es mayo que a. Si es la misma edad, regresa la relación de orden de los
             Empleados con respecto al orden natural de las cadenas.
    """
    if a == b:
        return 0
    elif a is None:
        return -1
    elif b is None:
        return 1
    else:
        dif_edad = a.edad() - b.edad()
        if dif_edad == 0:
            fullname1 = a.nombre + " " + a.apellidos
            fullname2 = b.nombre + " " + b.apellidos
            return __compare_strings(fullname1, fullname2)
        else:
            return dif_edad


def nombre_ascendente(a: cP.Persona.nombre_completo, b: cP.Persona.nombre_completo):
    """
    Metodo para determinar la relacion de los Contactos con respecto al nombre.
    :param a: El nombre del primer Contacto a comparar
    :param b: El nombre del segundo Contacto a comparar
    :return: Valor positivo si el nombre de a es mayor que b, negativo si el nombre de
             b es mayo que a. Si es el mismo nombre, regresa un 0.
    """
    dif_nombre = __compare_strings(a, b)
    return dif_nombre


def __compare_strings(str1: str, str2: str) -> int:
    """
    Método privado para comparar dos cadenas y devolver su relación de orden en términos de un int
    :param str1: Primera cadena a comparar
    :param str2: Segunda cadena a comparar
    :return: -1 si str1 lexicográficamente es menor que str2, 0 si son iguales, 1 en otro caso
    """
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0
