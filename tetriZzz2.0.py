from random import SystemRandom
import pecas
import pygame, time

altura = 600
largura = 350
base_blocos = 10
altura_blocos = 14
mapa = []
linha_vazia = []
random = SystemRandom()
pygame.font.init()
pontos = 0

def criar_mapa():
    for i in range(base_blocos):
        linha_vazia.append(0)

    for i in range(altura_blocos):
        mapa.append(linha_vazia.copy())

criar_mapa()


def criar_janela():
    pygame.init()
    pygame.display.set_caption("TetriZzz 2.0")
    fonte_texto = pygame.font.SysFont("Pixeled", 50)
    return (pygame.display.set_mode([largura, altura]), fonte_texto)

janela, fonte_texto = criar_janela()

def att_frame():
    janela.fill([25,25,25])
    for linhas in range(len(mapa)):
        for colunas in range(len(mapa[linhas])):
            block = pygame.Rect((largura/base_blocos)*colunas, (altura/altura_blocos)*linhas, (largura/base_blocos), (altura/altura_blocos))
            if mapa[linhas][colunas] == 1:
                pygame.draw.rect(janela, [0,255,10], block, border_radius=5)
            elif mapa[linhas][colunas] == 2:
                pygame.draw.rect(janela, [255,0,0], block, border_radius=5)
            elif mapa[linhas][colunas] == 3:
                pygame.draw.rect(janela, [255,0,255], block, border_radius=5)
            elif mapa[linhas][colunas] == 4:
                pygame.draw.rect(janela, [25,255,255], block, border_radius=5)
            elif mapa[linhas][colunas] == 5:
                pygame.draw.rect(janela, [255,255,0], block, border_radius=5)

    pygame.draw.line(janela, [255,0,0], (0, altura/altura_blocos), (largura, altura/altura_blocos))
    txt_pontos = fonte_texto.render(str(pontos), 1, (255,255,255))
    janela.blit(txt_pontos, (largura/3, (altura*10)/100))

    pygame.display.update()

def verifica_linhas():
    global pontos
    for linha in range(len(mapa) - 1, -1, -1):
        if not contem_0(mapa[linha]):
            swap_baixo(linha)
            pontos += 1000 
            return verifica_linhas()
        elif mapa[linha] == linha_vazia:
            return

def contem_0(linha):
    for i in linha:
        if i == 0:
            return True
    return False

def swap_baixo(linha):
    for linha in range(linha, 0, -1):
        if mapa[linha] == linha_vazia:
            break
        mapa[linha] = mapa[linha-1].copy()

def fim_de_jogo():
    texto = "Já era!"
    txt_fim_jogo = fonte_texto.render(texto, 1, (255,255,255), (25,25,25))
    janela.blit(txt_fim_jogo, (largura/3, (altura*50)/100))
    pygame.display.update()
    time.sleep(5)

def game_loop():
    linha = 0
    coluna = int(base_blocos/2)
    isA = False
    isD = False
    isS = False
    posicao = random.randint(1, 4)
    id_peca = random.randint(1, 5)
    reiniciou = True
    clock = pygame.time.Clock() 
    clock2 = 0
    nova_linha = 0
    global pontos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    isA = True
                    continue
                elif event.key == pygame.K_d:
                    isD = True
                    continue
                elif event.key == pygame.K_w:
                    linha, coluna, posicao = pecas.rotacionar_peca(mapa, linha, coluna, id_peca, posicao)
                    att_frame()
                    continue
                elif event.key == pygame.K_SPACE:
                    while linha != -1:
                        linha, coluna, posicao = pecas.mover_baixo(mapa, linha, coluna, id_peca, posicao)
                        pontos += 50
                    verifica_linhas()
                    att_frame()
                    linha = 0
                    reiniciou = True
                    clock2 = 0
                    continue
                elif event.key == pygame.K_s:
                    isS = True
                
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    isA = False
                elif event.key == pygame.K_d:
                    isD = False
                elif event.key == pygame.K_s:
                    isS = False

        #id_peca = 4
        #posicao = 2
        if linha == 0 and reiniciou:
            id_peca = random.randint(1,5)
            posicao = random.randint(1,4)
            coluna = int(base_blocos/2) - 1
            reiniciou = False
            pecas.desenhar_peca(mapa, linha, coluna, id_peca, posicao)
            att_frame()

        if isA and pecas.espaco_esquerda(mapa, linha, coluna, id_peca, posicao):
            linha, coluna, posicao = pecas.mover_esquerda(mapa, linha, coluna, id_peca, posicao)
            att_frame()

        elif isD and pecas.espaco_direita(mapa, linha, coluna, id_peca, posicao):
            linha, coluna, posicao = pecas.mover_direita(mapa, linha, coluna, id_peca, posicao)
            att_frame()

        if clock2 >= 8:
            nova_linha, coluna, posicao = pecas.mover_baixo(mapa, linha, coluna, id_peca, posicao)
            att_frame()
            if nova_linha == -1:
                if linha == 0:
                    return fim_de_jogo()
                linha = 0
                reiniciou  = True
                clock2 = 0
                verifica_linhas()
            else:
                linha = nova_linha
        if isS:
            clock2 = (clock2 + 6) % 10
            pontos += 1
            time.sleep(0.005)
            att_frame()
            continue
        else:
            clock2 = (clock2 + 1) % 9
        clock.tick(15)
        


game_loop()