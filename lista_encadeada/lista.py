class No():
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
    
    def consultar(self, indicie):
        if self.vazia():
            print("A lista está vazia!")
            return None
        elif self.tamanho <= indicie:
            print(f"O indicie é maior que a lista, tamanho da lista: {self.tamanho}")
            return None
        else:
            atual = self.head
            for i in range(indicie):
                atual = atual.proximo
            print(f"Valor na posição {indicie}: {atual.dado}")
            return atual.dado
        
    def inserir_em(self, indicie, dado):
        if indicie < 0 or indicie > self.tamanho:
            print("Índicie fora dos limites da lista.")
            return None
        if indicie == 0:
            self.inserir_inicio(dado)
        elif indicie == self.tamanho:
            self.inserir_final(dado)
        else:
            novo_no = No(dado)
            atual = self.head
            for i in range(indicie - 1):
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
            self.tamanho += 1
            print(f"{novo_no.dado} Inserido na posição {indicie} da lista.")
            return novo_no.dado
        
    def buscar_todos(self, dado_procurado):
        if self.vazia():
            print(f"Não foi possível encontrar {dado_procurado} na lista: LISTA VAZIA")
        posicoes = Lista()
        pos = 0
        p = self.head
        while p.proximo:
            if p.dado == dado_procurado:
                posicoes.inserir_final(pos)
            p = p.proximo
            pos += 1
        if posicoes.vazia():
            print(f"Não foi encontrado nenhum dado: {dado_procurado} na lista.")
        else:
            print(f"{dado_procurado} encontrado nas posiçoes:")
        return posicoes.exibir()
    
    def buscar_todos2(self, dado_procurado):
        if self.vazia():
            print(f"Busca por '{dado_procurado}': Lista vazia.")
            return []

        atual = self.head
        posicoes = []
        pos = 0

        while atual:
            if atual.dado == dado_procurado:
                posicoes.append(pos)
            atual = atual.proximo
            pos += 1

        if not posicoes:
            print(f"'{dado_procurado}' NÃO ENCONTRADO na lista.")
        else:
            print(f"'{dado_procurado}' ENCONTRADO nas posições: {posicoes}")

        return posicoes
    
    def remover_em(self, indicie):
        if self.vazia():
            print("A lista está vazia!")
            return None
        elif indicie > self.tamanho or indicie <= 0:
            print(f"Indicie maior que a lista, tamanho da lista: {self.tamanho}")
            return None
        elif indicie == 0:
            self.remover_inicio()
        else:
            atual = self.head
            for i in range(indicie -1):
                atual = atual.proximo
            removido = atual.proximo.dado
            atual.proximo = atual.proximo.proximo
            print(f"Dado: {removido} removido da lista com sucesso.")
            return None

    
    def __str__(self):
        saida = '['
        p = self.__inicio
        while p != None:
            saida += f'{p.dado}'
            p = p.prox
            if p != None:
                saida += ' '
        saida += ']'
        return saida