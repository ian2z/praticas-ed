class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.inicio = None
        self. fim = None
        self.tamanho = 0

    def estaVazio(self):
        return self.tamanho == 0

    def adicionarComeco(self, dado):
        novoNo = No(dado)
        if self.estaVazio():
            self.inicio = self.fim = novoNo
        else:
            novoNo.proximo = self.inicio
            self.inicio.anterior = novoNo
            self.inicio = novoNo
        self.tamanho += 1


