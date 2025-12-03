def maior_numero(num, k):
    # “Dado um número com N dígitos,
    # escolha exatamente K dígitos,
    # mantendo a ordem, para formar o maior número possível.”
    # Tempo de complexidade: O(n)

    remover = len(num) - k  # Quantos digitos precisam ser removido n - k
    pilha = []

    for digito in num:
        """
        Iterar enquanto:
            1. Poder remover digitos
            2. A pilha ainda não está vazia
            3. O topo da pilha é menor do que o dígito atual
        """
        while remover > 0 and pilha and pilha[-1] < digito:
            pilha.pop()
            remover -= 1

        # Colocar o digito atual na pilha
        pilha.append(digito)

    # No caso de sobra, remover do final, que é a única parte removível restante
    if remover > 0:
        pilha = pilha[:-remover]

    return "".join(pilha)


print(maior_numero("318231239125235321", 12))
