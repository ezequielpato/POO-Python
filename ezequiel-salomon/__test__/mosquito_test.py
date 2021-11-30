import unittest
from robot import Robot
from mosquito import Mosquito

class TestMosquito(unittest.TestCase):
    # def setUp(self) -> None:
    #     pass

    def test_mosquitoRecibioDisparo(self):
        robot  = Robot(100)
        mosquito = Mosquito()
        mosquito.inicializar()

        self.assertFalse(mosquito.recibioDisparo())

        robot.dispararAUnObjetivo(mosquito)

        self.assertTrue(mosquito.recibioDisparo())