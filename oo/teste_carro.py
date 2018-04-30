from unittest import TestCase
from oo.carro import Motor, Direcao


class CarroTestCase(TestCase):
    def test_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def test_freiar(self):
        motor = Motor()
        motor.acelerar()
        motor.freiar()
        self.assertEqual(0, motor.velocidade)

    def test_virar_direita(self):
        direcao = Direcao()
        direcao.virar_direita()
        self.assertEqual('leste', direcao.valor)

    def test_virar_esquerda(self):
        direcao = Direcao()
        direcao.virar_esquerda()
        self.assertEqual('oeste', direcao.valor)
