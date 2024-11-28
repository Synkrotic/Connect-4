from startpage import StartPage
import data

startPage = StartPage(data.WINDOWS_WIDTH, data.WINDOWS_HEIGHT, "Homepage", data.FPS)
startPage.run()