import pygame
from typing import Dict

IMAGES: Dict[str, pygame.Surface] = dict()
COLORS: Dict = {
    "shield_blue": "#434af3",
    "shield_red": "#ff1e00",
    "heart": "#00a002"
}

def saveImage(image_name: str, image: pygame.Surface):
    IMAGES[image_name] = image
    return image

def getImage(image_name: str):
    return IMAGES[image_name]

def deleteImage(image_name: str):
    del IMAGES[image_name]
