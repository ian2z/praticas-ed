def busca_binaria(vetor, chave, inicio, fim):
    if inicio > fim:
        return -1  # Chave não encontrada

    meio = (inicio + fim) // 2

    if vetor[meio] == chave:
        return meio
    elif chave < vetor[meio]:
        return busca_binaria(vetor, chave, inicio, meio - 1)
    else:
        return busca_binaria(vetor, chave, meio + 1, fim)
    

    