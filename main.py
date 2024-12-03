from startpage import StartPage
import data, pygame as pg, sys


pg.init() # Start the pygame module.

# Run the start page. And thus the game.
startPage: StartPage = StartPage(data.WINDOWS_WIDTH, data.WINDOWS_HEIGHT, 1, "Homepage", data.FPS)
startPage.run()

# Quit the pygame module. We can quit it since we reached this code and thus the main loop has been broken.
pg.quit()
sys.exit()