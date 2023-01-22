# 1
# 1
# 1
# 1
def posicionar(mapa, linha, coluna):
    if coluna < 0 or coluna > len(mapa[0]) - 1:
        return -1

    # Linha 0
    condicao1 = mapa[linha][coluna] == 0
    if linha == 0 and condicao1:
        mapa[linha][coluna] = 4
        return (linha, coluna, 1)

    # Linha 1
    condicao2 = mapa[linha-1][coluna] == 0
    if linha == 1 and condicao1 and condicao2:
        mapa[linha][coluna] = 4
        mapa[linha-1][coluna] = 4
        return (linha, coluna, 1)

    # Linha 2
    condicao3 = mapa[linha-2][coluna] == 0
    if linha == 2 and condicao1 and condicao2 and condicao3:
        mapa[linha][coluna] = 4
        mapa[linha-1][coluna] = 4
        mapa[linha-2][coluna] = 4
        return (linha, coluna, 1)

    # Linha >= 3
    condicao4 = mapa[linha-3][coluna] == 0
    if linha >= 3 and condicao1 and condicao2 and condicao3 and condicao4:
        mapa[linha][coluna] = 4
        mapa[linha-1][coluna] = 4
        mapa[linha-2][coluna] = 4
        mapa[linha-3][coluna] = 4
        return (linha, coluna, 1)

    return -1

# 1
# 1
# 1
# 1
def remover(mapa, linha, coluna):
    if linha == 0:
        mapa[linha][coluna] = 0

    elif linha == 1:
        mapa[linha][coluna] = 0
        mapa[linha-1][coluna] = 0
    
    elif linha == 2:
        mapa[linha][coluna] = 0
        mapa[linha-1][coluna] = 0
        mapa[linha-2][coluna] = 0
    
    else:
        mapa[linha][coluna] = 0
        mapa[linha-1][coluna] = 0
        mapa[linha-2][coluna] = 0
        mapa[linha-3][coluna] = 0

# 1
# 1
# 1
# 1
def espaco_esquerda(mapa, linha, coluna):
    if coluna == 0:
        return False
    
    condicao1 = mapa[linha][coluna-1] == 0
    condicao2 = mapa[linha][coluna-1] == 0
    condicao3 = mapa[linha][coluna-1] == 0
    condicao4 = mapa[linha][coluna-1] == 0

    return condicao1 and condicao2 and condicao3 and condicao4

# 1
# 1
# 1
# 1
def espaco_direita(mapa, linha, coluna):
    if coluna == len(mapa[0]) - 1:
        return False

    condicao1 = mapa[linha][coluna+1] == 0
    condicao2 = mapa[linha][coluna+1] == 0
    condicao3 = mapa[linha][coluna+1] == 0
    condicao4 = mapa[linha][coluna+1] == 0

    return condicao1 and condicao2 and condicao3 and condicao4