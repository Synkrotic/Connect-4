from startpage import StartPage
import data

startPage = StartPage(data.WINDOWS_WIDTH, data.WINDOWS_HEIGHT, 1, "Homepage", data.FPS)
startPage.run()