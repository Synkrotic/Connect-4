import data, pygame as pg
from button import Button
from typing_extensions import override # type: ignore
from pynput import mouse

class DoneButton(Button):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str, page: 'Page', borderRadius: int | None, shadowOffset: int | None) -> None: # type: ignore
        super().__init__(width, height, x, y, colour, hoverColour, text, borderRadius, shadowOffset)
        self.page: 'Page' = page # type: ignore
        self.pressed: bool = False


    def onClickLogic(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        """This function is called when the mouse is clicked.
            And checks if the mouse collides with the button."""
        if (self.rect.collidepoint(pg.mouse.get_pos()) and pressed):
            # self.hovered = False
            self.pressed = not self.pressed

    
    @override
    def logic(self) -> None:
        """Default logic function for the button.
            This is empty because I draw the button separately and the logic is in onClickLogic()."""
        pass
    

    @override
    def isHovered(self):
        """This function is called in the update function in the Button class.
            It checks if the button has been pressed before and keeps the hovercolour when it has been pressed."""
        if (self.pressed): return
        self.hovered = self.rect.collidepoint(pg.mouse.get_pos())
        match self.hovered:
            case True: self.image.fill(self.hoverColour)
            case False: self.image.fill(self.colour)
        self.doBorderRadius()