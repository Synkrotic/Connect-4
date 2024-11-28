import pygame as pg, data
from page import Page
from startgamebtn import StartButton
from button import Button
from typing import override

class StartPage(Page):
    def __init__(self, width: int, height: int, pageName: str, fps: int) -> None:
        super().__init__(width, height, pageName, fps)

        self.buttons: list[Button] = []
        self.startAgainstPlayerButton: StartButton = StartButton(self.width//3, self.height//4, self.width//9, self.height//6, (230, 230, 230), (175, 175, 175), "Play Against Player")
        # self.startAgainstAIButton: StartButton = StartButton(self.width//3, self.height//4, (self.width//6) * 2, self.height//3, (255, 255, 255), (175, 175, 175), "Play Against AI")
        
        self.buttons.append(self.startAgainstPlayerButton)
        # self.buttons.append(self.startAgainstAIButton)


    @override
    def draw(self) -> None:
        self.screen.fill(data.BACKGROUND_COLOUR)
        for button in self.buttons:
            button.draw(self.screen)


    @override
    def logic(self) -> None:
        for button in self.buttons:
            button.update()