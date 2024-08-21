from pygame import Rect, Surface, sprite

from src.dto.game_object_dto import GameObjectDTO

class GameObjectController(sprite.Sprite):
    id: str
    # data: GameObjectDTO
    position: Rect

    image: Surface
    rect: Rect

    def __init__(self, color, width, height):
       sprite.Sprite.__init__(self)

       self.image = Surface([width, height])
       self.image.fill(color)

       self.rect = self.image.get_rect()

    def resetPosition(self):
        self.position = self.rect.move(0, 0)

    def move(self, x: float, y: float):
        self.position = self.position.move(x, y)

    def set_position(self):
        pass

    def render(self):
        pass
