class No():
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        pass

class Fila():
    def __init__(self):
        self.inicio = None
        self.fim = None
        pass

    def vazia(self):
        return self.inicio is None
    
    def enfileirar(self, dado):
        no_novo = No(dado)
        if self.vazia():
            self.inicio = self.fim = no_novo
        else:
            self.fim.proximo = no_novo
            self.fim = no_novo

    def desenfileirar(self):
        if self.vazia():
            raise Exception("Erro ao desenfileirar => (A FILA ESTÁ VAZIA)")
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            self.fim = None
            return dado
    
    def mostrar(self):
        atual = self.inicio
        while atual:
            print(atual.dado)
            atual = atual.proximo