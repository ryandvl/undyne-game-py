from pygame import Surface

def centerCoordinateInScreen(screen: Surface):
    return screen.get_rect().center

def centerImageInSurface(surface: Surface, image: Surface):
    new_image = image.get_rect(center=surface.get_rect().center)

    return new_image
