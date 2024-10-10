# Programa: Repisa_Lista.py
# Objetivo: Clase que modela una Repisa como una Lista doblemente ligada (es para el estante 3).
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-10-2024

import Clase_Nodo as Cn
import Clase_Libro as Cl
import Interfaz_Listable as Il

# HAY QUE MODIFICARLO PORQUE NECESITA SER DOBLEMENTE LIGADA PARA PODER INSERTAR EN ORDEN

class RepisaLista(Il.Listable):
    def __init__(self):
        """
        Constructor por omision de una repisa com Lista simplemente ligada.
        """
        self.__inicio = None

    @property
    def inicio(self) -> Cn.Nodo:
        """
        Metodo GET para devolver el nodo inicio (libro al inicio)
        :return: El nodo (libro) inicio
        :rtype: Cn.Nodo
        """
        return self.__inicio

    def agregar(self, libro: Cl.Libro):
        """
        Metodo que permite agregar un elemento (libro) al inicio de la repisa (lista).
        Complejidad: O(1)
        :param libro: El libro que se va a almacenar en el Nodo
        """
        self.__inicio = Cn.Nodo(libro, self.__inicio)

    def eliminar(self, libro: Cl.Libro):
        """
        Metodo que permite eliminar la primera ocurrencia de un libro.
        Complejidad: O(n^2)
        :param libro: El libro a eliminar
        :return T: El Nodo que lo contiene, None en caso contrario
        """
        pos = self.__inicio
        anterior = None
        while pos is not None and not pos.elemento == libro:
            anterior = pos
            pos = pos.siguiente
        if pos is None:
            return  # No lo encontró
        if pos == self.__inicio:  # Es el inicio de la lista
            self.__inicio = self.__inicio.siguiente
        else:
            anterior.siguiente = pos.siguiente

    def contiene(self, libro: Cl.Libro) -> bool:
        """
        Metodo que permite saber si un libro se encuentra contenido
        dentro de la Repisa.
        Complejidad: O(n).
        :param libro: El libro a buscar
        :return: True si lo encontró, False en otro caso
        :rtype: bool
        """
        return self.buscar(libro) is not None

    def buscar(self, libro: Cl.Libro) -> Cn.Nodo:
        """
        Metodo que busca el Nodo que contiene el libro pasado como
        parametro.
        Complejidad: O(n).
        :param libro: El libro a buscar
        :return: El Nodo que contiene el elemento, None en caso contrario
        :rtype: bool
        """
        pos = self.__inicio
        while pos is not None and not pos.elemento == libro:
            pos = pos.siguiente
        return pos

    def esta_vacia(self) -> bool:
        """
        Metodo que permite saber si una Lista esta vacia.
        Complejidad: O(1)
        :return: True si esta vacio, False en otro caso.
        :rtype: bool
        """
        return self.__inicio is None

    def vaciar(self):
        """
        Metodo que permite vaciar la (Repisa).
        Nota: de vaciarse se 'perderan' los libros que contiene.
        Complejidad: O(1)
        """
        self.__inicio = None

    def primero(self):
        """
        Metodo que devuelve el primer Libro de la Repisa.
        Complejidad: O(1)
        """
        if not self.esta_vacia():
            return self.__inicio
        else:
            return None

    def sustituir(self, original: Cl.Libro, nuevo: Cl.Libro):
        """
        Sustituye un libro por otro nuevo. Se usa el
        metodo buscar para determinar cual es el Nodo que contiene el
        libro buscado.
        Complejidad: O(1)
        :param original: El libro original del Nodo
        :param nuevo: El nuevo libro del Nodo
        :return:
        """
        if not self.esta_vacia():
            nodo = self.buscar(original)
            if nodo is not None:
                nodo.elemento = nuevo
            else:
                print("No se puede realizar la sustitucion\n")
        else:
            print("La lista esta vacia\n")

    def __str__(self):
        """
        Metodo que permite imprimir la Repisa en formato cadena
        :return: Repisa en formato cadena
        """
        # Utilizando el iterador
        it1 = iter(self)
        lista = "Lista: "
        try:
            while True:
                elem = next(it1)
                lista += str(elem) + ", "
        except StopIteration:
            pass
        return lista

    def __iter__(self):
        """
        Metodo que permite inicializar el iterador de la Lista
        :return: Un objeto iterable
        """
        self.pos = self.__inicio
        return self

    def __next__(self) -> int:
        """
        Metodo que permite obtener el siguiente elemento de la Repisa
        :return: El siguiente elemento de la Lista
        :rtype: int
        """
        if self.pos is not None:
            a = self.pos.elemento
            self.pos = self.pos.siguiente
            return a
        else:
            raise StopIteration
