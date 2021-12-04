import unittest

from exepcion_surtidor import ImposibleRealizarUnaCarga
from surtidor import Surtidor

class TestSurtidor(unittest.TestCase):
    def setUp(self) -> None:
        self.surtidor = Surtidor(100)


    def test_surtidorIniciaEnCero(self):
        """ Valida si el surtidor se inicializa en cero """

        self.assertEqual(self.surtidor.carga, 0)

    def test_verificaCapacidadMaximaAlInstanciarse(self):
        """ Valida que posea una capacidad maxima """

        self.assertEqual(self.surtidor.cargaMax, 100)

    def test_verificaQueElSurtidorEstaVacio(self):
        """ Valida que el surtidor sepa si esta vacio """

        self.assertFalse(self.surtidor.carga, 0)

    def test_verificaCargaFaltante(self):
        """ Verifica que pueda devolver el lugar libre que tiene para cargar  """

        self.assertEqual(self.surtidor.carga, 0)
        self.assertEqual(self.surtidor.cargaMax, 100)

        carga_faltante = self.surtidor.cargaFaltante()

        self.assertEqual(carga_faltante, 100 )

    def test_puedeRecibirUnaCarga(self):
        """ Verifica que pueda recibir una carga """
        self.assertEqual(self.surtidor.carga, 0)

        self.surtidor.cargar(50)

        self.assertEqual(self.surtidor.carga, 50)


    def test_unaCargaQueSuperaLaCapacidadPermitidad(self):
        """ pass """
        self.assertEqual(self.surtidor.cargaMax, 100)

        with self.assertRaises(ImposibleRealizarUnaCarga):
            self.surtidor.cargar(101)


if __name__ == '__main__':
    unittest.main()