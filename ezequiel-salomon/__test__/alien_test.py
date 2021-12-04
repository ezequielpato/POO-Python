import unittest
from Clase_1.alien import Alien

class TestAlien(unittest.TestCase):
  def setUp(self) -> None:
      self.alien = Alien()

  def test_alienVive(self):
    """ Valida si el Alien se encuentra vivo """
    self.assertTrue(self.alien.estaVivo())

  def test_alienMuere(self):
    """ Valida que el Alien muera cuando energía = 0 """
    self.assertTrue(self.alien.estaVivo())
    self.assertEqual(self.alien.energia,5)

    for i in range(5):
      self.alien.recibirDisparo()

    self.assertFalse(self.alien.estaVivo())
    self.assertEqual(self.alien.energia,0)

  def test_disparo(self):
    """ Valida si el Alien recibe un corchazo """
    self.assertEqual(self.alien.energia,5)

    self.alien.recibirDisparo()

    self.assertEqual(self.alien.energia,4)

  def test_reponerse(self):
    """ Valida si el Alien repone su energía """
    for i in range(2):
      self.alien.recibirDisparo()

    self.assertEqual(self.alien.energia,3)

    self.alien.reponerse()

    self.assertEqual(self.alien.energia,5)

  def test_alReponerseNoPuedeSuperarLas5UnidadesDeEnergia(self):
    """ Valida si el Alien repone su energía """
    self.assertEqual(self.alien.energia,5)

    self.alien.reponerse()

    self.assertEqual(self.alien.energia,5)

  def test_alReponerseNoPuedeSuperarLas5UnidadesDeEnergiaEstandoEn4(self):
    """ Valida si el Alien repone su energía """
    self.alien.recibirDisparo()

    self.assertEqual(self.alien.energia,4)

    self.alien.reponerse()

    self.assertEqual(self.alien.energia,5)


if __name__ == "__main__":
    unittest.main()