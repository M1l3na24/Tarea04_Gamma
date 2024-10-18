# Programa: Comparadores.py
# Objetivo: Definir una serie de comparadores para la Lista Ordenada
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 17-10-2024

import clasePersona as cP
import claseProfesor as cPr
import claseCoordinador as cC


# Ejemplos de comparadores
def edad_ascendente(a: cP.Persona, b: cP.Persona) -> int:
    """
    Método para determinar la relación de los Empleados con respecto a la edad
    :param a: El primer Empleado a comparar por edad
    :param b: El segundo Empleado a comparar por edad
    :return: Valor positivo si la edad de a es menor que b, cero si son iguales,
             negativo en otro caso
    """
    return a.edad() - b.edad()


def salario_descendente(a: cP.Persona, b: cP.Persona) -> float:
    """
    Método para determinar la relación de los Empleados con respecto al salario
    :param a: El primer Empleado a comparar por salario
    :param b: El segundo Empleado a comparar por salario
    :return: Valor positivo si el salario de b es mayor que a, cero si son iguales,
             negativo en otro caso
    """
    # solo coordinadores y profesores tienen salarios
    if isinstance(a, cPr.Profesor or cC.Coordinador) and isinstance(b, cPr.Profesor or cC.Coordinador):
        return b.sueldo - a.sueldo
    else:
        return -1  # si alguno de los dos es alumno


def salario_nombre(a: cP.Persona, b: cP.Persona):
    """
    Método para determinar la relación de los Empleados con respecto al salario y nombre
    :param a: El primer Empleado a comparar
    :param b: El segundo Empleado a comparar
    :return: Valor positivo si el salario de a es mayor que b, negativo si el salario de
             b es mayo que a. Si es el mismo salario, regresa la relación de orden de los
             Empleados con respecto al orden natural de las cadenas.
    """
    if isinstance(a, cPr.Profesor or cC.Coordinador) and isinstance(b, cPr.Profesor or cC.Coordinador):
        dif_salario = b.sueldo - a.sueldo
        if dif_salario == 0:
            return __compare_strings(a.nombre_completo, b.nombre_completo)
        else:
            return dif_salario
    else:  # si alguno es alumno solo comparo por nombre
        return __compare_strings(a.nombre_completo, b.nombre_completo)


def edad_nombre(a: cP.Persona, b: cP.Persona):
    """
    Método para determinar la relación de los Empleados con respecto a la edad y nombre
    :param a: El primer Empleado a comparar
    :param b: El segundo Empleado a comparar
    :return: Valor positivo si la edad de a es mayor que b, negativo si la edad de
             b es mayo que a. Si es la misma edad, regresa la relación de orden de los
             Empleados con respecto al orden natural de las cadenas.
    """
    dif_edad = a.edad() - b.edad()
    if dif_edad == 0:
        return __compare_strings(a.nombre_completo, b.nombre_completo)
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
    dif_nombre = __compare_strings(a.nombre_completo, b.nombre_completo)
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
