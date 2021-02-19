class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

cliente1 = Cliente('Ramon', 25)
print(cliente1.nome)
cliente1.insere_endereco('Cruzeiro', 'SP')
cliente1.lista_endereco()

cliente2 = Cliente('Fernanda', 24)
print(cliente2.nome)
cliente2.insere_endereco('Passa Quatro', 'MG')
cliente2.lista_endereco()
