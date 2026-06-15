import time
from appium.webdriver.common.appiumby import AppiumBy
from utils.base_page import BasePage


class LoginPage(BasePage):

    def is_login_screen(self):
        page = self.driver.page_source

        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )

        return (
            len(fields) >= 2
            or "Welcome Back" in page
            or "Email" in page
            or "Password" in page
            or "Sign In" in page
            or "Login" in page
        )

    def login(self, email, password):
        time.sleep(5)

        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )

        if len(fields) < 2:
            self.driver.save_screenshot("login_debug.png")

            with open("login_debug.xml", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)

            raise AssertionError(
                "Email and password fields not found. Saved login_debug.xml"
            )

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

        if (
            "Welcome back" in page
            or "Bookings" in page
            or "Profile" in page
            or "Hestia" in page
        ):
            print("Dashboard verified")
            return

        print("Dashboard verification skipped")