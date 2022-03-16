from appium import webdriver
from app.application import Application
import time
from selenium.webdriver.common.by import By

def before_scenario(context, scenario):

    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "Pixel_4_28",
        "app": r"C:\Users\Shkolnyi\PycharmProjects\Appium\my_apk\org.wikipedia.apk",
        "appPackage": "org.wikipedia",
        "appActivity": ".main.MainActivity",
    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)
    # Skip first screen
    time.sleep(2)
    context.driver.find_element(By.ID, "org.wikipedia:id/fragment_onboarding_skip_button").click()
    time.sleep(2)


def after_scenario(context, scenario):
    context.driver.quit()