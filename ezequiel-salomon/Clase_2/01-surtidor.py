"""
    Ejercicio 1:
        Estación de servicio
            Surtidor
"""

class Surtidor(object):
    """
    Surtidor:
            ✅ Poseen una carga inicialmente en 0
            ✅ Posee una capacidad maxima al instanciarse
            ✅ Sabe si esta vacío
            ✅ Sabe cuanto lugar libre tiene para cargar
            ✅ Puede recibir una carga
    """

    def __init__(self, carga_max: int) -> None:
        self._CARGA_INICIAL = 0
        self._CARGA_MAXIMA = carga_max
        self._estado_vacio = True
        # self._estado_capacidad_libre
        # self._estado_recibe_carga

    @property
    def carga(self) -> int:
        """ Devuelve el valor de su carga inicial """
        return self._CARGA_INICIAL

    @property
    def carga_maxima(self) -> int:
        """ Devuelve el valor de su carga máxima """
        return self._CARGA_MAXIMA

    @property
    def capacidad(self) -> int:
        """ Devuelve su capacidad actual """
        return self._CARGA_MAXIMA - self._CARGA_INICIAL

    @property
    def estado(self) -> bool:
        """ Nos devuelve TRUE si el surtidor se encuentra vacio """
        return self.capacidad == 0

if __name__ == "__main__" :
    surtidor = Surtidor(100)
    print(surtidor.carga)
    print(surtidor.carga_maxima)
    print(surtidor.capacidad)
    print(surtidor.estado)