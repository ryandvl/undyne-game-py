from pygame import Color, PixelArray, Surface


def changeColor(image: Surface, from_color: str, to_color: str) -> Surface:
    surface = PixelArray(image)
    surface.replace(Color(from_color), Color(to_color))
    surface = surface.surface

    return surface