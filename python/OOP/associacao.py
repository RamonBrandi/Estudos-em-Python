
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    def escrever(self):
        return "caneta está escrevendo...."
    
    @property
    def marca(self):
        return self.__marca

class MaquinaDeEscrever:
    def escrever(self):
        return "Maquina está escrevendo...."


escritor = Escritor('Joao')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

#Fazendo a associação
escritor.ferramenta = maquina
print(escritor.ferramenta.escrever())
