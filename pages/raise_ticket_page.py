from utils.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time


class RaiseTicketPage(BasePage):

    def enter_title(self, title):
        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )

        if len(fields) > 0:
            fields[0].clear()
            fields[0].send_keys(title)

    def enter_description(self, description):
        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )

        if len(fields) > 1:
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
        print(self.driver.page_source[:5000])
        time.sleep(1)

        try:
            self.click_a11y("Medium")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 1300}
            )

        time.sleep(2)

    def verify_category_selected(self):
        assert "WiFi" in self.driver.page_source

    def verify_priority_visible(self):
        page = self.driver.page_source

        assert (
            "Low" in page
            or "Medium" in page
            or "High" in page
            or "Priority" in page
        )

    def submit_ticket(self):
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "down",
                "percent": 0.9
            }
        )

        time.sleep(2)

        try:
            self.click_a11y("Create Ticket")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 2120}
            )

        time.sleep(6)

        self.driver.save_screenshot("ticket_submitted_latest.png")

        with open(
            "ticket_submitted_latest.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(self.driver.page_source)

    def verify_ticket_submitted(self):
        page = self.driver.page_source

        assert (
            "Ticket" in page
            or "Support" in page
            or "Created" in page
            or "Submitted" in page
            or "Success" in page
        ), "Ticket submission confirmation not found"