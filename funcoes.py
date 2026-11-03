def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    for i in range(tamanho):
        if orientacao == "horizontal":
            posicoes.append([linha, coluna + i])
        elif orientacao == "vertical":
            posicoes.append([linha + i, coluna])
            
    return posicoes