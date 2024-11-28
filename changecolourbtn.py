from button import Button

class ChangeColourButton(Button):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], text: str) -> None:
        super().__init__(width, height, x, y, colour, hoverColour, text)
