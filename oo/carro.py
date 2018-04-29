#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Direcao:
    def __init__(self):
        self.valor = 'norte'

    def virar_direita(self):
        if self.valor == 'norte':
            self.valor = 'leste'
        elif self.valor == 'leste':
            self.valor = 'sul'
        elif self.valor == 'sul':
            self.valor = 'oeste'
        elif self.valor == 'oeste':
            self.valor = 'norte'

    def virar_esquerda(self):
        if self.valor == 'norte':
            self.valor = 'oeste'
        elif self.valor == 'oeste':
            self.valor = 'sul'
        elif self.valor == 'sul':
            self.valor = 'leste'
        elif self.valor == 'leste':
            self.valor = 'norte'

    def calcular_direcao(self):
        return self.valor


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def freiar(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        else:
            self.velocidade = (self.velocidade - self.velocidade)

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