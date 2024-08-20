import pygame
from src.dto.layer_dto import LayerDTO

class PlayerLayer(LayerDTO):
    def run(self, screen, clock):
        te = pygame.Rect(0,0,100, 100)
        pygame.draw.rect(
            screen,
            "red",
            te
        )
