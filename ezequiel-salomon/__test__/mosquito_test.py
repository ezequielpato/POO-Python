import unittest
from Clase_1._03_robot import Robot
from Clase_1._05_mosquito import Mosquito

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