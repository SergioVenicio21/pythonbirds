#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    nome = input('Digite seu nome: ')
    p = Pessoa(nome)
    print(p.comprimentar())
    print(id(p))
