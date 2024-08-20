import pygame

class GameController:
    '''
    Largura da janela
    '''
    WIDTH = 300
    HEIGHT = 300

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("purple")

            pygame.display.flip()

            clock.tick(30)

        pygame.quit()
    
    def setResolution(self, newWidth, newHeight):
        self.WIDTH = newWidth
        self.HEIGHT = newHeight

        pygame.display.set_mode((self.WIDTH, self.HEIGHT))