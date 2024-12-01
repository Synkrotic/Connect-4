import data
from button import Button
from typing_extensions import override # type: ignore
from game import Game

class StartButton(Button):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str, ai: bool, page: 'Page') -> None: # type: ignore
        super().__init__(width, height, x, y, colour, hoverColour, text, None)
        self.ai = ai
        self.mainPage = page


    @override
    def logic(self) -> None:
        print("Starting game against " + ("AI" if self.ai else "Player"))
        page: 'Page' = Game(self.mainPage.scale, self.mainPage.fps, self.ai) # type: ignore
        page.run()