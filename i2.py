# 1111
def posicionar(mapa, linha, coluna):
    if coluna < 0 or coluna > len(mapa[0]) - 4:
        return -1

    # Linha >= 0
    condicao1 = mapa[linha][coluna] == 0
    condicao2 = mapa[linha][coluna+1] == 0
    condicao3 = mapa[linha][coluna+2] == 0
    condicao4 = mapa[linha][coluna+3] == 0
    if condicao1 and condicao2 and condicao3 and condicao4:
        mapa[linha][coluna] = 4
        mapa[linha][coluna+1] = 4
        mapa[linha][coluna+2] = 4
        mapa[linha][coluna+3] = 4
        return (linha, coluna, 2)

    return -1

# 1111
def remover(mapa, linha, coluna):
    mapa[linha][coluna] = 0
    mapa[linha][coluna+1] = 0
    mapa[linha][coluna+2] = 0
    mapa[linha][coluna+3] = 0

# 1111
def espaco_esquerda(mapa, linha, coluna):
    if coluna == 0:
        return False

    condicao1 = mapa[linha][coluna-1] == 0

    return condicao1

# 1111
def espaco_direita(mapa, linha, coluna):
    if coluna == len(mapa[0]) - 4:
        return False

    condicao1 = mapa[linha][coluna+4] == 0

    return condicao1