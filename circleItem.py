import pygame as pg
import data

class CircleItem:
    def __init__(self, y: int | None, x: int, colour: tuple, scale: int, game: 'Game') -> None: # type: ignore
        self.colour: tuple[int, int, int] = colour
        self.scale: int = scale
        self.width: int = data.CIRCLE_DIAMETER * self.scale
        self.height: int = data.CIRCLE_DIAMETER * self.scale
        self.y: int = 0

        self.squareImage: pg.Surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.squareImage.fill(self.colour)

        self.mask: pg.Surface = pg.Surface(self.squareImage.get_size(), pg.SRCALPHA)
        self.mask.fill(data.TRANSPARENT_COLOUR)
        pg.draw.circle(self.mask, data.BACKGROUND_COLOUR, self.mask.get_rect().center, self.width//2)

        self.image: pg.Surface = self.squareImage.copy()
        self.image.blit(self.mask, (0, 0), special_flags=pg.BLEND_RGBA_MIN)

        self.rect = self.image.get_rect()
        self.setPosition(x, y, game)


    def draw(self, screen: pg.display) -> None:
        screen.blit(self.image, self.rect.topleft)


    def setPosition(self, x: int, y: int, game) -> None:
        yCoords: int = y
        if (y == None): yCoords = self.getLowestY(x, game.board)

        self.y = yCoords

        if (yCoords == -1):
            print("Try again. This column is full.")
            return;

        game.board.setItemAt(x, yCoords, self)

        self.rect.x = self.calcX(x)
        self.rect.y = self.calcY(yCoords, game.height)

        # game.BOARD.showInTerminal()

    def calcX(self, x: int) -> int:
        return (data.CIRCLE_PADDING * self.scale * x) + (x * data.CIRCLE_DIAMETER * self.scale) + (data.FRAME_MARGIN * self.scale)
    

    def calcY(self, y: int, windowHeight: int) -> int:
        return windowHeight - ((data.CIRCLE_DIAMETER * self.scale) + (y * data.CIRCLE_DIAMETER * self.scale) + (data.CIRCLE_PADDING * self.scale * y) + ((data.FRAME_FEET_HEIGHT + data.FRAME_MARGIN)) * self.scale)
    

    def getLowestY(self, x: int, board) -> int:
        for y in range(board.columns):
            if board.getItemAt(x, y).colour == data.BACKGROUND_COLOUR:
                # print(f"Found! {y} for {self.id}")
                return y
        # print(f"None found! For {self.id}")
        return -1