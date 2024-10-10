# Programa: Estante.py
# Objetivo: Clase que modela un Estante.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-10-2024

import Repisa_Pila as Rp
import Repisa_Lista as Rl


class Estante:
    def __init__(self):
        """
        Constructor de la clase Estante.
        Por omision se construye un estante con 3 repisas.
        """
        self.__repisa1 = Rp.RepisaPila()
        self.__repisa2 = Rp.RepisaPila()
        self.__repisa3 = Rl.RepisaLista()

    def ordenar_repisa3(self, comparador: callable):
        """
        Metodo que permitira ordenar los Libros en la repisa 3.
        :param comparador: Es el tipo de comparador que se utilizara para
                           ordenar los Libros.
        :return: Repisa 3 ordenada
        """
        # Verifico que mis repisas 1 y 2 no esten vacias
        if not self.__repisa1.esta_vacia() and not self.__repisa2.esta_vacia():
            # Aplico politica LIFO
            libro1_sacado = self.__repisa1.pop()
            # verifico si es el primer libro que meto a la repisa 3
            if self.__repisa3.esta_vacia():
                self.__repisa3.agregar(libro1_sacado)
            else: # caso donde ya hay al menos 1 libro en la repisa
                # Primero saco las
                while not self.__repisa1.esta_vacia(): # lo hago m veces
                    libro1 = self.__repisa1.top
                    libro22 = self.__repisa2.top
                # empiezo a comparar para meterlo en orden
                if comparador(libro_x_sacar1, libro_x_sacar2) > 0: # Esta 'ordenado'
                    self.__repisa3.agregar(libro1_sacado)

                elif comparador(libro_x_sacar1, libro_x_sacar2) < 0: # Esta 'desordenado'
                    pass

                else: # == 0 - son el mismo libro
                    pass





        else:
            raise Exception("Hay una de las 2 repisas (1,2) vacia.")
