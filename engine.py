import pygame, time

class Engine:
  def __init__(self, largura, altura, base_blocos, altura_blocos):
    self.largura = largura
    self.altura = altura
    self.base_blocos = base_blocos
    self.altura_blocos = altura_blocos
    janela, fonte_texto = self.criar_janela()
    self.janela = janela
    self.fonte_texto = fonte_texto
    janela.fill([25,25,25])
    pygame.display.update()

  def criar_janela(self):
    pygame.init()
    pygame.display.set_caption("TetriZzz")
    fonte_texto = pygame.font.SysFont("Pixeled", 50)
    return (pygame.display.set_mode([self.largura, self.altura]), fonte_texto)
  
  def fim_de_jogo(self):
    texto = "Aperte Enter\npara reiniciar"
    txt_fim_jogo = self.fonte_texto.render(texto, 1, (255,255,255), (25,25,25))
    self.janela.blit(txt_fim_jogo, (self.largura/3, (self.altura*50)/100))
    pygame.display.update()
    time.sleep(5)

  def desenhar_bloco(self, vetor2, peca):
    altura_blocos = 16
    block = pygame.Rect((self.largura/self.base_blocos)*vetor2[1], (self.altura/altura_blocos)*vetor2[0], (self.largura/self.base_blocos), (self.altura/altura_blocos))
    match peca:
      case 1: pygame.draw.rect(self.janela, [0,255,10],   block)
      case 2: pygame.draw.rect(self.janela, [255,0,0],    block)
      case 3: pygame.draw.rect(self.janela, [255,0,255],  block)
      case 4: pygame.draw.rect(self.janela, [25,255,255], block)
      case 5: pygame.draw.rect(self.janela, [255,255,0],  block)
      case 6: pygame.draw.rect(self.janela, [255,100,0],  block)
      case 7: pygame.draw.rect(self.janela, [100,50,255], block)
  
  def update(self, pontos):
    pygame.display.update()

  def limpar(self):
    self.janela.fill([25,25,25])

  def remover_bloco(self, vetor2):
    block = pygame.Rect((self.largura/self.base_blocos)*vetor2[1], (self.altura/self.altura_blocos)*vetor2[0], (self.largura/self.base_blocos), (self.altura/self.altura_blocos))
    pygame.draw.rect(self.janela, [25,25,25], block)