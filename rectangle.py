import pygame as pg
import data

class Rectangle:
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int]) -> None:
        self.width: int = width
        self.height: int = height
        self.colour: tuple[int, int, int] = colour

        squareImage: pg.Surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        squareImage.fill(self.colour)

        mask: pg.Surface = pg.Surface((self.width, self.height * 2), pg.SRCALPHA)
        mask.fill(data.TRANSPARENT_COLOUR)
        pg.draw.rect(mask, data.BACKGROUND_COLOUR, mask.get_rect(), border_radius=int(self.width/8))

        self.image: pg.Surface = squareImage.copy()
        self.image.blit(mask, (0, 0), special_flags=pg.BLEND_RGBA_MIN)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    

    def draw(self, screen: pg.display) -> None:
        screen.blit(self.image, self.rect.topleft)