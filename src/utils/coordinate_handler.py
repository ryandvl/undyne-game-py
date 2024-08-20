from pygame import Surface

def centerCoordinateInScreen(screen: Surface):
    return screen.get_rect().center
    # return (screen.get_width() / 2, screen.get_height() / 2)

def centerImageInSurface(surface: Surface, image: Surface):
    new_image = image.get_rect(center=surface.get_rect().center)
    # new_image.center = surface.get_rect().center

    return new_image
