import pygame as pg, data
from page import Page
from startgamebtn import StartButton
from changecolourpagebtn import ChangeColourPageButton
from button import Button
from typing_extensions import override # type: ignore
from game import Game
from colourspage import ColoursPage

class StartPage(Page):
    def __init__(self, width: int, height: int, scale: int, pageName: str, fps: int) -> None:
        super().__init__(width, height, scale, pageName, fps)
        self.game: Game | None = None
        self.coloursPage: Page | None = None

        self.buttons: list[Button] = []
        self.startAgainstPlayerButton: StartButton = StartButton(self.width//3, self.height//4, self.width//9, self.height//6,
                                                                 data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "Play Against Player", False, self)
        
        self.startAgainstAIButton: StartButton = StartButton(self.width//3, self.height//4, self.width - ((self.width//9) + self.width//3),
                                                             self.height//6, data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "Play Against AI", True, self)
        
        self.changeUserColoursButton: ChangeColourPageButton = ChangeColourPageButton(self.width//3, self.height//4, self.width//2 - self.width//6, self.height//6 + (self.height//4 + self.height//9),
                                                                                data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "Change User Colours", self)

        self.buttons.append(self.startAgainstPlayerButton)
        self.buttons.append(self.startAgainstAIButton)
        self.buttons.append(self.changeUserColoursButton)


    @override
    def draw(self) -> None:
        """Draws all the buttons to the screen."""
        self.screen.fill(data.BACKGROUND_COLOUR)
        for button in self.buttons:
            button.draw(self.screen)


    @override
    def logic(self) -> None:
        """Changes the pagename to the self.pagename and updates the buttons."""
        pg.display.set_caption(f"Connect 4 | {self.pageName}")
        for button in self.buttons:
            button.update()