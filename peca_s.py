import s1, s2

def posicionar(mapa, linha, coluna, posicao):
    if linha == len(mapa):
        return -1

    if posicao > 2:
        posicao -= 2
    
    match posicao:
        case 1:
            return s1.posicionar(mapa, linha, coluna)
        case 2:
            return s2.posicionar(mapa, linha, coluna)

def remover(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return s1.remover(mapa, linha, coluna)
        case 2:
            return s2.remover(mapa, linha, coluna)

def espaco_esquerda(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return s1.espaco_esquerda(mapa, linha, coluna)
        case 2:
            return s2.espaco_esquerda(mapa, linha, coluna)

def espaco_direita(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return s1.espaco_direita(mapa, linha, coluna)
        case 2:
            return s2.espaco_direita(mapa, linha, coluna)

def rotacionar(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            #  11     1
            # 11   -> 11
            #          1
            if linha == len(mapa)-1:
                return (linha, coluna, 1)
            
            s1.remover(mapa, linha, coluna)
            resultado = s2.posicionar(mapa, linha+1, coluna)
            if resultado == -1:
                return s1.posicionar(mapa, linha, coluna)
            return resultado

        case 2:
            # 1      11
            # 11 -> 11
            #  1
            s2.remover(mapa, linha, coluna)
            resultado = s1.posicionar(mapa, linha-1, coluna)
            if resultado == -1 and s1.espaco_esquerda(mapa, linha-1, coluna):
                return s1.posicionar(mapa, linha-1, coluna-1)
            elif resultado == -1:
                return s2.posicionar(mapa, linha, coluna)
            return resultado
