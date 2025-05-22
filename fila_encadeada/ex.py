from fila import *

fila = Fila()
fila.enfileirar("1")
fila.enfileirar("2")
fila.enfileirar("3")

print("=== FILA ===")
fila.mostrar()
print("Desenfileirando o primeiro da fila...", fila.desenfileirar())
fila.mostrar()