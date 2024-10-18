# Programa: Repisa_Lista.py
# Objetivo: Clase que modela una Repisa como una Lista doblemente ligada (es para el estante 3).
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 15-10-2024

import Clase_Nodo as Cn
import Clase_Libro as Cl
import Interfaz_Listable as Il


class RepisaLista(Il.Listable):
    """
    Clase que modela una repisa del tipo Lista.
    """
    def __init__(self):
        """
        Constructor por omision de una repisa com Lista doblemente ligada.
        """
        self.__inicio = None
        self.__final = None
        self.__ne = 0  # para saber cuantos libros tengo

    @property
    def inicio(self) -> Cn.Nodo:
        """
        Metodo GET para devolver el nodo inicio (libro al inicio)
        :return: El nodo (libro) inicio
        :rtype: Cn.Nodo
        """
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio: Cn.Nodo):
        """
        Metodo SET para definir un nuevo inicio
        :param inicio: Cn.Nodo - El nuevo nodo (libro) inicio
        """
        self.__inicio = inicio

    @property
    def final(self) -> Cn.Nodo:
        """
        Metodo GET para devolver el nodo (libro) final
        :return: El nodo (libro) final
        :rtype: Cn.Nodo
        """
        return self.__final

    @final.setter
    def final(self, final: Cn.Nodo):
        """
        Metodo SET para definir un nuevo nodo (libro) final
        :param final: Cn.Nodo - El nuevo nodo (libro) final
        """
        self.__final = final

    @property
    def ne(self) -> int:
        """
        Metodo GET para devolver el numero de libros en la Repisa
        :return: El numero de libros en la Repisa
        :rtype: int
        """
        return self.__ne

    @ne.setter
    def ne(self, ne: int):
        """
        Metodo SET para definir un nuevo numero de libros en la Repisa
        :param ne: int - El nuevo numero de libros en la Repisa
        """
        self.__ne = ne

    def agregar(self, elemento: Cl.Libro):
        """
        Metodo que permite agregar un libro al inicio de la Lista.
        Complejidad: O(1)
        :param elemento: El libro que se va a almacenar en el Nodo
        """
        if self.inicio is None:
            self.inicio = Cn.Nodo(elemento, self.inicio, self.final)
            self.final = self.inicio
            self.ne += 1
        else:
            self.inicio = Cn.Nodo(elemento, self.inicio, self.inicio.anterior)
            self.inicio.siguiente.anterior = self.inicio
            self.ne += 1

    def agregar_final(self, elemento: Cl.Libro):
        """
        Metodo que permite agregar un libro al final de la lista.
        Complejidad: O(1)
        :param elemento: El libro que se va a almacenar en el Nodo
        """
        if self.final is None:
            self.final = Cn.Nodo(elemento, self.inicio, self.final)
            self.inicio = self.final
            self.ne += 1
        else:
            self.final = Cn.Nodo(elemento, self.final.siguiente, self.final)
            self.final.anterior.siguiente = self.final
            self.ne += 1

    def agregar_intermedio(self, elemento: Cl.Libro, posicion: int):
        """
        Metodo que permite insertar un libro en la posicion
        deseada.
        Complejidad: O(n)
        :param elemento: El elemento a insertar,
        :param posicion: La posicion donde se desea insertar
        :return T: El Nodo que se desea insertar, None en caso de que la
        posicion sea un numero menor a 1.
        """
        pos = self.inicio
        c = 1
        if posicion < 1:
            return
        while pos is not None and c < posicion:
            pos = pos.siguiente
            c += 1
        if pos is None:
            self.agregar_final(elemento)
        elif pos == self.inicio:
            self.agregar(elemento)
        else:
            nodo_a = Cn.Nodo(elemento, pos, pos.anterior)
            pos.anterior.siguiente = nodo_a
            pos.anterior = nodo_a
            self.ne += 1

    def agregar_ordenado(self, elem: Cl.Libro, comparador: callable):
        """
        Metodo que permite agregar un libro a la lista de forma que quede ordenada.
        Complejidad: O(1)
        :param elem: El libro que se va a almacenar en el Nodo
        :param comparador: El comparador que se va a utilizar
        """
        pos = self.inicio
        while pos is not None:
            if comparador(elem, pos.elemento) <= 0:
                if pos == self.inicio:
                    self.agregar(elem)
                    return
                else:
                    nodo_a = Cn.Nodo(elem, pos, pos.anterior)
                    pos.anterior.siguiente = nodo_a
                    pos.anterior = nodo_a
                    self.ne += 1
                    return
            pos = pos.siguiente
        self.agregar_final(elem)

    def eliminar(self, elemento: Cl.Libro):
        """
        Metodo que permite eliminar la primera ocurrencia de un libro.
        Complejidad: O(n)
        :param elemento: El libro a eliminar
        :return T: El Nodo que lo contiene, None en caso contrario
        """
        pos = self.inicio
        while pos is not None and not pos.elemento == elemento:
            pos = pos.siguiente
        if pos is None:
            return  # No lo encontro
        if pos == self.inicio:  # Es el inicio de la lista
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = None
            self.ne -= 1
        elif pos == self.final:  # Es el final de la lista
            self.final = self.final.anterior
            self.final.siguiente = None
            self.ne -= 1
        else:
            pos.anterior.siguiente = pos.siguiente
            pos.siguiente.anterior = pos.anterior
            self.ne -= 1

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
        parametro comenzando en inicio.
        Complejidad: O(n).
        :param libro: El libro a buscar
        :return: El Nodo que contiene el elemento, None en caso contrario
        :rtype: Cn.Nodo
        """
        pos = self.__inicio
        while pos is not None and not pos.elemento == libro:
            pos = pos.siguiente
        return pos

    def buscar_final(self, libro: Cl.Libro) -> Cn.Nodo:
        """
        Metodo que busca el Nodo que contiene en el libro pasado como
        parametro comenzando desde final.
        Complejidad: O(n).
        :param libro: El libro a buscar
        :return: El Nodo que contiene el elemento, None en caso contrario
        :rtype: Cn.Nodo
        """
        pos = self.final
        while pos is not None and not pos.elemento == libro:
            pos = pos.anterior
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
        self.__final = None

    def primero(self):
        """
        Metodo que devuelve el primer Libro de la Repisa.
        Complejidad: O(1)
        :return: El primer Libro
        :rtype: Cl.Libro
        """
        if not self.esta_vacia():
            return self.__inicio
        else:
            return None

    def ultimo(self):
        """
        Metodo que devuelve el ultimo Libro de la Repisa.
        Complejidad: O(1)
        :return: El ultimo Libro
        :rtype: Cl.Libro
        """
        if not self.esta_vacia():
            return self.final.elemento
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
        lista = ""
        try:
            while True:
                elem = next(it1)
                lista += str(elem) + "\n"
        except StopIteration:
            pass
        return lista

    def __iter__(self):
        """
        Metodo que permite inicializar el iterador de la Lista
        Nota: Para esta lista solo consideramos el recorrer la lista comenzando
        en el inicio.
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
