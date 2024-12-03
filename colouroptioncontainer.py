import pygame as pg, data
from changecolourbtn import ChangeColourButton

class ColourOptionContainer:
    def __init__(self, x: int, y: int, playerID: int) -> None:
        self.x: int = x
        self.y: int = y
        self.playerID: int = playerID
        self.pickedColourID: int | None = None
        self.buttons: list[ChangeColourButton] = []
        self.otherContainer: 'ColourOptionContainer' | None = None
        
        colourID: int = 0
        for i in range(0, 3):
            for j in range(0, 3):
                colour: tuple[int, int, int] = data.USERCOLOURS.get(colourID)
                hoverColour: tuple[int, int, int] = tuple(colourVal - 50 if colourVal - 50 >= 0 else 0 for colourVal in colour)
                xCoord = int(self.x + data.COLOUR_BUTTON_DIAMETER//2 + (data.COLOUR_BUTTON_DIAMETER + data.COLOUR_BUTTON_DIAMETER//2) * j)
                yCoord = int(self.y + (data.COLOUR_BUTTON_DIAMETER + data.COLOUR_BUTTON_DIAMETER//2) * i)
                self.buttons.append(ChangeColourButton(data.COLOUR_BUTTON_DIAMETER, data.COLOUR_BUTTON_DIAMETER, xCoord, yCoord, colour, hoverColour, self.playerID, self))
                self.buttons[-1].picked = True if (self.playerID == 1 and data.player1_colour == colour) or (self.playerID == 2 and data.player2_colour == colour) else False
                if self.buttons[-1].picked: self.pickedColourID = colourID
                colourID += 1


    def getOtherColourID(self, otherContainer: 'ColourOptionContainer') -> int:
        """Returns the colour ID of the other container's picked colour."""
        self.otherContainer = otherContainer
        for button in self.otherContainer.buttons:
            if (data.USERCOLOURID.get(button.colour) == self.pickedColourID):
                button.otherChoice = True
        return self.otherContainer.pickedColourID


    def update(self) -> None:
        """Updates the colour buttons."""
        for button in self.buttons:
            if (data.USERCOLOURID.get(button.colour) != self.otherContainer.pickedColourID):
                button.otherChoice = False
                button.update()
            else: button.otherChoice = True


    def draw(self, screen: pg.Surface) -> None:
        """Draws the colour buttons to the screen."""
        for button in self.buttons:
            button.draw(screen)
            button.drawLocked(screen)