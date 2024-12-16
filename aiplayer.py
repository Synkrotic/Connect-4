import pygame as pg, random, os
from typing_extensions import override # type: ignore
from player import Player
from circleItem import CircleItem as Circle

class AIPlayer:
    def __init__(self, colour: tuple[int, int, int], scale: int, game: 'Game', turn: bool) -> None: # type: ignore
        self.gameWidth: int; self.gameHeight: int
        self.gameWidth, self.gameHeight = game.width, game.height
        self.game: 'Game' = game # type: ignore
        self.board: 'Board' = game.board # type: ignore
        self.colour: tuple[int, int, int] = colour
        self.otherColour: tuple[int, int, int] = game.player1.colour
        self.scale: int = scale
        self.items: list[Circle] = []
        self.turn: bool = turn
        self.calculations = 0
        self.move = 1

        # Clear AI-Scores.txt
        with open('AI-Scores.txt', 'w') as file:
            file.write("")

        # Delete all files in /kaas/
        for file in os.listdir('kaas/'):
            os.remove(f"kaas/{file}")
    

    def logic(self) -> None:
        """Make the AI think and make a move."""
        self.calculations = 0
        moveScores: list[dict[int, int]] = self.calculateTurn(1, self.board.copy())
        # self.logScores(moveScores)

        self.game.turn = not self.game.turn


    def logScores(self, moveScores: list[dict[int, int]]) -> None:
        """Log the scores to AI-Scores.txt.
            To later analyse the AI's decision making."""
        text: list[str] = []

        with open('AI-Scores.txt', 'r') as file:
            text.append(file.read())

        move = 0
        for turn in moveScores:
            text.append(f"{move} as {1 if move % 2 == 0 else 2}:\n")
            move += 1
            for x in turn:
                text.append(f"{x}: {turn.get(x)}\n")
            text.append("\n")
        text.append(f"\n\n\n{self.calculations}")

        with open('AI-Scores.txt', 'w') as file:
            file.writelines(text)
        self.move += 1


    def getBestMove(self, movesDict: dict[int, int]) -> int:
        """Returns the highest score and thus the best move to make for the AI.
            If there are multiple moves with the same score, it will randomly choose one."""
        movesList: list[int] = list(movesDict.values())
        reversedDict: dict[int, int] = {v: k for k, v in movesDict.items()}
        highestScore: int = max(movesList)
        xCoords: list[int] = [reversedDict[x] for x in movesList if x == highestScore]
        if (len(xCoords) == 1): return xCoords[0]
        return random.choice(xCoords)
    

    def filterMoveScores(self, moveScores: dict[int, int]) -> dict[int, int]:
        """Filter out all the moves that have a score of 0.
            This is to prevent the AI from making a move that doesn't have any impact.
            If all the moves have a score of 0, it will return the original moveScores."""
        filtered: dict[int, int] = {x: moveScores.get(x) for x in range(len(moveScores)) if moveScores.get(x) != 0}
        return filtered if len(filtered) != 0 else moveScores


    def calculateTurn(self, depth: int, board: 'Board') -> list[dict[int, int]]: # type: ignore
        """Calculate the scores for all the possible moves the AI can make.
            The depth is how many turns ahead the AI should calculate."""
        # board.showInTerminal()
        nextTurnScores: dict[int, int] = {x: self.calculateMove(x, board.copy(), (self.otherColour if depth % 2 == 0 or depth == 0 else self.colour)) for x in range(board.columns)}
        nextTurnScores = self.filterMoveScores(nextTurnScores)
        if (depth == 0):
            return [nextTurnScores]
    
        turns: list[dict[int, int]] = []
        for x, _ in nextTurnScores.items():
            boardy: 'Board' = board.copy() # type: ignore

            circle: Circle = Circle(None, x, (self.otherColour if depth % 2 == 0 or depth == 0 else self.colour), self.scale, self.game, boardy)
            turns.append(self.calculateTurn(depth - 1, boardy))
        return turns + [nextTurnScores]


    def calculateMove(self, x: int, board: 'Board', colour: tuple[int, int, int]) -> int: # type: ignore
        """Calculate the impact of a move on the board.
            The impact is calculated by comparing the score of the board before and after the move."""
        self.calculations += 1
        tempBoard: 'Board' = board.copy() # type: ignore
        boardScore: int = tempBoard.calculatePosition()
        circle: Circle = Circle(None, x, colour, self.scale, self.game, tempBoard)
        newScore: int = tempBoard.calculatePosition()
        impactScore: int = newScore - boardScore

        tempBoard.drawToScreen(self.game.screen)
        pg.image.save(self.game.screen, f"kaas/screenshot_{self.calculations}.png")

        calc: str = f"{self.calculations}: Before: {boardScore} | x: {x} | After: {newScore} | Impact: {impactScore}"
        with open ('AI-Scores.txt', 'r') as file:
            calc = file.read() + "\n" + calc
        with open ('AI-Scores.txt', 'w') as file:
            file.write(calc + ("\n" if self.calculations % 7 == 0 else ""))


        # print(impactScore)
        return impactScore