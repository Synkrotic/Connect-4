import pygame as pg
from typing_extensions import override # type: ignore
from player import Player
from circleItem import CircleItem as Circle
import random

class AIPlayer:
    def __init__(self, colour: tuple[int, int, int], scale: int, game: 'Game', turn: bool) -> None: # type: ignore
        self.gameWidth: int; self.gameHeight: int
        self.gameWidth, self.gameHeight = game.width, game.height
        self.game: 'Game' = game # type: ignore
        self.board: 'Board' = game.board # type: ignore
        self.colour: tuple[int, int, int] = colour
        self.scale: int = scale
        self.items: list[Circle] = []
        self.turn: bool = turn
        self.move = 1
    

    def logic(self) -> None:
        moveScores: list[int] = [self.calculateMove(x) for x in range(self.game.COLUMNS)]
        if self.checkAllSameScore(moveScores):
            nextMove: int = random.randint(0, self.game.COLUMNS - 1)
        else:
            nextMove: int = moveScores.index(max(moveScores))
        self.items.append(Circle(None, nextMove, self.colour, self.scale, self.game, self.board))

        self.game.turn = not self.game.turn

        # Log data in AI-Scores.txt
        text: list[str] = []
        with open('AI-Scores.txt', 'r') as file:
            text.append(file.read())
        text.append(f"{self.move}: {moveScores}\n")
        with open('AI-Scores.txt', 'w') as file:
            file.writelines(text)
        self.move += 1


    def checkAllSameScore(self, scores: list[int]) -> bool:
        return all(score == scores[0] for score in scores)


    def calculateMove(self, x) -> int:
        tempBoard: 'Board' = self.board.copy() # type: ignore
        boardScore: int = tempBoard.calculatePosition()
        circle: Circle = Circle(None, x, self.colour, self.scale, self.game, tempBoard)
        newScore: int = tempBoard.calculatePosition()
        impactScore: int = newScore - boardScore
        return impactScore