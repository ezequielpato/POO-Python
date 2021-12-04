"""
    Ejercicio 2:

        Implementar la clase Porcentaje tal que respete el siguiente protocolo:
        👉🏻 valor(unNumero). Indica el valor porcentual que va a representar el objeto.
        👉🏻 aplicarA(unNumero). Retorna el resultado de aplicar el porcentaje a un numero.

        Defina los tests de unidad que considere necesarios para esta clase.
"""

from exeption_porcentaje import DividendoNoPuedeSerCero

class Porcentaje(object):
    """
        Clase Porcentaje
            ✔ valor(unNumero). Indica el valor porcentual que va a representar el objeto.
            ✔ aplicarA(unNumero). Retorna el resultado de aplicar el porcentaje a un numero.
    """

    def __init__(self, unNumero) -> None:
        self.__valor = unNumero

    @property
    def valor(self) -> float: return self.__valor

    def aplicarA(self, unNumero) -> float:
        """ Número al cual se le aplicará el porcentaje """
        if unNumero == 0:
            raise DividendoNoPuedeSerCero
        else:
            return unNumero * self.valor / 100

if __name__ == "__main__":
    porcentaje = Porcentaje(45)
    resultado = porcentaje.aplicarA(0)
    print(f' Representa el % {int(resultado)}')
