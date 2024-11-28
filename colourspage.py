import pygame as pg, data
from page import Page
from startgamebtn import StartButton
from changecolourbtn import ChangeColourButton
from button import Button
from typing_extensions import override
from game import Game

class StartPage(Page):
    def __init__(self, width: int, height: int, scale: int, pageName: str, fps: int) -> None:
        super().__init__(width, height, scale, pageName, fps)
        self.game: Game | None = None

        self.buttons: list[Button] = []
        self.startAgainstPlayerButton: StartButton = StartButton(self.width//3, self.height//4, self.width//9, self.height//6,
                                                                 data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "Play Against Player", False, self)
        
        self.startAgainstAIButton: StartButton = StartButton(self.width//3, self.height//4, self.width - ((self.width//9) + self.width//3),
                                                             self.height//6, data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "Play Against AI", True, self)
        
        self.changeUserColoursButton: ChangeColourButton = ChangeColourButton(self.width//3, self.height//4, self.width//2 - self.width//6, self.height//6 + (self.height//4 + self.height//9),
                                                                 data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "Change User Colours")


        self.buttons.append(self.startAgainstPlayerButton)
        self.buttons.append(self.startAgainstAIButton)
        self.buttons.append(self.changeUserColoursButton)


    @override
    def draw(self) -> None:
        pass


    @override
    def logic(self) -> None:
        pass