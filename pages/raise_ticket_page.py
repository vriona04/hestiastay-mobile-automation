from utils.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time


class RaiseTicketPage(BasePage):

    def enter_title(self, title):
        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )
        fields[0].clear()
        fields[0].send_keys(title)

    def select_wifi_category(self):
        self.click_a11y("Select equipment category")
        time.sleep(2)

        self.driver.execute_script(
            "mobile: clickGesture",
            {"x": 550, "y": 815}
        )

        time.sleep(2)

    def select_medium_priority(self):
        self.click_a11y("Medium")

    def verify_category_selected(self):
        assert "WiFi" in self.driver.page_source

    def verify_priority_visible(self):
        assert "Low" in self.driver.page_source
        assert "Medium" in self.driver.page_source
        assert "High" in self.driver.page_source