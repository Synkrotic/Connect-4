import pygame as pg, data
from player import Player
from circleItem import CircleItem as Circle

class Board:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows: int = rows
        self.columns: int = columns
        self.layout: list[list[None | Circle]] = [[None for _ in range(self.columns)] for _ in range(self.rows)]
    

    def drawToScreen(self, screen: pg.display) -> None:
        for row in self.layout:
            for item in row:
                if (item == None or item.colour == data.BACKGROUND_COLOUR): continue
                item.draw(screen)


    def getInverseCoords(self, x: int, y: int) -> tuple:
        return (self.rows - y - 1, x)


    def getItemAt(self, x: int, y: int) -> Player | None:
        if (x < 0 or x > self.rows or
            y  < 0 or y > self.columns): return None
        xCoord: int; yCoord: int
        xCoord, yCoord = self.getInverseCoords(x, y)
        return self.layout[xCoord][yCoord]


    def setItemAt(self, x: int, y: int, value: Player) -> bool:
        if (x < 0 or x > self.rows or
            y  < 0 or y > self.columns): return False
        xCoord: int; yCoord: int
        xCoord, yCoord = self.getInverseCoords(x, y)
        self.layout[xCoord][yCoord] = value
        return True


    def delItemAt(self, x: int, y: int) -> bool:
        if (x < 0 or x > self.rows or
            y  < 0 or y > self.columns): return False
        xCoord: int; yCoord: int
        xCoord, yCoord = self.getInverseCoords(x, y)
        self.layout[xCoord][yCoord] = None
        return True
    

    def showInTerminal(self) -> None:
        for row in self.layout:
            for item in row:
                if (item == None): print("N", end = " | ")
                elif (item.colour == data.PLAYER1_COLOUR): print("1", end = " | ")
                elif (item.colour == data.PLAYER2_COLOUR): print("2", end = " | ")
                else: print("?", end = " | ")
            print("\n")
            