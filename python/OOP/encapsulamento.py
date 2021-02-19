# public, private, protected

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def delete_clientes(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Ottavio')
bd.inserir_cliente(2, 'Ramon')
bd.inserir_cliente(3, 'Fernanda')
bd.inserir_cliente(4, 'Matirdi')
bd.__dados = 'outra coisa'
bd.lista_clientes()