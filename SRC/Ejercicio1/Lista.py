# Programa: ListaEmpleadoOrden.py
# Objetivo: Clase abstracta que permite simular la interfaz para el TAD Lista.
#           Se implementa la "interfaz" Listable. La Lista se crea con comparadores
# Autor: Gerardo Avilés
# Version: 09-09-2024

import Nodo as No
import Listable as Li


class Lista(Li.Listable):
    def __init__(self, comparador):
        """
        Constructor por omisión de la clase Lista
        """
        self.__inicio = None
        self.__comparador = comparador

    @property
    def inicio(self) -> No.Nodo:
        """
        Método GET para devolver el nodo inicio
        :return: El nodo inicio
        :rtype: n.Nodo
        """
        return self.__inicio

    @inicio.setter
    def inicio(self, nodo: No.Nodo):
        """
        Método para establecer el valor del centinela Inicio
        :param nodo: El nodo al que debe apuntar
        """
        self.__inicio = nodo

    def agregar(self, elemento):
        if self.esta_vacia():
            self.__inicio = No.Nodo(elemento, self.__inicio)
        else:
            if self.__comparador(elemento, self.__inicio.elemento) <= 0:  # El elemento que llega es menor
                self.__inicio = No.Nodo(elemento, self.__inicio)
            else:
                pos = self.__inicio.siguiente
                ant = self.__inicio
                while pos is not None and self.__comparador(pos.elemento, elemento) <= 0:
                    ant = pos
                    pos = pos.siguiente
                ant.siguiente = No.Nodo(elemento, pos)

    def eliminar(self, elemento):
        """
        Método que permite eliminar la primera ocurrencia de un elemento.
        Complejidad: O(n^2)
        :param elemento: El elemento a eliminar
        :return T: El Nodo que lo contiene, None en caso contrario
        """
        pos = self.__inicio
        anterior = None
        while pos is not None and not pos.elemento == elemento:
            anterior = pos
            pos = pos.siguiente
        if pos is None:
            return  # No lo encontró
        if pos == self.__inicio:  # Es el inicio de la lista
            self.__inicio = self.__inicio.siguiente
        else:
            anterior.siguiente = pos.siguiente

    def contiene(self, elemento) -> bool:
        """
        Método que permite saber sí un elemento se encuentra contenido
        dentro de la Lista.
        Complejidad: O(n).
        :param elemento: El elemento a buscar
        :return: True si lo encontró, False en otro caso
        :rtype: bool
        """
        return self.buscar(elemento) is not None

    def buscar(self, elemento) -> No.Nodo:
        """
        Método que busca el Nodo que contiene en el elemento pasado como
        parámetro.
        Complejidad: O(n).
        :param elemento: El elemento a buscar
        :return: El Nodo que contiene el elemento, None en caso contrario
        :rtype: bool
        """
        pos = self.__inicio
        while pos is not None and not pos.elemento == elemento:
            pos = pos.siguiente
        return pos

    def esta_vacia(self) -> bool:
        """
        Método que permite saber sí una Lista está vacía.
        Complejidad: O(1)
        :return: True sí está vacío, False en otro caso.
        :rtype: bool
        """
        return self.__inicio is None

    def vaciar(self):
        """
        Método que permite vaciar la Lista Ligada.
        Complejidad: O(1)
        """
        self.__inicio = None

    def primero(self):
        """
        Método que devuelve el primer Nodo de la Lista.
        Complejidad: O(1)
        """
        if not self.esta_vacia():
            return self.__inicio.elemento
        else:
            return None

    def sustituir(self, original, nuevo):
        """
        Sustituye el valor actual de un Nodo por otro nuevo. Se usa el
        método buscar para determinar cual es el Nodo que contiene el
        valor buscado.
        Complejidad: O(1)
        :param original: El valor original del Nodo
        :param nuevo: El nuevo valor del Nodo
        :return:
        """
        if not self.esta_vacia():
            nodo = self.buscar(original)
            if nodo is not None:
                nodo.elemento = nuevo
            else:
                print("No se puede realizar la sustitución\n")
        else:
            print("La lista está vacía\n")

    def __str__(self):
        """
        Método que permite imprimir una Lista en formato cadena
        :return:
        """
        # Utilizando el iterador
        it1 = iter(self)
        lista = "Lista: \n"
        try:
            while True:
                elem = next(it1)
                lista += str(elem) + "\n"
        except StopIteration:
            pass
        return lista

    def __iter__(self):
        """
        Método que permite inicializar el iterador de la Lista
        :return: Un objeto iterable
        """
        self.pos = self.__inicio
        return self

    def __next__(self):
        """
        Método que permite obtener el siguiente elemento de la Lista
        :return: El siguiente elemento de la Lista
        :rtype: int
        """
        if self.pos is not None:
            a = self.pos.elemento
            self.pos = self.pos.siguiente
            return a
        else:
            raise StopIteration
