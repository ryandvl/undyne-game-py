import pygame
from typing import Dict

IMAGES: Dict[str, pygame.Surface] = dict()

def saveImage(image_name: str, image: pygame.Surface):
    IMAGES[image_name] = image
    return image

def getImage(image_name: str):
    return IMAGES[image_name]

def deleteImage(image_name: str):
    del IMAGES[image_name]
