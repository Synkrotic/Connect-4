import pygame as pg, data, threading
from page import Page
from startgamebtn import StartButton
from doneButton import DoneButton
from button import Button
from typing_extensions import override # type: ignore
from rectangle import Rectangle
from game import Game
from pynput import mouse

class ColoursPage(Page):
    def __init__(self, width: int, height: int, scale: int, pageName: str, fps: int) -> None:
        super().__init__(width, height, scale, pageName, fps)
        self.text: list = []        
        self.buttons: list[Button] = []
        self.listener: mouse.Listener | None = None

        doneButton1: DoneButton = DoneButton((self.width//18) * 5, self.height//12, (self.width//9), self.height - (self.height//18 + self.height//12),
                                            data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "DONE", self, None)
        
        doneButton2: DoneButton = DoneButton((self.width//18) * 5, self.height//12, self.width - (self.width//9 + (self.width//18 * 5)), self.height - (self.height//18 + self.height//12),
                                            data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "DONE", self, None)
        
        self.splitterLine: Rectangle = Rectangle(self.width//81, self.height, self.width/2, 0, data.BLACK, 0)

        font: pg.font.FontType = pg.font.Font("Resources/PixelFont.ttf", int(data.BUTTON_FONT_SIZE * 1.5))
        self.textPlayer1 = font.render("Player 1", True, data.BUTTON_FONT_COLOUR)
        self.textPlayer2 = font.render("Player 2", True, data.BUTTON_FONT_COLOUR)

        self.buttons.append(doneButton1)
        self.buttons.append(doneButton2)

        self.listenerThread: threading.Thread = threading.Thread(target=self.startMouseListener)
        self.listenerThread.start()


    def startMouseListener(self) -> None:
        self.listener = mouse.Listener(on_click=self.onClick)
        self.listener.start()


    def onClick(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        if (pg.mouse.get_focused() == False): return
        for button in self.buttons:
            button.onClickLogic(x, y, button, pressed)


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
        goBack: bool = True
        for button in self.buttons:
            if (button.pressed == False): goBack = False
            button.update()
        if (goBack): self.running = False

    
    @override
    def run(self) -> None:
        while self.running:
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    self.running = False

            self.update()
            pg.display.flip()
            self.clock.tick(self.fps)
        
        self.listener.stop()
