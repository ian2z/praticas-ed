from lista import *
import os
os.system("cls")

lista=Lista()

lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(10)
lista.inserir_inicio(30)
print("-------------------------------------")
lista.buscar(1)
lista.buscar(10)
lista.exibir()
print("-------------------------------------")
lista.inserir_em(3, 40)
lista.inserir_em(10, 30)
lista.exibir()