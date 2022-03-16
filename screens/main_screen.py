from screens.base_screen import Screen
from selenium.webdriver.common.by import By

class mainScreen(Screen):
    SEARCH = (By.ID, 'org.wikipedia:id/search_container')

    def click_search(self):
        self.click(*self.SEARCH)
        