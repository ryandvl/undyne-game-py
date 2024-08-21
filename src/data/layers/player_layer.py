from typing import TYPE_CHECKING
from pygame import Rect, draw, transform, Surface, BLEND_RGB_ADD
from src.dto.layer_dto import LayerDTO
from src.utils.colors_handler import changeColor
from src.utils.coordinate_handler import centerImageInSurface
from src.utils.files_handler import loadImage

import src.controllers.data_controller as DataController

if TYPE_CHECKING:
    from src.controllers.game_controller import GameController

class PlayerLayer(LayerDTO):
    def init(self, _):
        DataController.saveImage(
            "heart",
            loadImage("heart.png")
        )

    def run(self, game):
        heart_image = DataController.getImage("heart")
        player = game.screen.blit(
            changeColor(heart_image, 'white', 'green'),
            centerImageInSurface(game.screen, heart_image)
        )
        self.summonShield(game, player)

    def summonShield(self, game: 'GameController', player: Rect):
        from src.controllers.data_controller import COLORS

        shield_layer = Surface((game.WIDTH, game.HEIGHT))

        self.shield = Rect(
            (0, 0),
            (60, 5)
        )
        self.shield.center = player.center[0], player.center[1] + 30
        color = COLORS['shield_blue']
        draw.rect(
            shield_layer,
            color,
            self.shield
        )
        game.screen.blit(shield_layer, (0,0), special_flags=BLEND_RGB_ADD)
    
    
        
