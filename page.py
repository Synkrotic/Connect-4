import pygame as pg

class Page:
    def __init__(self, width: int, height: int, scale: int, pageName: str, fps: int) -> None:

        self.scale: int = scale
        self.width: int = width * self.scale
        self.height: int = height * self.scale
        self.pageName: str = pageName
        self.fps: int = fps

        self.screen: pg.display = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(f"Connect 4 | {self.pageName}")
        pg.display.set_icon(pg.image.load("Resources/icon.png"))
        self.clock: pg.time.Clock = pg.time.Clock()

        self.running: bool = True


    def update(self) -> None:
        """Run the logic and draw functions."""
        self.logic()
        self.draw()


    def logic() -> None:
        """This is the default logic function. It is empty since every page has other logic.
            This is why we use the @override decorator in the other page classes."""
        pass


    def draw(self) -> None:
        """This is the default draw function. It is empty since every page draws other objects.
            This is why we use the @override decorator in the other page classes."""
        pass


    def run(self) -> None:
        """Run the main loop of the page so its shown on the screen."""
        while self.running:
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    self.running = False

            self.update()
            pg.display.flip()
            self.clock.tick(self.fps)