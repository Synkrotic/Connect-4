import pygame as pg, data
from button import Button
from rectangle import Rectangle

class ChangeColourButton(Button):
    def __init__(self, width: int, height: int, x: int, y: int, colour: tuple[int, int, int], hoverColour: tuple[int, int, int], id: int, container: 'ColourOptionContainer') -> None: # type: ignore
        super().__init__(width, height, x, y, colour, hoverColour, "", height//2, height//8)
        self.playerID: int = id
        self.picked: bool = False
        self.otherChoice: bool = False
        self.container: 'ColourOptionContainer' = container # type: ignore
        self.corners: dict[str, tuple[int, int]] = {
            "topLeft": (self.x + self.width*0.14, self.y + self.height*0.14),
            "topRight": (self.x + (self.width*0.86), self.y + self.height*0.14),
            "center": (self.x + self.width//2, self.y + self.height//2),
            "bottomLeft": (self.x + self.width*0.14, self.y + (self.height*0.86)),
            "bottomRight": (self.x + (self.width*0.86), self.y + (self.height*0.86))
        }


    def logic(self) -> None:
        """Changes the colour of the player to the colour of the button."""
        if (self.playerID == 1): data.player1_colour = self.colour
        elif (self.playerID == 2): data.player2_colour = self.colour
        else: return;
        for button in self.container.buttons:
            button.picked = False
        self.picked = True
        self.container.pickedColourID = data.USERCOLOURID.get(self.colour)


    def drawLocked(self, screen: pg.display) -> None:
        """Locks the button when the other player has chosen the colour.
            When locked it draws a gray circle to the position."""
        if (self.picked):
            self.outline: Rectangle = Rectangle(self.width + (data.BUTTON_OUTLINE_WIDTH * 4), self.height + (data.BUTTON_OUTLINE_WIDTH * 4),
                                            self.x - (data.BUTTON_OUTLINE_WIDTH * 2), self.y - (data.BUTTON_OUTLINE_WIDTH * 2), data.USER_CHOSEN_OUTLINE_COLOUR, self.borderRadius + (data.BUTTON_OUTLINE_WIDTH * 2))
            # pg.draw.line(screen, data.BLACK, self.corners.get("topLeft"), self.corners.get("bottomRight"), self.width//8)
            # pg.draw.line(screen, data.BLACK, self.corners.get("topRight"), self.corners.get("bottomLeft"), self.width//8)
        else:
            self.outline: Rectangle = Rectangle(self.width + (data.BUTTON_OUTLINE_WIDTH * 2), self.height + (data.BUTTON_OUTLINE_WIDTH * 2),
                                            self.x - data.BUTTON_OUTLINE_WIDTH, self.y - data.BUTTON_OUTLINE_WIDTH, data.BLACK, self.borderRadius + data.BUTTON_OUTLINE_WIDTH)
        if (self.otherChoice):
            circle_surface = pg.Surface((data.CIRCLE_DIAMETER, data.CIRCLE_DIAMETER), pg.SRCALPHA)
            pg.draw.circle(circle_surface, data.ALREADY_PICKED_COLOUR, (data.CIRCLE_DIAMETER//2, data.CIRCLE_DIAMETER//2), data.CIRCLE_DIAMETER//5 * 2)
            circle_surface.set_alpha(255)
            screen.blit(circle_surface, (self.corners.get("center")[0] - data.CIRCLE_DIAMETER//2, self.corners.get("center")[1] - data.CIRCLE_DIAMETER//2))
            # pg.draw.line(screen, data.BLACK, self.corners.get("topRight"), self.corners.get("bottomLeft"), self.width//8)