
"""
    Ejercicio 6:
        Modelar la clase Banco:
            - Un banco puede transferir un monto de una cuenta a otra cuenta.
"""
from 01-caja_de_ahorros import CajaDeAhorro as Caja

class Banco():
    """
        Clase Banco
            ✅ transferir(un_monto, una_cuenta, otra_cuenta): transferir un monto de una cuenta a otra cuenta.
    """
    def __init__(self) -> None:
        pass

    def transferirUnMonto(self, un_monto: float, una_cuenta: Caja, otra_cuenta: Caja):
        """ Transfiere un monto de una cuenta a otra cuenta """
        try:
            una_cuenta.extraerUnMonto(un_monto)
            otra_cuenta.depositarUnMonto(un_monto)
        except ValueError as err:
            raise ValueError('Transacción no disponible.')