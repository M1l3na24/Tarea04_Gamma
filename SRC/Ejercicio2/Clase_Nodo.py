# Programa: Clase_Nodo.py
# Objetivo: Clase que modela Nodo de Lista simplemente y doblemente ligada.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 15-10-2024

class Nodo:
    """
    Clase que representa a los nodos de las listas
    """
    def __init__(self, *params):
        """
        Constructor para los Nodos de la Lista Doblemente Ligadas
        :param params: Si se manda un parametro, es el dato a guardar en la Lista,
                       el siguiente se inicia en None al igual que el anterior.
                       Si se mandan tres parametros, el primero es el dato, el siguiente
                       apunta a otro nodo, y el anterior apunta a otro nodo.

        """
        if len(params) == 1:
            self.elemento = params[0]
            self.siguiente = None
            self.anterior = None
        elif len(params) == 2:  # Para las pilas
            self.elemento = params[0]
            self.siguiente = params[1]
        elif len(params) == 3:
            self.elemento = params[0]
            self.siguiente = params[1]
            self.anterior = params[2]
