from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_a11y(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, locator)
            )
        ).click()

    def page_contains(self, text):
        return text in self.driver.page_source

    def save_debug(self, name):
        self.driver.save_screenshot(f"screenshots/{name}.png")
        with open(f"screenshots/{name}.xml", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)

    def scroll_down(self):
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 300,
                "width": 800,
                "height": 1500,
                "direction": "down",
                "percent": 0.8
            }
        )
        time.sleep(2)

    def go_home(self):
        page = self.driver.page_source

        if "Home" in page and "Bookings" in page and "Profile" in page:
            self.click_a11y("Home")
            time.sleep(2)
            return

        if "Back" in page:
            try:
                self.click_a11y("Back")
                time.sleep(2)
            except:
                pass

        page = self.driver.page_source

        if "Home" in page:
            try:
                self.click_a11y("Home")
                time.sleep(2)
            except:
                pass