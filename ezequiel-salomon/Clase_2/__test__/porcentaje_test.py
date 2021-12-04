import unittest

from exeption_porcentaje import DividendoNoPuedeSerCero
from porcentaje import Porcentaje

class TestPorcentaje(unittest.TestCase):
    def setUp(self) -> None:
        porcentaje = Porcentaje(45)

    def test_aplicarA(self):
        """ pass """
        porcentaje = Porcentaje(45)

        resultado = porcentaje.aplicarA(100)

        self.assertEqual(resultado,45)

    def test_elDividendoNoPuedeSerCero(self):
        """ pass """

        porcentaje = Porcentaje(45)

        with self.assertRaises(DividendoNoPuedeSerCero):
            porcentaje.aplicarA(0)


if __name__ == "__main__":
    unittest.main()