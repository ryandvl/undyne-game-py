import src.controllers.data_controller as DataController
from src.dto.layer_dto import LayerDTO
from src.utils.coordinate_handler import centerImageInSurface
from src.utils.files_handler import loadImage
# from src.controllers.game_controller import GameController

class PlayerLayer(LayerDTO):
    def init(self, game):
        DataController.saveImage(
            "heart",
            loadImage("heart.png")
        )

    def run(self, game):
        heart_image = DataController.getImage("heart")
        game.screen.blit(
            heart_image,
            centerImageInSurface(game.screen, heart_image)
        )   