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
        self._capacidad_de_carga
        # self._estado_recibe_carga

    @property
    def carga_inicial(self) -> int:
        """ Devuelve el valor de su carga inicial. """
        return self._CARGA_INICIAL

    @property
    def carga_maxima(self) -> int:
        """ Devuelve el valor de su carga máxima. """
        return self._CARGA_MAXIMA

    @property
    def estaVacio(self) -> int:
        """ Devuelve su estado actual. """
        return self._CARGA_MAXIMA - self._CARGA_INICIAL

    @property
    def estaVacio(self) -> bool:
        """ Devuelve TRUE si el surtidor se encuentra vacio """
        return self.capacidad == 0

    @property
    def puedeRecibirCarga(self) -> int:
        """ Devuelve la capacidad libre que el surtidor tiene para recibir una carga  """
        return self._capacidad_de_carga



if __name__ == "__main__" :
    surtidor = Surtidor(100)
    print(surtidor.carga)
    print(surtidor.carga_maxima)
    print(surtidor.capacidad)
    print(surtidor.estado)