from lista import *
import os
os.system("cls")

lista = Lista()

lista.inserir_inicio(20) #6
lista.inserir_inicio(10) #5
lista.inserir_inicio(10) #4
lista.inserir_inicio(50) #3
lista.inserir_inicio(40) #2
lista.inserir_inicio(10) #1
lista.inserir_inicio(10) #0
print("-------------------")
lista.exibir()
print("-------------------")
lista.buscar_todos(10)
print("-------------------")
