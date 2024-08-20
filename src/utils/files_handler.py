import os
import pygame

def getImage(image_filename: str):
    return os.path.join("src", "assets", "images", image_filename)

def loadImage(image_filename: str):
    return pygame.image.load(getImage(image_filename))
