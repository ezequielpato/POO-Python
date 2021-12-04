import unittest
from Clase_1.banco import Banco
from Clase_1.caja_de_ahorros import CajaDeAhorro as Caja

class TestBanco(unittest.TestCase):
    def setUp(self) -> None:
        self.banco = Banco()
        self.cuenta1 = Caja("ezequiel")
        self.cuenta1.depositarUnMonto(1000)
        self.cuenta2 = Caja("nico")

    def test_elbancoPuedeTrasnferirUnMontoDeUnaCuentaAOtra(self):
        self.assertEqual(self.cuenta2.saldo, 0)

        self.banco.transferirUnMonto(1000,self.cuenta1,self.cuenta2)

        self.assertEqual(self.cuenta2.saldo, 1000)
        self.assertEqual(self.cuenta1.saldo, 0)

    def test_elbancoNoPuedaRealizarLaTransferencia(self):

        self.assertEqual(self.cuenta2.saldo, 0)

        with self.assertRaisesRegex(ValueError, 'Transacción no disponible.'):
            self.banco.transferirUnMonto(1100,self.cuenta1,self.cuenta2)

        self.assertEqual(self.cuenta2.saldo, 0)
        self.assertEqual(self.cuenta1.saldo, 1000)