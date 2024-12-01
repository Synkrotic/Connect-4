import pygame as pg, data
from doneButton import DoneButton

class EndScreen:
    def __init__(self, width: int, height: int, x: int, y: int, winner: str) -> None:
        self.width: int = width
        self.height: int = height
        self.x: int = x
        self.y: int = y
        self.winner: str = winner

        pg.display.set_caption("Connect 4 | End Screen")

        font: pg.font.FontType = pg.font.Font("Resources/PixelFont.ttf", int(data.BUTTON_FONT_SIZE * 1.5))
        self.winner = font.render(f"{self.winner} won!", True, data.WHITE)

        self.backButton: DoneButton = DoneButton((self.width//18) * 5, self.height//12, self.width//2 - (self.width//36 * 5), self.height - (self.height//8 + self.height//24),
                                            data.BUTTON_MENU_COLOUR, data.BUTTON_MENU_HOVER_COLOUR, "BACK", self, None, None)
        
        self.background: pg.Surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.background.fill(data.GAME_ENDED_COLOUR)
    
    def logic(self) -> bool:
        self.backButton.update()
        if (self.backButton.pressed):
            return True
        return False


    def draw(self, screen: pg.display) -> None:
        screen.blit(self.background, (0, 0))
        screen.blit(self.winner, (self.width//2 - self.winner.get_width()//2, self.height//2 - self.winner.get_height()//2))
        self.backButton.draw(screen)
