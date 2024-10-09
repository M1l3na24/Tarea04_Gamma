# Programa: PruebaSecuencia.py
# Objetivo: Clase que modela un Libro.
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-10-2024


class Libro:
    def __init__(self, titulo: str, autor: str, editorial: str, anio_publicacion: int):
        """
        Constructor del objeto Libro que tiene un titulo, autor,
        editorial y anio de publicacion.
        :param titulo - titulo del Libro
        :param autor -  autor que escribio el Libro
        :param editorial - editorial que publico el Libro
        :param anio_publicacion - anio en el que se publico el Libro
        """
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__anio_publicacion = anio_publicacion

    # Metodos GET
    @property
    def titulo(self):
        """
        Metodo para obtener el titulo del Libro
        :return: El titulo del Libro
        :rtype: str
        """
        return self.__titulo

    @property
    def autor(self):
        """
        Metodo para obtener el autor del Libro
        :return: El autor del Libro
        :rtype: str
        """
        return self.__autor

    @property
    def editorial(self):
        """
        Metodo para obtener la editorial del Libro
        :return:La editorial del Libro
        :rtype: str
        """
        return self.__editorial

    @property
    def anio_publicacion(self):
        """
        Metodo para obtener el anio de publicacion del Libro
        :return: El anio de publicacion del Libro
        :rtype: int
        """
        return self.__anio_publicacion

    # Metodos SET
    @titulo.setter
    def titulo(self, titulo: str):
        """
        Metodo para modificar el titulo del Libro
        :param titulo: El titulo del Libro
        """
        self.__titulo = titulo

    @autor.setter
    def autor(self, autor: str):
        """
        Metodo para modificar el autor del Libro
        :param autor: El autor del Libro
        """
        self.__autor = autor

    @editorial.setter
    def editorial(self, editorial: str):
        """
        Metodo para modificar la editorial del Libro
        :param editorial: La editorial del Libro
        """
        self.__editorial = editorial

    @anio_publicacion.setter
    def anio_publicacion(self, anio_publicacion: int):
        """
        Metodo para modificar el anio de publicacion del Libro
        :param anio_publicacion: El anio de publicacion del Libro
        """
        self.__anio_publicacion = anio_publicacion

    def __str__(self):
        """
        Metodo que permite definir un Libro en formato cadena
        :return: El Libro en formato str
        :rtype: str
        """
        return ("Libro: {} {} | Autor: {} | "
                "Editorial: {} | Anio de Publicacion: {}").format(self.__titulo,
                                                                  self.__autor,
                                                                  self.__editorial,
                                                                  self.__anio_publicacion)
