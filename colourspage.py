import pygame as pg, data
from page import Page
from startgamebtn import StartButton
from doneButton import DoneButton
from button import Button
from typing_extensions import override # type: ignore
from rectangle import Rectangle
from game import Game

class ColoursPage(Page):
    def __init__(self, width: int, height: int, scale: int, pageName: str, fps: int) -> None:
        super().__init__(width, height, scale, pageName, fps)
        self.text: list = []        
        self.buttons: list[Button] = []


        doneButton1: DoneButton = DoneButton((self.width//18) * 5, self.height//12, (self.width//9), self.height - (self.height//18 + self.height//12),
                                            data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "DONE", self, None)
        
        doneButton2: DoneButton = DoneButton((self.width//18) * 5, self.height//12, self.width - (self.width//9 + (self.width//18 * 5)), self.height - (self.height//18 + self.height//12),
                                            data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "DONE", self, None)
        
        self.splitterLine: Rectangle = Rectangle(self.width//81, self.height, self.width/2, 0, data.BLACK, 0)

        font: pg.font.FontType = pg.font.Font("Resources/PixelFont.ttf", data.BUTTON_FONT_SIZE)
        self.textPlayer1 = font.render("Player 1", True, data.BUTTON_FONT_COLOUR)
        self.textPlayer2 = font.render("Player 2", True, data.BUTTON_FONT_COLOUR)

        self.buttons.append(doneButton1)
        self.buttons.append(doneButton2)


    @override
    def draw(self) -> None:
        self.screen.fill(data.BACKGROUND_COLOUR)
        self.screen.blit(self.textPlayer1, (self.width//4 - self.textPlayer1.get_width()//2, self.height//9))
        self.screen.blit(self.splitterLine.image, self.splitterLine.rect.topleft)
        self.screen.blit(self.textPlayer2, (self.width - (self.width//4 + self.textPlayer2.get_width()//2), self.height//9))
        for button in self.buttons:
            button.draw(self.screen)


    @override
    def logic(self) -> None:
        for button in self.buttons:
            button.update()