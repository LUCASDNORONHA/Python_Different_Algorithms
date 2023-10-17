def encontrar_primeiro_duplicado(lista):
    """
    Esta função encontra o primeiro número duplicado em uma lista, considerando o segundo número como a duplicação.

    Args:
        lista (list): A lista de inteiros a ser verificada.

    Returns:
        int: O primeiro número duplicado encontrado, ou -1 se nenhum duplicado for encontrado.
    """
    numeros_checados = set()
    numero_duplicado = -1

    for numero in lista:
        if numero in numeros_checados:
            numero_duplicado = numero
            break

        numeros_checados.add(numero)

    # Redefina o conjunto dentro do escopo da função após cada iteração
    numeros_checados = set()
    
    return numero_duplicado

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# Verificando duplicados nas listas
for i, lista in enumerate(lista_de_listas_de_inteiros, start=1):
    resultado = encontrar_primeiro_duplicado(lista)
    if resultado != -1:
        print(f"Lista {i}: {lista} -> Primeiro duplicado: {resultado}")
    else:
        print(f"Lista {i}: {lista} -> Nenhum duplicado encontrado")
