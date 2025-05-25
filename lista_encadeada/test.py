import os
from lista import *

os.system("cls")
#os.system("clear")

print("--- Testando Lista ---")
lista = Lista()
print(f"Vazia? {lista.vazia()}")
lista.inserir_inicio(10)
lista.inserir_final(20)
lista.inserir_inicio(5)
lista.inserir_final(30)
lista.exibir()
lista.remover_inicio()
lista.remover_final()
print("-----------------segundo teste---------------")
lista.exibir()
lista.remover_final()
lista.remover_final()
print(f"Vazia? {lista.vazia()}")