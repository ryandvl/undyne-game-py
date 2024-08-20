from src.dto.layer_dto import LayerDTO

class BackgroundLayer(LayerDTO):
    def run(self, screen, clock):
        screen.fill("purple")
