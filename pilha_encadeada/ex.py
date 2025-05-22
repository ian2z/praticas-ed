from pilha import *

print("=== PILHA ===")
pilha = Pilha()
pilha.empilhar("A")
pilha.empilhar("B")
pilha.empilhar("C")
pilha.mostrar()  # C -> B -> A
print("Desempilhando:", pilha.desempilhar())
pilha.mostrar()  # B -> A