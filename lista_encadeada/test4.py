import os
from lista import *
os.system("cls")

lista = Lista()

lista.inserir_inicio("N")
lista.inserir_inicio("A")
lista.inserir_inicio("I")
lista.exibir()
print("-------------------")
lista.remover_em(1)
lista.exibir()
print("-------------------")