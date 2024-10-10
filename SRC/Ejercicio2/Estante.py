# Programa: Estante.py
# Objetivo: Clase que modela un Estante.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 10-10-2024

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

    def ordenar_en_repisa3(self, comparador: callable):
        """
        Metodo que permitira ordenar los Libros en la repisa 3.
        :param comparador: Es el tipo de comparador que se utilizara para
                           ordenar los Libros.
        :return: Repisa 3 ordenada
        """
        # Comienza sacando libros de la repisa 1

        # Verifico que mi repisas 1 no este vacias
        if not self.__repisa1.esta_vacia():
            # Aplico politica LIFO
            libro1_sacado = self.__repisa1.pop()
            # verifico si es el primer libro que meto a la repisa 3
            if self.__repisa3.esta_vacia():
                self.__repisa3.agregar(libro1_sacado)
            else:  # caso donde ya hay al menos 1 libro en la repisa
                while not self.__repisa1.esta_vacia():  # lo hago m veces
                    libros = self.__repisa3
                    libro2 = self.__repisa1.top
                # empiezo a comparar para meterlo en orden
                    for i in range(libros.ne):

                        if comparador(libros[i], libro2) > 0:
                            posicion =
                            self.__repisa3.agregar(libro2) # lo agrego antes (libro2, libro1)
                    elif comparador(libro1, libro2) < 0: # lo agrego despues  (libro1, libro2)
                        self.__repisa3.agregar_intermedio(libro2,i)



                    else:  # == 0 - son el mismo libro

        else:
            raise Exception("Hay una de las 2 repisas (1,2) vacia.")
