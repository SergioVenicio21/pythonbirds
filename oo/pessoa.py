#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Pessoa:
    olhos = 2

    def __init__(self, nome, idade, *filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    nome = input('Digite seu nome: ')
    p2 = Pessoa('teste', 23)
    p3 = Pessoa('teste2', 23)
    p4 = Pessoa('teste3', 23)
    p5 = Pessoa('teste4', 23)
    p = Pessoa(nome, 23, p2, p3, p4, p5)
    print(p.comprimentar())
    for filho in p.filhos:
        print(filho.nome)
    print(id(p))
