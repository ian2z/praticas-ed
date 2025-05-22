class No():
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha():
    def __init__(self):
        self.topo = None
    
    def esta_vazia(self):
        return self.topo is None
    
    def empilhar(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.topo
        self.topo = novo_no
    
    def desempilhar(self):
        if self.esta_vazia():
            raise Exception("Erro ao desempilhar => (A pilha está vazia!)")
        dado = self.topo.dado
        self.topo = self.topo.proximo
        return dado

    def mostrar(self):
        atual = self.topo
        while atual:
            print(atual.dado)
            atual = atual.proximo