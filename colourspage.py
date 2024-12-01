import pygame as pg, data, threading
from page import Page
from changecolourbtn import ChangeColourButton
from doneButton import DoneButton
from button import Button
from typing_extensions import override # type: ignore
from rectangle import Rectangle
from game import Game
from pynput import mouse
from colouroptioncontainer import ColourOptionContainer

class ColoursPage(Page):
    def __init__(self, width: int, height: int, scale: int, pageName: str, fps: int) -> None:
        super().__init__(width, height, scale, pageName, fps)
        self.text: list = []        
        self.doneButtons: list[Button] = []
        self.colourButtons: list[ChangeColourButton] = []

        self.listener: mouse.Listener | None = None

        self.doneButtons.append(DoneButton((self.width//18) * 5, self.height//12, (self.width//9), self.height - (self.height//18 + self.height//12),
                                            data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "DONE", self, None, None))
        
        self.doneButtons.append(DoneButton((self.width//18) * 5, self.height//12, self.width - (self.width//9 + (self.width//18 * 5)), self.height - (self.height//18 + self.height//12),
                                            data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "DONE", self, None, None))
        
        self.splitterLine: Rectangle = Rectangle(data.SPLITTER_WIDTH, self.height, self.width/2, 0, data.BLACK, 0)

        font: pg.font.FontType = pg.font.Font("Resources/PixelFont.ttf", int(data.BUTTON_FONT_SIZE * 1.5))
        self.textPlayer1 = font.render("Player 1", True, data.BUTTON_FONT_COLOUR)
        self.textPlayer2 = font.render("Player 2", True, data.BUTTON_FONT_COLOUR)


        self.colourOptions1: ColourOptionContainer = ColourOptionContainer(0, self.height//100 * 29, 1)
        self.colourOptions2: ColourOptionContainer = ColourOptionContainer(data.WINDOWS_WIDTH//2 + data.SPLITTER_WIDTH, self.height//100 * 29, 2)
        self.colourOptions1.getOtherColourID(self.colourOptions2)
        self.colourOptions2.getOtherColourID(self.colourOptions1)

        self.listenerThread: threading.Thread = threading.Thread(target=self.startMouseListener)
        self.listenerThread.start()


    def startMouseListener(self) -> None:
        self.listener = mouse.Listener(on_click=self.onClick)
        self.listener.start()


    def onClick(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        if (pg.mouse.get_focused() == False): return
        for button in self.doneButtons:
            button.onClickLogic(x, y, button, pressed)


    @override
    def draw(self) -> None:
        self.screen.fill(data.BACKGROUND_COLOUR)
        self.screen.blit(self.textPlayer1, (self.width//4 - self.textPlayer1.get_width()//2, self.height//9))

        self.screen.blit(self.splitterLine.image, self.splitterLine.rect.topleft)

        self.screen.blit(self.textPlayer2, (self.width - (self.width//4 + self.textPlayer2.get_width()//2), self.height//9))
        for button in self.doneButtons:
            button.draw(self.screen)
        for button in self.colourButtons:
            button.draw(self.screen)

        self.colourOptions1.draw(self.screen)
        self.colourOptions2.draw(self.screen)


    @override
    def logic(self) -> None:
        pg.display.set_caption(f"Connect 4 | {self.pageName}")
        goBack: bool = True
        for button in self.doneButtons:
            if (button.pressed == False): goBack = False
            button.update()
        for button in self.colourButtons:
            button.update()
        self.colourOptions1.update()
        self.colourOptions2.update()
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
