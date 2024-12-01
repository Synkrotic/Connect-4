from button import Button
from colourspage import ColoursPage
from typing_extensions import override # type: ignore

class ChangeColourPageButton(Button):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str, mainPage: 'Page') -> None: # type: ignore
        super().__init__(width, height, x, y, colour, hoverColour, text, None)
        self.mainPage: 'Page' = mainPage # type: ignore


    @override
    def logic(self) -> None:
        page: 'Page' = ColoursPage(self.mainPage.width, self.mainPage.height, self.mainPage.scale, "Colours", self.mainPage.fps) # type: ignore
        page.run()