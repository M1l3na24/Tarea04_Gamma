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
        self.__repisa1 = Rp.Repisa_Pila()
        self.__repisa2 = Rp.Repisa_Pila()
        self.__repisa3 = Rp.Repisa_Pila()


