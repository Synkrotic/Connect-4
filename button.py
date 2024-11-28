import pygame as pg
from rectangle import Rectangle

class Button(Rectangle):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str) -> None:
        super().__init__(width, height, x, y, colour)
        self.text: str = text
        self.hovered: bool = False
        self.outline: Rectangle = Rectangle()

    def draw(self, screen: pg.Surface) -> None:
        screen.blit(self.image, self.rect.topleft)

    def update(self) -> None:
        self.isHovered()

    def isHovered(self) -> None:
        self.hovered = self.rect.collidepoint(pg.mouse.get_pos())
        match self.hovered:
            case True: self.image.fill((255, 255, 255, 100))
            case False: self.image.fill(self.colour)