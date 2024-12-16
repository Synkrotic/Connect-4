import pygame as pg, data
from player import Player
from circleItem import CircleItem as Circle

class Board:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows: int = rows
        self.columns: int = columns
        self.layout: list[list[None | Circle]] = [[None for _ in range(self.columns)] for _ in range(self.rows)]
    

    def drawToScreen(self, screen: pg.display) -> None:
        """Draws the board to the screen.
            By iterating through all the circles in the board and
            drawing them if they aren't None or the background colour."""
        for row in self.layout:
            for item in row:
                if (item == None or item.colour == data.BACKGROUND_COLOUR): continue
                item.draw(screen)


    def getInverseCoords(self, x: int, y: int) -> tuple:
        """Returns the inverse coordinates of the given coordinates."""
        return (self.rows - y - 1, x)


    def clear(self):
        """Clear the board by setting all the items to None."""
        self.layout = [[None for _ in range(self.columns)] for _ in range(self.rows)]


    def getItemAt(self, x: int, y: int) -> Circle | None:
        """Retrieve the item at the given coordinates."""
        if (x < 0 or x > self.rows or
            y  < 0 or y > self.columns): return None
        xCoord: int; yCoord: int
        xCoord, yCoord = self.getInverseCoords(x, y)
        return self.layout[xCoord][yCoord]


    def setItemAt(self, x: int, y: int, value: Player) -> bool:
        """Set the item at the given coordinates to the given value."""
        if (x < 0 or x > self.rows or
            y  < 0 or y > self.columns): return False
        xCoord: int; yCoord: int
        xCoord, yCoord = self.getInverseCoords(x, y)
        self.layout[xCoord][yCoord] = value
        return True


    def delItemAt(self, x: int, y: int) -> bool:
        """Delete the item at the given coordinates."""
        if (x < 0 or x > self.rows or
            y  < 0 or y > self.columns): return False
        xCoord: int; yCoord: int
        xCoord, yCoord = self.getInverseCoords(x, y)
        self.layout[xCoord][yCoord] = None
        return True
    

    def copy(self) -> 'Board':
        """Returns a copy of the board."""
        newBoard: Board = Board(self.rows, self.columns)
        for x in range(len(newBoard.layout)):
            for y in range(len(newBoard.layout[x])):
                newBoard.layout[x][y] = Circle(self.getItemAt(x, y).y, self.getItemAt(x, y).x, self.getItemAt(x, y).colour, self.getItemAt(x, y).scale, self.getItemAt(x, y).game, newBoard)
        return newBoard


    def showInTerminal(self) -> None:
        """Prints the board to the terminal by iterating through the items
            and checking if the colour is player1_colour or player2_colour.
            Used for debugging purposes."""
        for row in self.layout:
            for item in row:
                if (item == None): print("N", end = " | ")
                elif (item.colour == data.player1_colour): print("1", end = " | ")
                elif (item.colour == data.player2_colour): print("2", end = " | ")
                else: print("?", end = " | ")
            print("\n")


    def checkTie(self) -> bool:
        """Check if the game is a tie.
            By iterating through all the items in the board
            and checking if there are any empty spots."""
        for x in range(self.columns):
            for y in range(self.rows):
                if (self.getItemAt(x, y).colour == data.BACKGROUND_COLOUR): return False
        return True


    def checkWin(self) -> bool | str:
        """Check if the game has been won.
            By iterating through all the items in the board and checking if there are any 4 in a row."""
        for x in range(self.columns):
            for y in range(self.rows):
                if (self.getItemAt(x, y) == None): tie = False
                if (self.getItemAt(x, y).colour == data.BACKGROUND_COLOUR): continue
                if (self.checkHorizontal(x, y) == 3 or self.checkVertical(x, y) == 3 or self.checkDiagonalLeft(x, y) == 3 or self.checkDiagonalRight(x, y) == 3): return True
        return False


    def checkHorizontal(self, x: int, y: int) -> int:
        """Check if there are 4 in a row horizontally."""
        if (x > self.columns - 4): return False
        result: int = 0
        colour: tuple[int, int, int] = self.getItemAt(x, y).colour
        for i in range(1, 4):
            circle: Circle = self.getItemAt(x + i, y)

            if (circle == None or circle.colour == data.BACKGROUND_COLOUR): continue
            elif (circle.colour == colour): result += 1
            elif (circle.colour != colour): 
                result = 0
                break
        return result


    def checkVertical(self, x: int, y: int) -> int:
        """Check if there are 4 in a row vertically."""
        if (y > self.rows - 4): return 0
        result: int = 0
        colour: tuple[int, int, int] = self.getItemAt(x, y).colour
        for i in range(1, 4):
            circle: Circle = self.getItemAt(x, y + i)

            if (circle == None or circle.colour == data.BACKGROUND_COLOUR): continue
            elif (circle.colour == colour): result += 1
            elif (circle.colour != colour): 
                result = 0
                break
        return result
    

    def checkDiagonalLeft(self, x: int, y: int) -> int:
        """Check if there are 4 in a row diagonally to the left."""
        result: int = 0
        colour: tuple[int, int, int] = self.getItemAt(x, y).colour
        for i in range(1, 4):
            circle: Circle = self.getItemAt(x + i, y + i)

            if (circle == None or circle.colour == data.BACKGROUND_COLOUR): continue
            elif (circle.colour == colour): result += 1
            elif (circle.colour != colour): 
                result = 0
                break
        return result
    

    def checkDiagonalRight(self, x: int, y: int) -> int:
        """Check if there are 4 in a row diagonally to the right."""
        result: int = 0
        colour: tuple[int, int, int] = self.getItemAt(x, y).colour
        for i in range(1, 4):
            circle: Circle = self.getItemAt(x - i, y + i)

            if (circle == None or circle.colour == data.BACKGROUND_COLOUR): continue
            elif (circle.colour == colour): result += 1
            elif (circle.colour != colour): 
                result = 0
                break
        return result
    

    def calculatePosition(self) -> int:
        """Give the current position of the board a score.
            This is done by checking how long the connections are between circles."""
        score: int = 0
        for i in range(self.columns):
            for j in range(self.rows):
                score += self.checkHorizontal(i, j) if self.checkHorizontal(i, j) != 3 else 100
                score += self.checkVertical(i, j) if self.checkVertical(i, j) != 3 else 100
                score += self.checkDiagonalLeft(i, j) if self.checkDiagonalLeft(i, j) != 3 else 100
                score += self.checkDiagonalRight(i, j) if self.checkDiagonalRight(i, j) != 3 else 100
        return score
