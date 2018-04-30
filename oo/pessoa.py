#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Pessoa:
    olhos = 2
    pessoas = 0

    def __init__(self, nome, idade, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
        Pessoa.pessoas += 1

    def comprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return True

    @classmethod
    def contador(cls):
        return cls.pessoas


class Homem(Pessoa):
    def comprimentar(self):
        comprimentar = super().comprimentar()
        return f'{comprimentar}. Apertado de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    nome = input('Digite seu nome: ')
    p2 = Pessoa('teste', 23)
    p3 = Pessoa('teste2', 23)
    p4 = Pessoa('teste3', 23)
    p5 = Pessoa('teste4', 23)
    p = Homem(nome, 23, p2, p3, p4, p5)
    print(p.comprimentar())
    print(p2.comprimentar())
