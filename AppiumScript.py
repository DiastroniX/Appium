from appium import webdriver
from selenium.webdriver.common.by import By
import time

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Pixel_4_28",
    "app": r"C:\Users\Shkolnyi\PycharmProjects\Appium\my_apk\org.wikipedia.apk",
    "appPackage": "org.wikipedia",
    "appActivity": ".main.MainActivity",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

driver.implicitly_wait(5)


#Skip first screen
time.sleep(2)
driver.find_element(By.ID, "org.wikipedia:id/fragment_onboarding_skip_button").click()

#Search test
time.sleep(2)
driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()

time.sleep(2)
e = driver.find_element(By.ID, 'org.wikipedia:id/search_src_text')
e.clear()
e.send_keys('Python')
time.sleep(2)
text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text
assert 'Python' in text, f'Expected Python to be in (text)'
