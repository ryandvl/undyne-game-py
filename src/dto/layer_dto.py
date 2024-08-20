from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.controllers.game_controller import GameController

class LayerDTO():
    NAME: str
    LAYER: int

    def init(self, game: 'GameController'):
        pass

    def run(self, game: 'GameController'):
        pass
