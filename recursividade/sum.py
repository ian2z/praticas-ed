def sum(lista):
    if lista == []:
        return 0
    ult = lista.pop()
    return ult + sum(lista)

numeros = [1,2,3,4,5]
print(sum(numeros))