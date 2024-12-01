from startpage import StartPage
from colourspage import ColoursPage
import data, pygame as pg, sys

pg.init()

startPage: StartPage = StartPage(data.WINDOWS_WIDTH, data.WINDOWS_HEIGHT, 1, "Homepage", data.FPS)
startPage.run()

# coloursPage: ColoursPage = ColoursPage(data.WINDOWS_WIDTH, data.WINDOWS_HEIGHT, 1, "Homepage", data.FPS)
# coloursPage.run()

pg.quit()
sys.exit()