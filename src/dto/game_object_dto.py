from pygame import Surface

class GameObjectDTO:
    name: str
    speed: float
    is_enemy: bool
    sprite: Surface
    health: float
    collidable: bool
