import unittest
from Clase_1._01_caja_de_ahorros import CajaDeAhorro

class TestCajaDeAhorro(unittest.TestCase):
    def setUp(self) -> None:
        self.caja = CajaDeAhorro('ezequiel')

    def test_laCajaDeAhorroSeInicializaEnCero(self):
        self.assertEqual(self.caja.saldo,0)

    def test_depositarUnMonto(self):
        self.assertEqual(self.caja.saldo,0)

        self.caja.depositarUnMonto(1000)

        self.assertEqual(self.caja.saldo,1000)

    def test_noPuedeExtraerUnMonto(self):
        self.assertFalse(self.caja.puedeExtraerUnMonto(1))

    def test_puedeExtraerUnMontoMenorAlSaldo(self):
        self.caja.depositarUnMonto(1000)

        self.assertTrue(self.caja.puedeExtraerUnMonto(999))

    def test_puedeExtraerUnMontoIgualAlSaldo(self):
        self.caja.depositarUnMonto(1000)

        self.assertTrue(self.caja.puedeExtraerUnMonto(1000))

    def test_extraeUnMonto(self):
        self.caja.depositarUnMonto(1000)

        self.caja.extraerUnMonto(1000)

        self.assertEqual(self.caja.saldo,0)

    def test_alSolicitarUnMontoSuperiorAlSaldonoPuedeExtraerUnMonto(self):
        with self.assertRaisesRegex(ValueError, 'No es posible extraer un monto superior al saldo de cuenta'):
            self.caja.extraerUnMonto(1)