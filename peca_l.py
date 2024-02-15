import l1, l2, l3, l4

def posicionar(mapa, linha, coluna, posicao):
    if linha == len(mapa):
        return -1
    
    match posicao:
        case 1:
            return l1.posicionar(mapa, linha, coluna)
        case 2:
            return l2.posicionar(mapa, linha, coluna)
        case 3:
            return l3.posicionar(mapa, linha, coluna)
        case 4:
            return l4.posicionar(mapa, linha, coluna)

def remover(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return l1.remover(mapa, linha, coluna)
        case 2:
            return l2.remover(mapa, linha, coluna)
        case 3:
            return l3.remover(mapa, linha, coluna)
        case 4:
            return l4.remover(mapa, linha, coluna)

def espaco_esquerda(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return l1.espaco_esquerda(mapa, linha, coluna)
        case 2:
            return l2. espaco_esquerda(mapa, linha, coluna)
        case 3:
            return l3. espaco_esquerda(mapa, linha, coluna)
        case 4:
            return l4. espaco_esquerda(mapa, linha, coluna)

def espaco_direita(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return l1.espaco_direita(mapa, linha, coluna)
        case 2:
            return l2.espaco_direita(mapa, linha, coluna)
        case 3:
            return l3.espaco_direita(mapa, linha, coluna)
        case 4:
            return l4.espaco_direita(mapa, linha, coluna)

def rotacionar(mapa, linha, coluna, posicao):

    match posicao:
        case 1:
            # 1
            # 1 -> 111
            # 11   1
            l1.remover(mapa, linha, coluna)
            resultado = l2.posicionar(mapa, linha, coluna-1)
            if resultado == -1:
                resultado = l2.posicionar(mapa, linha, coluna-2)

            if resultado == -1:
                resultado = l2.posicionar(mapa, linha, coluna)

            if resultado == -1:
                return l1.posicionar(mapa, linha, coluna)
                
            return resultado
        case 2:
            #         11
            # 111  ->  1
            # 1        1
            l2.remover(mapa, linha, coluna)
            resultado = l3.posicionar(mapa, linha, coluna)
            if resultado == -1:
                return l2.posicionar(mapa, linha, coluna)
            return resultado
        case 3:
            # 11      1
            #  1 -> 111
            #  1
            l3.remover(mapa, linha, coluna)
            resultado = l4.posicionar(mapa, linha-1, coluna)
            if resultado == -1:
                resultado = l4.posicionar(mapa, linha-1, coluna-1)

            if resultado == -1:
                return l3.posicionar(mapa, linha, coluna)

            return resultado
        case 4:
            #   1    1
            # 111 -> 1
            #        11
            if linha == len(mapa) - 1:
                return (linha, coluna, 4)

            l4.remover(mapa, linha, coluna)
            resultado = l1.posicionar(mapa, linha+1, coluna+1)
            if resultado == -1:
                return l4.posicionar(mapa, linha, coluna)
            return resultado
        
def obter_coordenadas(linha, coluna, posicao):
    match posicao:
        case 1: return [[linha, coluna], [linha, coluna+1], [linha-1, coluna], [linha-2, coluna]]
        case 2: return [[linha, coluna], [linha-1, coluna], [linha-1, coluna+1], [linha-1, coluna+2]]
        case 3: return [[linha, coluna+1], [linha-1, coluna+1], [linha-2, coluna], [linha-2, coluna+1]]
        case 4: return [[linha, coluna], [linha, coluna+1], [linha, coluna+2], [linha-1, coluna+2]]