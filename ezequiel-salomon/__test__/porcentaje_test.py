import unittest
from exeption import DividendoNoPuedeSerCero
from porcentaje import Porcentaje


class TestPorcentaje(unittest.TestCase):

  def test_aplicarA(self):
    """ pass """

    unPorcentaje = Porcentaje(45)
    numero = 100

    resultado = unPorcentaje.aplicarA(numero)

    self.assertEqual(resultado,45)

  def test_elDividendoNoPuedeSerCero(self):
    """ pass """

    unPorcentaje = Porcentaje(45)

    with self.assertRaises(DividendoNoPuedeSerCero):
      unPorcentaje.aplicarA(0)


if __name__ == "__main__":
  unittest.main()