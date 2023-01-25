import j1, j2, j3, j4

def posicionar(mapa, linha, coluna, posicao):
    if linha == len(mapa):
        return -1
    
    match posicao:
        case 1:
            return j1.posicionar(mapa, linha, coluna)
        case 2:
            return j2.posicionar(mapa, linha, coluna)
        case 3:
            return j3.posicionar(mapa, linha, coluna)
        case 4:
            return j4.posicionar(mapa, linha, coluna)

def remover(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return j1.remover(mapa, linha, coluna)
        case 2:
            return j2.remover(mapa, linha, coluna)
        case 3:
            return j3.remover(mapa, linha, coluna)
        case 4:
            return j4.remover(mapa, linha, coluna)

def espaco_esquerda(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return j1.espaco_esquerda(mapa, linha, coluna)
        case 2:
            return j2. espaco_esquerda(mapa, linha, coluna)
        case 3:
            return j3. espaco_esquerda(mapa, linha, coluna)
        case 4:
            return j4. espaco_esquerda(mapa, linha, coluna)

def espaco_direita(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return j1.espaco_direita(mapa, linha, coluna)
        case 2:
            return j2.espaco_direita(mapa, linha, coluna)
        case 3:
            return j3.espaco_direita(mapa, linha, coluna)
        case 4:
            return j4.espaco_direita(mapa, linha, coluna)

def rotacionar(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            #  1    1
            #  1 -> 111
            # 11    
            j1.remover(mapa, linha, coluna)
            resultado = j2.posicionar(mapa, linha-1, coluna)
            if resultado == -1:
                resultado = j2.posicionar(mapa, linha-1, coluna-1)

            if resultado == -1:
                return j1.posicionar(mapa, linha, coluna)
                
            return resultado

        case 2:
            # 1      11
            # 111 -> 1
            #        1
            if linha == len(mapa) - 1:
                return (linha, coluna, 4)

            j2.remover(mapa, linha, coluna)
            resultado = j3.posicionar(mapa, linha+1, coluna+1)
            if resultado == -1:
                return j2.posicionar(mapa, linha, coluna)
            return resultado

        case 3:
            # 11
            # 1  -> 111
            # 1       1
            j3.remover(mapa, linha, coluna)
            resultado = j4.posicionar(mapa, linha, coluna-1)
            if resultado == -1:
                resultado = j4.posicionar(mapa, linha, coluna)

            if resultado == -1:
                resultado = j4.posicionar(mapa, linha, coluna-1)

            if resultado == -1:
                return j3.posicionar(mapa, linha, coluna)

            return resultado

        case 4:
            #         1
            # 111 ->  1
            #   1    11
            j4.remover(mapa, linha, coluna)
            resultado = j1.posicionar(mapa, linha, coluna)
            if resultado == -1:
                return j4.posicionar(mapa, linha, coluna)

            return resultado
            