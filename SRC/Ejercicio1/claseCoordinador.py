# Programa: claseCoordinador.py
# Objetivo: Clase que modela un Coordinador que hereda de Persona
# Autores: Milena Rivera, Carlos Barrera, Isaac Garrido, Mayela Rosas
# Version: 09-09-2024

import clasePersona as cP
from locale import currency, setlocale, LC_MONETARY


class Coordinador(cP.Persona):
    """
    Clase que representa una persona del tipo Coordinador.
    """

    def __init__(self, nombre_completo: str, celular: int, fecha_cumpleanios: str, email: str, num_empleado: int,
                 tel_oficina: int, sueldo: float, dept_ads: str, carrera_coordina: str):
        """
        Constructor para un Coordinador, ademas de los datos de una Persona, recibe el numero de empleado,
        telefono de oficina, sueldo, departamento de adscripcion y carrera que coordina.
        :param nombre_completo:str - El nombre completo del Coordinador
        :param celular:int - El celular del Coordinador
        :param fecha_cumpleanios:str - La fecha de cumpleanios del Coordinador
        :param email:str - EL correo electronico del PCoordinador
        :param num_empleado:int - El numero empleado del Coordinador
        :param tel_oficina:int - El telefono del Coordinador
        :param sueldo:float - El sueldo del Coordinador
        :param dept_ads:str - El departamento del Coordinador
        :param carrera_coordina:str - La carrera que coordina el Coordinador
        """
        super().__init__(nombre_completo, celular, fecha_cumpleanios, email)
        self.__num_empleado = num_empleado
        self.__tel_oficina = tel_oficina
        self.__sueldo = sueldo
        self.__dept_ads = dept_ads
        self.__carrera_coordina = carrera_coordina

    # Metodos GET

    @property
    def num_empleado(self) -> int:
        """
        Metodo para obtener el numero de empleado del Coordinador
        :return: El numero de empleado
        :rtype: int
        """
        return self.__num_empleado

    @property
    def tel_oficina(self) -> int:
        """
        Metodo para obtener el numero de oficina del Coordinador
        :return: El numero de oficina
        :rtype: int
        """
        return self.__tel_oficina

    @property
    def sueldo(self) -> float:
        """
        Metodo para obtener el sueldo del Coordinador
        :return: El sueldo del Coordinador
        :rtype: int
        """
        return self.__sueldo

    @property
    def dept_ads(self) -> str:
        """
        Metodo para obtener el departamento de adscripcion del Coordinador
        :return: El departamento de adscripcion del Coordinador
        :rtype: str
        """
        return self.__dept_ads

    @property
    def carrera_coordina(self) -> str:
        """
        Metodo para obtener la carrera que coordina el Coordinador
        :return: La carrera que coordina
        :rtype: str
        """
        return self.__carrera_coordina

    # Metodos SET

    @num_empleado.setter
    def num_empleado(self, num_empleado: int):
        """
        Metodo para modificar el numero de empleado del Coordinador
        :param num_empleado: El numero de empleado del Coordinador
        """
        self.__num_empleado = num_empleado

    @tel_oficina.setter
    def tel_oficina(self, tel_oficina: int):
        """
        Metodo para modificar el telefono de oficina del Coordinador
        :param tel_oficina: El telefono de oficina del Coordinador
        """
        self.__tel_oficina = tel_oficina

    @sueldo.setter
    def sueldo(self, sueldo: int):
        """
        Metodo para modificar el sueldo del Coordinador
        :param sueldo: El sueldo del Coordinador
        """
        self.__sueldo = sueldo

    @dept_ads.setter
    def dept_ads(self, dept_ads: str):
        """
        Metodo para modificar el departamento de adscripcion del Coordinador
        :param dept_ads: El departamento de adscripcion del Coordinador
        """
        self.__dept_ads = dept_ads

    @carrera_coordina.setter
    def carrera_coordina(self, carrera_coordina: str):
        """
        Metodo para modificar la carrera que coordina el Coordinador
        :param carrera_coordina: La carrera que coordina
        """
        self.__carrera_coordina = carrera_coordina

    # Metodos calculadores
    def __str__(self) -> str:
        """
        Metodo para obtener un Coordinador en formato cadena
        :return: El Coordinador en formato de impresion
        :rtype: str
        """
        setlocale(LC_MONETARY, "en_US")
        return super().__str__().replace("Persona", "Coordinador") + \
            " | Num_empleado: {} | Tel_oficina: {} |  Sueldo: {} | Dept. Ads: {} | Carrera Coordina: {} |".format(
                self.__num_empleado, self.__tel_oficina, currency(self.__sueldo, grouping=True), self.__dept_ads,
                self.__carrera_coordina)

    # Este metodo se define cuando se desea que los objetos se guarden en un archivo

    def __iter__(self):
        """
        Metodo que devuelve una representacion iterable de un objeto
        :return: La representacion en formato iterable del Coordinador
        :rtype: iterable
        """
        return iter([super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email,
                     self.__num_empleado, self.__tel_oficina, self.__sueldo, self.__dept_ads,
                     self.__carrera_coordina])

    # Estos metodos se tienen que agregar cuando se trabajan con objetos en los Conjuntos y lograr
    # que sus objetos sean hasheables

    def __llave(self) -> tuple:
        """
        Metodo privado que permite definir una llave a través de los atributos del objeto
        :return: Una tupla con los atributos del objeto.
        :rtype: tuple
        """
        return (super().nombre_completo, super().celular, super().fecha_cumpleanios, super().email, self.__num_empleado,
                self.__tel_oficina, self.__sueldo, self.__dept_ads, self.__carrera_coordina)

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
        if isinstance(otro, Coordinador):
            return self.__llave() == otro.__llave()
