def brancos(string):
    cont = 0
    if string == "":
        return 0
    if string[-1] == " ":
        cont += 1
    return cont + brancos(string[:-1])

print(brancos('A B C 7 3 1 d f a'))