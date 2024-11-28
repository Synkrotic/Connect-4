import pygame as pg, data
from rectangle import Rectangle
from typing import override

class Button(Rectangle):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str) -> None:
        super().__init__(width, height, x, y, colour, height // 10)
        self.text: str = text
        self.hovered: bool = False
        self.hoverColour = hoverColour
        self.outline: Rectangle = Rectangle(self.width + (data.BUTTON_OUTLINE_WIDTH * 2), self.height + (data.BUTTON_OUTLINE_WIDTH * 2), self.x - data.BUTTON_OUTLINE_WIDTH, self.y - data.BUTTON_OUTLINE_WIDTH, (0, 0, 0), (height // 10) + data.BUTTON_OUTLINE_WIDTH)


    @override
    def draw(self, screen: pg.Surface) -> None:
        self.outline.draw(screen)
        screen.blit(self.image, self.rect.topleft)
        


    def update(self) -> None:
        self.isHovered()


    def isHovered(self) -> None:
        self.hovered = self.rect.collidepoint(pg.mouse.get_pos())
        match self.hovered:
            case True: self.image.fill(self.hoverColour)
            case False: self.image.fill(self.colour)
        self.doBorderRadius(self.height//10)