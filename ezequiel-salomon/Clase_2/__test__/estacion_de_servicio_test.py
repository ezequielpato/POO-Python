import unittest

from estacion_de_servicio import Estacion
from surtidor import Surtidor

class TestEstacionDeServicio(unittest.TestCase):
    def setUp(self) -> None:
        self.estacion = Estacion()
        self.surtidorUno = Surtidor(100)

    """ pass """
    def test_alInstanciarseNoTendraSurtidores(self):
        self.assertListEqual(self.estacion.surtidores, [])

    def test_seAgregaUnSurtidorALaEstacion(self):
        """ pass """
        self.assertListEqual(self.estacion.surtidores, [])
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 0)

        self.estacion.agregarSurtidor(self.surtidorUno)

        self.assertEqual(self.estacion.cantidadDeSurtidores(), 1)
        self.assertListEqual(self.estacion.surtidores, [self.surtidorUno])

    def test_cantidadDeSurtidoresDeUnaEstacionVacia(self):
        """ pass """
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 0)



    """ Estacion con surtidores
        0
        agrega
        x
    """


if  __name__ == '__main__':
    unittest.main()