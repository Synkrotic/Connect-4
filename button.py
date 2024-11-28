import pygame as pg, data
from rectangle import Rectangle
from typing_extensions import override

class Button(Rectangle):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str) -> None:
        super().__init__(width, height, x, y, colour, height // 10)
        self.text: str = text
        self.hovered: bool = False
        self.hoverColour = hoverColour

        self.outline: Rectangle = Rectangle(self.width + (data.BUTTON_OUTLINE_WIDTH * 2), self.height + (data.BUTTON_OUTLINE_WIDTH * 2),
                                            self.x - data.BUTTON_OUTLINE_WIDTH, self.y - data.BUTTON_OUTLINE_WIDTH, data.BLACK, data.BUTTON_BORDER_RADIUS + data.BUTTON_OUTLINE_WIDTH)
        
        self.shadow: Rectangle = Rectangle(self.width + (data.BUTTON_OUTLINE_WIDTH * 2), self.height + (data.BUTTON_OUTLINE_WIDTH * 2), self.x - data.BUTTON_OUTLINE_WIDTH + data.BUTTON_SHADOW_OFFSET,
                                           self.y - data.BUTTON_OUTLINE_WIDTH  + data.BUTTON_SHADOW_OFFSET, data.BUTTON_MENU_SHADOW_COLOUR, data.BUTTON_BORDER_RADIUS + data.BUTTON_OUTLINE_WIDTH)

        

    @override
    def draw(self, screen: pg.Surface) -> None:
        self.shadow.draw(screen)
        self.outline.draw(screen)
        font = pg.font.Font("Resources/PixelFont.ttf", data.BUTTON_FONT_SIZE)
        text = font.render(self.text, True, data.BUTTON_FONT_COLOUR)
        words = self.text.split()
        if len(words) > 1:
            first_line = ' '.join(words[:-1])
            second_line = words[-1]
            text1 = font.render(first_line, True, data.BUTTON_FONT_COLOUR)
            text2 = font.render(second_line, True, data.BUTTON_FONT_COLOUR)
            self.image.blit(text1, ((self.width/2) - text1.get_width()/2 , (self.height/2) - text1.get_height()))
            self.image.blit(text2, ((self.width/2) - text2.get_width()/2 , (self.height/2)))
        else:
            self.image.blit(text, ((self.width/2) - text.get_width()/2 , (self.height/2) - text.get_height()/2))
        screen.blit(self.image, self.rect.topleft)


    def logic(self) -> None:
        print("Button has no logic yet.")


    def update(self) -> None:
        self.isHovered()
        if (self.hovered and pg.mouse.get_pressed()[0]):
            self.logic()


    def isHovered(self) -> None:
        self.hovered = self.rect.collidepoint(pg.mouse.get_pos())
        match self.hovered:
            case True: self.image.fill(self.hoverColour)
            case False: self.image.fill(self.colour)
        self.doBorderRadius(self.height//10)
