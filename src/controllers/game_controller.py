import pygame
from src.controllers.data_controller import COLORS
from src.controllers.layer_controller import LayerController
from src.data.layers.background_layer import BackgroundLayer
from src.data.layers.player_layer import PlayerLayer
from src.data.layers.square_layer import SquareLayer
from src.utils.colors_handler import changeColor
from src.utils.files_handler import loadImage

class GameController:
    screen: pygame.Surface
    clock: pygame.Clock

    layer_controller: LayerController

    WIDTH = 500
    HEIGHT = 500
    GAME_NAME = 'Undyne Fight'
    
    '''
    Iniciar o processo
    '''
    def start(self):
        pygame.init()

        self.screen = self.setResolution(self.WIDTH, self.HEIGHT)
        pygame.display.set_caption(self.GAME_NAME)
        
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(changeColor(loadImage("heart.png"), 'white', 'red'))

        self.layer_controller = LayerController(self)
        
        self.layer_controller.addLayer("background", BackgroundLayer())
        self.layer_controller.addLayer("player", PlayerLayer())
        self.layer_controller.addLayer("square", SquareLayer())

        self.run()

    '''
    Iniciar o pygame
    '''
    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    exit()

            self.layer_controller.renderLayers()

            self.clock.tick(30)
            pygame.display.flip()

        pygame.quit()
    
    '''
    Definir a resolução
    '''
    def setResolution(self, newWidth: int, newHeight: int) -> pygame.Surface:
        self.WIDTH = newWidth
        self.HEIGHT = newHeight

        return pygame.display.set_mode((self.WIDTH, self.HEIGHT))
