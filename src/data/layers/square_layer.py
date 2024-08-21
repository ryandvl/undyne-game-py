import pygame
from src.dto.layer_dto import LayerDTO

class SquareLayer(LayerDTO):
    def init(self, _):
        pass

    def run(self, game):
        ret = pygame.Rect(
            (0, 0), 
            tuple(x/3 for x in game.screen.size)
        )
        ret.center = game.screen.get_rect().center
        pygame.draw.rect(
            game.screen,
            'white',
            ret,
            2
        )