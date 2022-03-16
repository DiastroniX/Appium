from screens.launch_screen import launchScreen
from screens.main_screen import mainScreen
from screens.search_screen import searchScreen

class Application:

    def __init__(self, driver):
        self.launch_screen = launchScreen(driver)
        self.main_screen = mainScreen(driver)
        self.search_screen = searchScreen(driver)