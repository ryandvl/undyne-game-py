from typing import Dict
from src.dto.layer_dto import LayerDTO

class LayerController:
    LAYERS: Dict[str, LayerDTO] = dict()

    def __init__(self, game_controller) -> None:
        self.game_controller = game_controller

    def renderLayers(self):
        for layer_name in self.LAYERS.keys():
            self.runLayer(layer_name)

    def addLayer(self, layer_name: str, layer_dto: LayerDTO):
        layer_dto.NAME = layer_name
        layer_dto.LAYER = len(self.LAYERS) + 1

        self.LAYERS[layer_name] = layer_dto

    def removeLayer(self, layer_name: str):
        del self.LAYERS[layer_name]

    def runLayer(self, layer_name: str):
        self.LAYERS[layer_name].run(
            self.game_controller.screen,
            self.game_controller.clock
        )
