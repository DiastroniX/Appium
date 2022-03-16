from screens.base_screen import Screen
from selenium.webdriver.common.by import By


class launchScreen(Screen):
    SKIP_BUTTON = ((By.ID, "org.wikipedia:id/fragment_onboarding_skip_button"))

    def click_skip(self):
        self.click(*self.SKIP_BUTTON)
