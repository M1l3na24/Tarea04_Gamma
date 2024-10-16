# Programa: Listable.py
# Objetivo: Clase abstracta que permite simular la interfaz para el TAD Lista
# Autor: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 18-10-2024

from abc import abstractmethod, ABCMeta
from typing import TypeVar

T = TypeVar('T')


class Listable(metaclass=ABCMeta):
    @abstractmethod
    def agregar(self, elemento: T):
        """
        Método que permite agregar un elemento al inicio de la Lista.
        Complejidad: O(1)
        :param elemento: El elemento que se va a almacenar en el Nodo
        """
        pass

    @abstractmethod
    def eliminar(self, elemento: T):
        """
        Método que permite eliminar la primera ocurrencia de un elemento.
        Complejidad: O(n^2)
        :param elemento: El elemento a eliminar
        """
        pass

    @abstractmethod
    def contiene(self, elemento: T) -> bool:
        """
        Método que permite saber sí un elemento se encuentra contenido
        dentro de la Lista.
        Complejidad: O(n).
        :param elemento: El elemento a buscar
        :return: True si lo encontró, False en otro caso
        :rtype: bool
        """
        pass

    @abstractmethod
    def buscar(self, elemento: T) -> T:
        """
        Método que busca el Nodo que contiene en el elemento pasado como
        parámetro.
        Complejidad: O(n).
        :param elemento: El elemento a buscar
        :return: El Nodo que contiene el elemento, None en caso contrario
        :rtype: bool
        """
        pass

    @abstractmethod
    def esta_vacia(self) -> bool:
        """
        Método que permite saber sí una Lista está vacía.
        Complejidad: O(1)
        :return: True sí está vacío, False en otro caso.
        :rtype: bool
        """
        pass

    @abstractmethod
    def vaciar(self):
        """
        Método que permite vaciar la Lista Ligada.
        Complejidad: O(1)
        """
        pass

    @abstractmethod
    def primero(self) -> T:
        """
        Método que devuelve el primer Nodo de la Lista.
        Complejidad: O(1)
        """
        pass

    @abstractmethod
    def sustituir(self, original: T, nuevo: T):
        """
        Sustituye el valor actual de un Nodo por otro nuevo. Se usa el
        método buscar para determinar cual es el Nodo que contiene el
        valor buscado.
        Complejidad: O(1)
        :param original: El valor original del Nodo
        :param nuevo: El nuevo valor del Nodo
        :return:
        """
        pass
