from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

print(Pessoa.gera_id())
p3 = Pessoa('Ramon', 25)
print(p3.gera_id())