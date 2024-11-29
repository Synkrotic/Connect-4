import pygame as pg
import data

class Rectangle:
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], borderRadius: int) -> None:
        self.width: int = width
        self.height: int = height
        self.x = x
        self.y = y
        self.colour: tuple[int, int, int] = colour
        self.borderRadius = borderRadius if borderRadius != None else data.BUTTON_BORDER_RADIUS


        squareImage: pg.Surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        # print(self.colour[0], self.colour[1], self.colour[2])
        squareImage.fill(self.colour)
        self.image: pg.Surface = squareImage.copy()

        self.doBorderRadius()

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    

    def doBorderRadius(self) -> None:
        mask: pg.Surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        mask.fill(data.TRANSPARENT_COLOUR)
        pg.draw.rect(mask, data.BACKGROUND_COLOUR, mask.get_rect(), border_radius=self.borderRadius)

        self.image.blit(mask, (0, 0), special_flags=pg.BLEND_RGBA_MIN)


    def draw(self, screen: pg.display) -> None:
        screen.blit(self.image, self.rect.topleft)