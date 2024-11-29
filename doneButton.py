import data
from button import Button
from typing_extensions import override # type: ignore
from game import Game

class DoneButton(Button):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str, page: 'Page', borderRadius: int | None) -> None: # type: ignore
        super().__init__(width, height, x, y, colour, hoverColour, text, borderRadius)
        self.page: 'Page' = page # type: ignore


    @override
    def logic(self) -> None:
        pass