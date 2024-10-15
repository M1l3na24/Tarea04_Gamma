# Programa: claseProfesor.py
# Objetivo: Clase que modela un Profesor que hereda de Persona
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-09-2024

import clasePersona as cP
from locale import currency, setlocale, LC_MONETARY


class Profesor(cP.Persona):
    """
    Clase que representa una persona del tipo Profesor.
    """

    def __init__(self, nombre_completo: str, celular: int, fecha_cumpleanios: str, email: str, num_profesor: int,
                 tel_oficina: int, sueldo: float, dept_ads: str, carrera: str, grupos: list):
        """
        Constructor para un Profesor, ademas de los datos de una Persona, recibe el numero de profesor,
        telefono de oficina, sueldo, departamento de adscripcion, carrera donde imparte materias,
        y grupos.
        :param nombre_completo:str - El nombre completo del Profesor
        :param celular:int - El celular del Profesor
        :param fecha_cumpleanios:str - La fecha de cumpleanios del Profesor
        :param email:str - EL correo electronico del Profesor
        :param num_profesor:int - El numero de profesor
        :param tel_oficina:int - El telefono del Profesor
        :param sueldo:float - El sueldo del Profesor
        :param dept_ads:str - El departamento del Profesor
        :param carrera:str - La carrera donde imparte materias el Profesor
        :param grupos:list - Los grupos del Profesor
        """
        super().__init__(nombre_completo, celular, fecha_cumpleanios, email)
        self.__num_profesor = num_profesor
        self.__tel_oficina = tel_oficina
        self.__sueldo = sueldo
        self.__dept_ads = dept_ads
        self.__carrera = carrera
        self.__grupos = grupos

    # Metodos GET
    @property
    def num_profesor(self) -> int:
        """
        Metodo para obtener el numero de profesor del Profesor
        :return: El numero de profesor
        :rtype: int
        """
        return self.__num_profesor

    @property
    def tel_oficina(self) -> int:
        """
        Metodo para obtener el numero de oficina del Profesor
        :return: El numero de oficina
        :rtype: int
        """
        return self.__tel_oficina

    @property
    def sueldo(self) -> float:
        """
        Metodo para obtener el sueldo del Profesor
        :return: El sueldo del profesor
        :rtype: int
        """
        return self.__sueldo

    @property
    def dept_ads(self) -> str:
        """
        Metodo para obtener el departamento de adscripcion del Profesor
        :return: El departamento de adscripcion del profesor
        :rtype: str
        """
        return self.__dept_ads

    @property
    def carrera(self) -> str:
        """
        Metodo para obtener la carrera donde imparte materias el Profesor
        :return: La carrera donde imparte materias el Profesor
        :rtype: str
        """
        return self.__carrera

    @property
    def grupos(self) -> list:
        """
        Metodo para obtener la lista de grupos del Profesor
        :return: La lista de grupos del Profesor
        :rtype: list
        """
        return self.__grupos

    # Metodos SET

    @num_profesor.setter
    def num_profesor(self, num_profesor: int):
        """
        Metodo para modificar el numero de profesor del Profesor
        :param num_profesor: El numero de profesor del Profesor
        """
        self.__num_profesor = num_profesor

    @tel_oficina.setter
    def tel_oficina(self, tel_oficina: int):
        """
        Metodo para modificar el telefono de oficina del Profesor
        :param tel_oficina: El telefono de oficina del Profesor
        """
        self.__tel_oficina = tel_oficina

    @sueldo.setter
    def sueldo(self, sueldo: int):
        """
        Metodo para modificar el sueldo del Profesor
        :param sueldo: El sueldo del Profesor
        """
        self.__sueldo = sueldo

    @dept_ads.setter
    def dept_ads(self, dept_ads: str):
        """
        Metodo para modificar el departamento de adscripcion del Profesor
        :param dept_ads: El departamento de adscripcion del Profesor
        """
        self.__dept_ads = dept_ads

    @carrera.setter
    def carrera(self, carrera: str):
        """
        Metodo para modificar la carrera donde imparte clases el Profesor
        :param carrera: La carrera donde imparte clases el Profesor
        """
        self.__carrera = carrera

    @grupos.setter
    def grupos(self, grupos: list):
        """
        Metodo para modificar los grupos donde imparte clases el Profesor
        :param grupos: Los grupos donde imparte clases el Profesor
        """
        self.__grupos = grupos

    # Metodos calculadores
    def __str__(self) -> str:
        """
        Metodo para obtener un Profesor en formato cadena
        :return: El Profesor en formato de impresion
        :rtype: str
        """
        setlocale(LC_MONETARY, "en_US")
        return super().__str__().replace("Persona", "Profesor") + \
            " | Num_profesor: {} | Tel_oficina: {} |  Sueldo: {} | Dept. Ads: {} | Carrera: {} | Grupos: {} |".format(
                self.__num_profesor, self.__tel_oficina, currency(self.__sueldo, grouping=True), self.__dept_ads,
                self.__carrera, self.__grupos)

    # Este metodo se define cuando se desea que los objetos se guarden en un archivo

    def __iter__(self):
        """
        Metodo que devuelve una representacion iterable de un objeto
        :return: La representacion en formato iterable del Profesor
        :rtype: iterable
        """
        return iter([super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email,
                     self.__num_profesor, self.__tel_oficina, self.__sueldo, self.__dept_ads,
                     self.__carrera, self.__grupos])

    # Estos metodos se tienen que agregar cuando se trabajan con objetos en los Conjuntos y lograr
    # que sus objetos sean hasheables

    def __llave(self) -> tuple:
        """
        Metodo privado que permite definir una llave a través de los atributos del objeto
        :return: Una tupla con los atributos del objeto.
        :rtype: tuple
        """
        return (super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email, self.__num_profesor,
                self.__tel_oficina, self.__sueldo, self.__dept_ads, self.__carrera, self.__grupos)

    def __hash__(self) -> int:
        """
        Metodo que internamente llama la funcion hash() para obtener el valor hash del objeto.
        Se utilizan generalmente para una comparacion mas rapida entre los dos objetos,
        ya que los valores hash se comparan directamente en lugar de comparar el valor de cada objeto.
        :return: Un valor entero que corresponde al valor hash del objeto
        :rtype: int
        """
        return hash(self.__llave())

    def __eq__(self, otro) -> bool:
        """
        Metodo que permite definir el criterio de igualdad para dos objetos
        :param otro: El Profesor con el que se va a realizar la comparacion
        :return: True si los Profesores son iguales, False en caso contrario
        :rtype: bool
        """
        if isinstance(otro, Profesor):
            return self.__llave() == otro.__llave()
