# 11
# 1
# 1
def posicionar(mapa, linha, coluna):
    if coluna < 0 or coluna > len(mapa[0]) - 2:
        return -1

    # Linha 0
    condicao1 = mapa[linha][coluna] == 0
    if linha == 0 and condicao1:
        mapa[linha][coluna] = 7
        return (linha, coluna, 3)

    # Linha 1
    condicao2 = mapa[linha-1][coluna] == 0
    if linha == 1 and condicao1 and condicao2:
        mapa[linha][coluna] = 7
        mapa[linha-1][coluna] = 7
        return (linha, coluna, 3)

    # Linha >= 2
    condicao3 = mapa[linha-2][coluna] == 0
    condicao4 = mapa[linha-2][coluna+1] == 0
    if linha >= 2 and condicao1 and condicao2 and condicao3 and condicao4:
        mapa[linha][coluna] = 7
        mapa[linha-1][coluna] = 7
        mapa[linha-2][coluna] = 7
        mapa[linha-2][coluna+1] = 7
        return (linha, coluna, 3)

    return -1

# 11
# 1
# 1
def remover(mapa, linha, coluna):
    if linha == 0:
        mapa[linha][coluna] = 0
    
    elif linha == 1:
        mapa[linha][coluna] = 0
        mapa[linha-1][coluna] = 0

    else:
        mapa[linha][coluna] = 0
        mapa[linha-1][coluna] = 0
        mapa[linha-2][coluna] = 0
        mapa[linha-2][coluna+1] = 0

# 11
# 1
# 1
def espaco_esquerda(mapa, linha, coluna):
    if coluna == 0:
        return False

    condicao1 = mapa[linha][coluna-1] == 0
    condicao2 = mapa[linha-1][coluna-1] == 0
    condicao3 = mapa[linha-2][coluna-1] == 0

    return condicao1 and condicao2 and condicao3

def espaco_direita(mapa, linha, coluna):
    if coluna == len(mapa[0]) - 2:
        return False

    condicao1 = mapa[linha][coluna+1] == 0
    condicao2 = mapa[linha-1][coluna+1] == 0
    condicao3 = mapa[linha-2][coluna+2] == 0

    return condicao1 and condicao2 and condicao3