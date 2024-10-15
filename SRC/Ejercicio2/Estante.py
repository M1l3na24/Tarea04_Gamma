# Programa: Estante.py
# Objetivo: Clase que modela un Estante.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 10-10-2024

import Repisa_Lista as Rl
import Repisa_Pila as Rp

class Estante:
    def __init__(self):
        """
        Constructor de la clase Estante.
        Por omision se construye un estante con 3 repisas.
        """
        self.__repisa1 = Rp.RepisaPila()
        self.__repisa2 = Rp.RepisaPila()
        self.__repisa3 = Rl.RepisaLista()

    # Metodos Get
    @property
    def repisa1(self):
        """
        Metodo GET para devolver la pila de la primer repisa.
        return: La primer repisa
        :rtype: Rp.RepisaPila
        """
        return self.__repisa1

    @property
    def repisa2(self):
        """
        Metodo GET para devolver la pila de la segunda repisa.
        return: La segunda repisa
        :rtype: Rp.RepisaPila
        """
        return self.__repisa2

    @property
    def repisa3(self):
        """
        Metodo GET para devolver la pila de la tercer repisa.
        return: La tercer repisa
        :rtype: Rp.RepisaPila
        """
        return self.__repisa3

    # Métodos set
    @repisa1.setter
    def repisa1(self, nueva_repisa):
        """
        Metodo que permite establecer una nueva primer repisa
        :param nueva_repisa:
        """
        if isinstance(nueva_repisa, Rp.RepisaPila):
            self.__repisa1 = nueva_repisa
        else:
            raise TypError

    @repisa2.setter
    def repisa2(self, nueva_repisa):
        """
        Metodo que permite establecer una nueva segunda repisa
        :param nueva_repisa:
        """
        if isinstance(nueva_repisa, Rp.RepisaPila):
            self.__repisa2 = nueva_repisa
        else:
            raise TypError

    @repisa3.setter
    def repisa3(self, nueva_repisa):
        """
        Metodo que permite establecer una nueva tercer repisa
        :param nueva_repisa:
        """
        if isinstance(nueva_repisa, Rp.RepisaPila):
            self.__repisa3 = nueva_repisa
        else:
            raise TypError

    def ordenar_en_repisa3(self, comparador: callable):
        """
        Metodo que permitira ordenar los Libros en la repisa 3.
        :param comparador: Es el tipo de comparador que se utilizara para
                           ordenar los Libros.
        :return: Repisa 3 ordenada
        """
        # Mientras la repisa 1 no este vacia
        while not self.__repisa1.esta_vacia():
            libro_sacado = self.__repisa1.pop()
            print(type(libro_sacado))
            self.__repisa3.agregar_ordenado(libro_sacado, comparador)

        # Mientras la repisa 2 no este vacia
        while not self.__repisa2.esta_vacia():
            libro_sacado = self.__repisa1.pop()
            self.__repisa3.agregar_ordenado(libro_sacado, comparador)

    def __str__(self):
        """
        Método que permite imprimir el estante en formato cadena
        :return: La repisa en formato cadena de caracteres
        :rtype: str
        """
        return ("\nRepisa 1: \n" + self.__repisa1.__str__() + "\nRepisa 2: \n" + self.__repisa2.__str__() +
                "\nRepisa 3: \n" + self.__repisa3.__str__() + "\n")