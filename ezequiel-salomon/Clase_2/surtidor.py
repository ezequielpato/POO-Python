"""
    Ejercicio 1:
        Estación de servicio
        Surtidor:
            ✅ Poseen una carga inicialmente en 0
            ✅ Posee una capacidad maxima al instanciarse
            ✅ Sabe si esta vacío
            ✅ Sabe cuanto lugar libre tiene para cargar
            ✅ Puede recibir una carga
"""

from exepcion_surtidor import ImposibleRealizarUnaCarga

class Surtidor():
    def __init__(self, carga_max:int) -> None:
        self.__carga = 0
        self.__CARGAMAX = carga_max

    @property
    def carga(self):  return self.__carga
    @property
    def cargaMax(self): return self.__CARGAMAX

    def estaVacio(self) -> bool:
        return self.carga == 0

    def cargaFaltante(self) -> int:
        """ Devuelve la carga faltante """
        return self.cargaMax - self.carga

    def cargar(self, una_carga:int) -> None:
        """ Le agrega una carga al surtidor """
        if una_carga + self.carga <= self.cargaMax:
            self.__carga += una_carga
        else:
            raise ImposibleRealizarUnaCarga


if __name__ == "__main__":
    pass