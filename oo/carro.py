#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
EX:
    >>> motor = Motor()
    >>> direcao = Direcao()
    >>> carro = Carro(direcao, motor)
    >>> carro.motor.acelerar()
    >>> print(carro.direcao.calcular_direcao())
    norte
    >>> carro.direcao.virar_direita()
    >>> print(carro.direcao.calcular_direcao())
    leste
    >>> carro.direcao.virar_direita()
    >>> print(carro.direcao.calcular_direcao())
    sul
    >>> carro.direcao.virar_direita()
    >>> print(carro.direcao.calcular_direcao())
    oeste
    >>> carro.direcao.virar_esquerda()
    >>> print(carro.direcao.calcular_direcao())
    sul
"""

class Direcao:
    ORIENTACAO_DIR = {
        'norte': 'leste', 'leste': 'sul',
        'sul': 'oeste', 'oeste': 'norte'
    }
    ORIENTACAO_ESQ = {
        'norte': 'oeste', 'leste': 'norte',
        'sul': 'leste', 'oeste': 'sul'
    }
    def __init__(self):
        self.valor = 'norte'

    def virar_direita(self):
        self.valor = self.ORIENTACAO_DIR[self.valor]

    def virar_esquerda(self):
        self.valor = self.ORIENTACAO_ESQ[self.valor]


    def calcular_direcao(self):
        return self.valor


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def freiar(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor


if __name__ == '__main__':
    motor = Motor()
    direcao = Direcao()
    carro = Carro(direcao, motor)
    for i in range(5):
        carro.motor.acelerar()

    carro.direcao.virar_direita()
    carro.direcao.virar_direita()
    carro.direcao.virar_direita()
    carro.direcao.virar_esquerda()
    print(carro.motor.velocidade)
    print(carro.direcao.calcular_direcao())
