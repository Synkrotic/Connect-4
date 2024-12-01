import pygame as pg, data
from circleItem import CircleItem as Circle
from pynput import mouse

class Player:
    def __init__(self, colour: tuple[int, int, int], scale: int, gameSize: tuple[int, int], game: 'Game', turn: bool) -> None: # type: ignore
        self.gameWidth: int; self.gameHeight: int
        self.gameWidth, self.gameHeight = gameSize
        self.game: 'Game' = game # type: ignore
        self.colour: tuple[int, int, int] = colour
        self.scale: int = scale
        self.items: list[Circle] = []
        self.turn: bool = turn

        
    def getColumn(self, xCoord: int) -> int:
        for column, boundaries in data.columnBoundaries.items():
            if (boundaries[0] <= xCoord <= boundaries[1]): return column
        return -1

    
    def onClick(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        if (pressed and button == mouse.Button.left):
            xCoord: int = pg.mouse.get_pos()[0]
            column: int = self.getColumn(xCoord)
            if (column == -1): return;
        
            circle: Circle = Circle(y=None, x=column, colour=self.colour, scale=self.scale, game=self.game, board=self.game.board)
            if (circle.y != -1):
                self.items.append(circle)
                self.game.turn = not self.game.turn   