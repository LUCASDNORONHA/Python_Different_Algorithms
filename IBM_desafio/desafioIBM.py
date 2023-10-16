def minNum(threshold, points):
    n = len(points) # Retorna o número de elementos na lista de notas.
    dp = [0] * n # Multiplicar n vezes o elemento 0 e atribuindo essa lista a variável dp.
    
    dp[0] = 1 # Atulizando o índice 0 pelo valor 1.
    
    # loop for para iterar cada índice a partir de 1 até n. 
    # Lembrando que n é valor da quantidade de elementos da lista de notas.
    for i in range(1, n):
        dp[i] = i + 1  # Itera em cada índice a partid o segundo índice atualizando com o valor do índice + 1.
        
        
        for j in range(i, -1, -1):
            min_points = points[j]  
            max_points = points[i]  
            if max_points - min_points <= threshold:
                if j > 0:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
                else:
                    dp[i] = 1
    
    return dp[n - 1]

# Exemplo de uso:
# limite = 4
# pontos = [1, 2, 3, 5, 8]
# resultado = minNum(limite, pontos)
# print(resultado)  # Isso imprimirá 3

if __name__ == '__main__':
    limite = 4
    pontos = [1, 2, 3, 5, 8]
    resultado = minNum(limite, pontos)
    print(resultado)
