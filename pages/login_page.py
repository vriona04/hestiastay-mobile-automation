import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage


class LoginPage(BasePage):

    def login(self, email, password):
        time.sleep(3)

        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )

        assert len(fields) >= 2, "Email and password fields not found"

        fields[0].click()
        fields[0].clear()
        fields[0].send_keys(email)

        fields[1].click()
        fields[1].clear()
        fields[1].send_keys(password)

        time.sleep(1)

        try:
            self.click_a11y("Sign In")
        except Exception:
            try:
                self.click_a11y("Login")
            except Exception:
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 540, "y": 1780}
                )

        time.sleep(8)

    def verify_dashboard(self):
        page = self.driver.page_source

        assert (
            "Welcome back" in page
            or "Bookings" in page
            or "Profile" in page
            or "Hestia" in page
        ), "Dashboard not opened after login"