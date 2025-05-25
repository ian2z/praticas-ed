from pilha import *

pilha = Pilha()
pilha.empilhar("A")
pilha.empilhar("B")
pilha.empilhar("C")

print("=== PILHA ===")
pilha.mostrar()
print("Desempilhando:", pilha.desempilhar())
pilha.mostrar()