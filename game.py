import pygame as pg, data, threading
from player import Player
from aiplayer import AIPlayer
from board import Board
from rectangle import Rectangle
from circleItem import CircleItem as Circle
from pynput import mouse
from endscreen import EndScreen

class Game:
    def __init__(self, scale: int, fps: int, ai: bool) -> None:

        self.ROWS: int = 6
        self.COLUMNS: int = 7
        self.scale: int = scale
        self.width: int = data.WINDOWS_WIDTH * self.scale
        self.height: int = data.WINDOWS_HEIGHT * self.scale
        self.ai: bool = ai

        self.fps: int = fps
        self.board: Board = Board(self.ROWS, self.COLUMNS)
        self.player1: Player = Player(data.player1_colour, self.scale, (self.width, self.height), self, True)
        if (not self.ai):
            self.player2: Player = Player(data.player2_colour, self.scale, (self.width, self.height), self, False)
        else:
            self.player2: AIPlayer = AIPlayer(data.player2_colour, self.scale, self, False)
        self.circles: list[Circle] = self.getCircles()
        self.background: Rectangle = Rectangle(self.width - ((data.FRAME_FEET_WIDTH * 2) * self.scale), (data.FRAME_FEET_HEIGHT * self.scale) * 2, data.FRAME_FEET_WIDTH * self.scale, self.height - (data.FRAME_FEET_WIDTH * self.scale), data.BACKGROUND_COLOUR, data.RECTANGLE_BORDER_RADIUS)

        self.screen: pg.display = pg.display.set_mode((self.width, self.height), pg.SRCALPHA)
        pg.display.set_caption("Connect 4 | Game")
        self.clock: pg.time.Clock = pg.time.Clock()

        self.running: bool = True
        self.pressedMouseDown: bool = False
        self.frame: int = 0
        self.ended: bool = False
        self.turn: bool = True

        self.listener: mouse.Listener | None = None
        self.endScreen: EndScreen | None = None

        self.listenerThread: threading.Thread = threading.Thread(target=self.startMouseListener)
        self.listenerThread.start()
       
        # circle: Circle = Circle(None, 0, data.player1_colour, self.scale, self, self.board)
        # circle: Circle = Circle(None, 0, data.player2_colour, self.scale, self, self.board)
        # circle: Circle = Circle(None, 1, data.player2_colour, self.scale, self, self.board)
        # circle: Circle = Circle(None, 1, data.player2_colour, self.scale, self, self.board)
        # circle: Circle = Circle(None, 1, data.player2_colour, self.scale, self, self.board)

        # self.board.showInTerminal()

    def getCircles(self) -> list[Circle]:
        """Return a list of Circle objects that make the holes in the frame."""
        circles: list[Circle] = []
        for x in range(self.COLUMNS):
            for y in range(self.ROWS):
                circles.append(Circle(y, x, data.BACKGROUND_COLOUR, self.scale, self, self.board))
        return circles


    def getColorTurnString(self) -> str:
        """Return the string of the player whose turn it was.
            This will be used when someone has won the game."""
        if (self.turn): return "Player 2"
        return "Player 1"
    

    def getColorTurn(self) -> Player:
        """Return the player object of which players turn it is."""
        if (self.turn): return self.player1
        return self.player2


    def startMouseListener(self) -> None:
        """Start listening for mouse inputs.
            And updating the player when pressed."""
        self.listener = mouse.Listener(on_click=self.updateActivePlayer)
        self.listener.start()


    def updateActivePlayer(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        """Update the active player when the mouse is pressed.
            If you play against an AI the AI will think and play their move."""
        if (pg.mouse.get_focused() == False): return;
        if (self.ended):
            self.endScreen.backButton.onClickLogic(x, y, button, pressed)
            return;
        if (self.ai and not self.turn): return;
        activePlayer: Player = self.getColorTurn()
        activePlayer.onClick(x, y, button, pressed)


    def update(self) -> None:
        """Updates the logic and executes the draw function.
            At the end it checks if someone has won or if the game is a tie."""
        self.draw()

        if (self.ended): 
            if (self.endScreen.logic()):
                self.running = False
            return;

        tie: bool = False
        if (self.board.checkWin() or (tie := self.board.checkTie())):
            winner = self.getColorTurnString()
            print(f"{winner} wins!" if not tie else "It's a tie!")
            self.endScreen = EndScreen(self.width, self.height, 0, 0, f"{winner} won!" if not tie else "It's a tie!")
            self.ended = True
            return;
        
        if (self.ai and not self.turn):
            self.player2.logic()

        
    def draw(self) -> None:
        """First it draws the background circles, then it draws the background rectangle (the rectangle that create the feet of the frame).
            Then it circles that are in the board.
            If the game is ended it will draw the endscreen over the rest."""
        for circle in self.circles:
            circle.draw(self.screen)
        self.background.draw(self.screen)
        self.board.drawToScreen(self.screen)

        if (self.ended): self.endScreen.draw(self.screen)



    def run(self) -> bool:
        """The main loop of the game, it executes the update function checks if the window is closed and keeps track of which frame we are on."""
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
