from src.dto.layer_dto import LayerDTO

class BackgroundLayer(LayerDTO):
    def init(self, _):
        pass
    
    def run(self, game):
        game.screen.fill("black")
