# Programa: Comparadores_Libros.py
# Objetivo: Definir los metodos comparadores entre libros. (titulo, autor, editorial)
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 15-10-2024

import Clase_Libro as Cl


def titulo(a: Cl.Libro, b: Cl.Libro) -> int:
    """
    Comparador que define como se distinguen 2 libros entre si,
    a partir de su titulo.
    :param a: Libro
    :param b: Libro
    :return: -1 si el titulo del libro a es alfabeticamente menor que
    el titulo de b, 1 en caso contrario y 0 si son titulos identicos.
    """
    if isinstance(a, Cl.Libro) and isinstance(b, Cl.Libro):
        if a.titulo < b.titulo:
            return -1
        elif a.titulo > b.titulo:
            return 1
        else:
            return 0
    else:
        raise TypeError('Los argumentos deben ser objetos "Libros"')


def autor(a: Cl.Libro, b: Cl.Libro) -> int:
    """
    Comparador que define como se distinguen 2 libros entre si,
    a partir de su autor.
    :param a: Libro
    :param b: Libro
    :return: -1 si el autor del libro a es alfabeticamente menor que
    el autor de b, 1 en caso contrario y 0 si son autores identicos.
    """
    if isinstance(a, Cl.Libro) and isinstance(b, Cl.Libro):
        if a.autor < b.autor:
            return -1
        elif a.autor > b.autor:
            return 1
        else:
            return 0
    else:
        raise TypeError('Los argumentos deben ser objetos "Libros"')


def editorial(a: Cl.Libro, b: Cl.Libro) -> int:
    """
    Comparador que define como se distinguen 2 libros entre si,
    a partir de su editorial.
    :param a: Libro
    :param b: Libro
    :return: -1 si la editorial del libro a es alfabeticamente menor que
    la editorial de b, 1 en caso contrario y 0 si son editoriales identicas.
    """
    if isinstance(a, Cl.Libro) and isinstance(b, Cl.Libro):
        if a.editorial < b.editorial:
            return -1
        elif a.editorial > b.editorial:
            return 1
        else:
            return 0
    else:
        raise TypeError('Los argumentos deben ser objetos "Libros"')
