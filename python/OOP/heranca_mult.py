class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self.ligado = True
        print(f"{self._nome} está ligado")

    def desligado(self):
        if not self._ligado:
            return
        self._ligado = False

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            print(f"{self._nome} não está ligado")
            return
        if self._conectado:
            print(f"{self._nome} já está conectado")
            return

        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            print(f"{self._nome} não está conectado")
            return
        self._conectado = False

smartphone = Smartphone('MOnzofone')
smartphone.conectar()
smartphone.ligar()
