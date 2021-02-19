class Pessoa:
    ano_atual = 2021

    #metodo construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #metodo de instancia
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # método de classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento

        return cls(nome, idade)




print("Metodo de instancia:")
p1 = Pessoa('Ramon', 25)
p1.get_ano_nascimento()
print()

print("Metodo de classe:")
p2 = Pessoa.por_ano_nascimento("Fernanda", 24)
print(p2.idade)