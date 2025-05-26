class No ():
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Lista():
    def __init__(self):
        self.head = None
        self.tamanho = 0

    def vazia(self):
        return self.head is None
    
    def __len__ (self):
        return self.tamanho
    
    def inserir_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.head
        self.head = novo_no
        self.tamanho += 1
        print(f"{dado} Inserido no COMEÇO da lista.")
    
    def inserir_final(self, dado):
        novo_no = No(dado)
        if self.vazia():
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1
        print(f"{dado} Inserido no FINAL da lista.")
    
    def remover_inicio(self):
        if self.vazia():
            return "A lista já está vazia!"
        dado_rem = self.head.dado
        self.head = self.head.proximo
        self.tamanho -= 1
        print(f"{dado_rem} Removido do inicio da lista.")
        return dado_rem
    
    def remover_final(self):
        if self.vazia():
            print("A lista está vazia!")
            return None
        elif self.head.proximo is None: #Laço especifico, se houver apenas um elemento na lista.
            dado_rem = self.head.dado
            self.head = None
            self.tamanho -= 1
            print(f"{dado_rem} Removido da lista. Agora a lista está vazia.")
            return None
        
        atual =  self.head
        while atual.proximo.proximo:
            atual = atual.proximo
        
        dado_rem = atual.proximo.dado
        atual.proximo = None
        self.tamanho -= 1
        print(f"{dado_rem} Removido com sucesso da lista")
        return dado_rem
    
    def exibir(self):
        if self.vazia():
            print("Lista vazia!")
            return None
        
        atual = self.head
        while atual:
            print(atual.dado)
            atual = atual.proximo
    
    def buscar2(self, dado):
        laps = Lista()
        lap = 0
        atual = self.head
        if self.vazia():
            print("A fila esta vazia!")
            return None
        else:
            while atual:
                if atual.dado == dado:
                    laps.inserir_inicio(lap)
                    atual.proximo
                else:
                    atual.proximo
            if laps.vazia():
                print(f"Nenhum valor {dado} encontrado na lista.")
                return None
            else:
                print(f"Valor {dado} encontrado na lista, nas posiçoes:")
                return laps.exibir()
            
    def buscar(self, dado_procurado):
        if self.vazia():
            print(f"Busca por {dado_procurado}: Lista vazia.")
            return -1

        atual = self.head
        posicao = 0
        while atual:
            if atual.dado == dado_procurado:
                print(f"'{dado_procurado}' ENCONTRADO na posição {posicao}.")
                return posicao
            atual = atual.proximo
            posicao += 1

        print(f"'{dado_procurado}' NÃO ENCONTRADO na lista.")
        return -1