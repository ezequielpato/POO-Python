import unittest
from surtidor import Surtidor

class TestSurtidor(unittest.TestCase):
    def setUp(self) -> None:
        self.surtidor = Surtidor()

    def test_surtidor(self):
        """ Valida si el surtidor se inicializa en 0 """
        self.assertEqual(self.surtidor.carga,0)