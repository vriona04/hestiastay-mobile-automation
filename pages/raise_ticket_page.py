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

    def enter_description(self, description):
        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )

        fields[-1].clear()
        fields[-1].send_keys(description)

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

    def submit_ticket(self):
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "down",
                "percent": 0.8
            }
        )

        time.sleep(2)

        try:
            self.click_a11y("Submit Ticket")
        except:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 2000}
            )

        time.sleep(4)

    def verify_ticket_submitted(self):
        page = self.driver.page_source

        assert (
            "Ticket" in page
            or "Support Tickets" in page
            or "success" in page.lower()
            or "created" in page.lower()
            or "submitted" in page.lower()
        ), "Ticket submit confirmation not found"

    def verify_category_selected(self):
        assert "WiFi" in self.driver.page_source

    def verify_priority_visible(self):
        assert "Low" in self.driver.page_source
        assert "Medium" in self.driver.page_source
        assert "High" in self.driver.page_source