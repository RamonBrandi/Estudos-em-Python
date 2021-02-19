class CarrinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


carrinho = CarrinhoDeCompra()
p1 = Produto('Camiseta', 50)
p2 = Produto('Caneca', 20)
p3 = Produto('Boné', 60)
p4 = Produto('Bandana', 15)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p4)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p1)

carrinho.lista_produtos()
print(f"\nO valor total é: {carrinho.soma()}")

