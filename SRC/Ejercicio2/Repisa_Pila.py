# Programa: Repisa_Pila.py
# Objetivo: Clase que modela una Repisa como una Pila (es para el estante 1 y 2).
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-10-2024

import Interfaz_Apilable as Ia
import Clase_Libro as Cl
import Clase_Nodo as Cn


class RepisaPila(Ia.Apilable):
    def __init__(self):
        """
        Constructor que inicializa una repisa vacia como una Pila.
        Los nodos son libros.
        """
        self.__top = None

    @property
    def top(self) -> Cn.Nodo:
        """
        Metodo GET para devolver el nodo top (libro que este en el tope)
        :return: El nodo inicio
        :rtype: n.Nodo
        """
        return self.__top

    def push(self, libro: Cl.Libro):
        """
        Metodo que permite agregar un elemento en el tope de la Pila.
        (Agregar un libro a la Repisa)
        Complejidad: O(1)
        :param libro: El elemento que se va a almacenar en el Nodo
        """
        self.__top = Cn.Nodo(libro, self.__top)

    def pop(self):
        """
        Metodo que permite eliminar el elemento que se encuentra en el
        tope de la Pila. (Sacar un libro de la Repisa con la politica LIFO)
        Complejidad: O(1)
        :return: El elemento del tope de la Pila, None si la pila esta vacia
        :rtype: Cl.Libro
        """
        if self.esta_vacia():
            return None
        dato = self.__top.elemento
        self.__top = self.__top.siguiente
        return dato

    def tope(self):
        """
        Metodo que devuelve el elemento que esta en el tope de la Pila, sin
        eliminarlo. (Saber cual es el libro que puedo sacar.)
        Complejidad: O(1).
        :return: El elemento del tope de la Pila, None si la pila esta vacia
        :rtype: T
        """
        if self.esta_vacia():
            return None
        dato = self.__top.elemento
        return dato

    def esta_vacia(self) -> bool:
        """
        Metodo que permite saber si una Pila esta vacia.
        (Saber si mi repisa esta vacia)
        Complejidad: O(1)
        :return: True si esta vacio, False en otro caso.
        :rtype: bool
        """
        return self.__top is None

    def vaciar(self):
        """
        Metodo que permite vaciar la Pila.
        (Vaciar la Repisa)
        Complejidad: O(1)
        """
        self.__top = None

    def contiene(self, libro: Cl.Libro) -> bool:
        """
        Metodo que permite saber si un elemento se encuentra contenido
        dentro de la Pila. Este metodo no afecta el estado de la Pila
        (Verificar que un libro esta en la repisa)
        Complejidad: O(n).
        :param libro: El libro a buscar
        :return: True si lo encontro, False en otro caso.
        :rtype: bool
        """
        return self.buscar(libro) is not None

    def buscar(self, libro: Cl.Libro) -> Cn.Nodo:
        """
        Metodo que busca el Nodo que contiene en el elemento pasado como
        parametro. Este metodo no afecta el estado de la Repisa.
        Complejidad: O(n).
        :param libro: El elemento a buscar
        :return: El Nodo que contiene el elemento, None en caso contrario
        :rtype: bool
        """
        pos = self.__top
        while pos is not None and not pos.elemento == libro:
            pos = pos.siguiente
        return pos

    def __str__(self):
        """
        Método que permite imprimir una Repisa en formato cadena
        :return: La Repisa en formato cadena de caracter
        :rtype: str
        """
        # Utilizando el iterador
        it1 = iter(self)
        pila = ""
        try:
            while True:
                elem = next(it1)
                pila += str(elem) + "\n "
        except StopIteration:
            pass
        return pila

    def __iter__(self):
        """
        Metodo que permite inicializar el iterador de la Repisa
        :return: Un objeto iterable
        """
        self.pos = self.__top
        return self

    def __next__(self) -> Cl.Libro:
        """
        Metodo que permite obtener el siguiente elemento (libro) de la Repisa
        :return: El siguiente elemento de la Lista
        :rtype: T
        """
        if self.pos is not None:
            a = self.pos.elemento
            self.pos = self.pos.siguiente
            return a
        else:
            raise StopIteration
