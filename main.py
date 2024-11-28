from startpage import StartPage
import data, pygame as pg, sys

startPage = StartPage(data.WINDOWS_WIDTH, data.WINDOWS_HEIGHT, 1, "Homepage", data.FPS)
startPage.run()
pg.quit()
sys.exit()