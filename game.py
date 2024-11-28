import pygame as pg, sys
from player import Player
from board import Board
from rectangle import Rectangle
from circleItem import CircleItem as Circle
from pynput import mouse
import data, threading

class Game:
    def __init__(self, scale: int, fps: int, ai: bool) -> None:
        pg.init()

        self.ROWS: int = 6
        self.COLUMNS: int = 7
        self.scale: int = scale
        self.width: int = data.WINDOWS_WIDTH * self.scale
        self.height: int = data.WINDOWS_HEIGHT * self.scale
        self.ai: bool = ai

        self.fps: int = fps
        self.board: Board = Board(self.ROWS, self.COLUMNS)
        self.player1: Player = Player(data.PLAYER1_COLOUR, self.scale, (self.width, self.height), self, True)
        self.player2: Player = Player(data.PLAYER2_COLOUR, self.scale, (self.width, self.height), self, False)
        self.circles: list[Circle] = self.getCircles()
        self.background: Rectangle = Rectangle(self.width - ((data.FRAME_FEET_WIDTH * 2) * self.scale), (data.FRAME_FEET_HEIGHT * self.scale) * 2, data.FRAME_FEET_WIDTH * self.scale, self.height - (data.FRAME_FEET_WIDTH * self.scale), data.BACKGROUND_COLOUR, data.RECTANGLE_BORDER_RADIUS)

        self.screen: pg.display = pg.display.set_mode((self.width, self.height), pg.DOUBLEBUF)
        pg.display.set_caption("Connect 4")
        self.clock: pg.time.Clock = pg.time.Clock()

        self.running: bool = True
        self.pressedMouseDown: bool = False
        self.frame: int = 0
        self.turn: bool = True
        self.listener: mouse.Listener | None = None

        self.listenerThread: threading.Thread = threading.Thread(target=self.startMouseListener)
        self.listenerThread.start()
       
        # self.board.showInTerminal()

    def getCircles(self) -> list[Circle]:
        circles: list[Circle] = []
        for x in range(self.COLUMNS):
            for y in range(self.ROWS):
                circles.append(Circle(y, x, data.BACKGROUND_COLOUR, self.scale, self))
        return circles


    def getColorTurnString(self) -> str:
        if (self.turn): return "Player 2"
        return "Player 1"
    

    def getColorTurn(self) -> Player:
        if (self.turn): return self.player1
        return self.player2


    def startMouseListener(self) -> None:
        self.listener = mouse.Listener(on_click=self.updateActivePlayer)
        self.listener.start()


    def updateActivePlayer(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        if (pg.mouse.get_focused() == False): return
        activePlayer: Player = self.getColorTurn()
        activePlayer.onClick(x, y, button, pressed)


    def update(self) -> None:
        check: bool = self.board.checkWin()
        if (check):
            print(f"{self.getColorTurnString()} wins!")
            self.running = False

        self.draw()


    def draw(self) -> None:
        for circle in self.circles:
            circle.draw(self.screen)
        self.background.draw(self.screen)
        self.board.drawToScreen(self.screen)


    def run(self) -> bool:
        while self.running:
            if (self.frame == self.fps - 1): self.pressedMouseDown = False
            if (self.frame == self.fps): self.frame = 0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
    
            self.screen.fill(data.FRAME_COLOUR)
            self.update()
            pg.display.flip()
            self.frame += 1
            self.clock.tick(self.fps)

        self.listener.stop()
        # self.board.showInTerminal()
        # print("Game Over!")
        return False
