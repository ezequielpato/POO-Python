import unittest
from robot import Robot
from alien import Alien

class TestRobot(unittest.TestCase):
    # def setUp(self) -> None:

    def test_elRobotDecrementaLaBateriaAlCaminar(self):
        """ cada 10 metros se resta una unidad de su bateria"""

        robot = Robot(100)

        self.assertEqual(robot.bateria,100)

        robot.caminar(100)

        self.assertEqual(robot.bateria, 90)

    def test_alCaminarlasUnidadesAUtilizarNoPuedenSuperarLaBateriaDelRobot(self):
        """ pass """

        robot = Robot(9)

        self.assertEqual(robot.bateria,9)

        with self.assertRaisesRegex(ValueError, 'no hay bateria suficiente'):
            robot.caminar(100)
        self.assertEqual(robot.bateria, 9)

    def test_elRobotPuedeCargarSuBateria(self):

        robot = Robot(0)

        self.assertEqual(robot.bateria, 0)

        robot.cargarBateria(50)

        self.assertEqual(robot.bateria, 50)

    def test_elRobotNoPuedeCargarMasDe100Unidades(self):
        """ pass """

        robot = Robot(99)

        self.assertEqual(robot.bateria, 99)

        robot.cargarBateria(2)

        self.assertEqual(robot.bateria, 100)

    def test_dispararLeConsumeEl10PorCientoDeSuBateria(self):
        """ pass """
        alien = Alien()
        robot = Robot(100)

        self.assertEqual(alien.energia, 5)
        self.assertEqual(robot.bateria, 100)


        robot.dispararAUnObjetivo(alien)

        self.assertEqual(robot.bateria, 90)
        self.assertEqual(alien.energia, 4)

    def test_elRobotCaminaEnReversaYDecrementaLaBateria(self):
        """ pass """
        robot = Robot(100)

        self.assertEqual(robot.bateria, 100)

        robot.caminar(-100)

        self.assertEqual(robot.bateria, 90)



















if __name__ == '__main__':
    unittest.main()