import pygame as pg

class Page:
    def __init__(self, width: int, height: int, scale: int, pageName: str, fps: int) -> None:
        pg.init()

        self.scale: int = scale
        self.width: int = width * self.scale
        self.height: int = height * self.scale
        self.pageName: str = pageName
        self.fps: int = fps

        self.screen: pg.display = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption(self.pageName)
        pg.display.set_icon(pg.image.load("icon.png"))
        self.clock: pg.time.Clock = pg.time.Clock()

        self.running: bool = True


    def update(self) -> None:
        self.logic()
        self.draw()


    def logic() -> None:
        pass


    def draw(self) -> None:
        pass


    def run(self) -> None:
        while self.running:
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    self.running = False

            self.update()
            pg.display.flip()
            self.clock.tick(self.fps)