from typing import TYPE_CHECKING, Dict
from src.dto.layer_dto import LayerDTO

if TYPE_CHECKING:
    from src.controllers.game_controller import GameController

class LayerController():
    LAYERS: Dict[str, LayerDTO] = dict()
    game: 'GameController'

    def __init__(self, game: 'GameController') -> None:
        self.game = game

    def renderLayers(self):
        for layer_name in self.LAYERS.keys():
            self.runLayer(layer_name)

    def addLayer(self, layer_name: str, layer_dto: LayerDTO):
        layer_dto.NAME = layer_name
        layer_dto.LAYER = len(self.LAYERS) + 1
        layer_dto.init(self.game)

        self.LAYERS[layer_name] = layer_dto

    def removeLayer(self, layer_name: str):
        del self.LAYERS[layer_name]

    def runLayer(self, layer_name: str):
        self.LAYERS[layer_name].run(self.game)
