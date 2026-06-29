import time
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def is_login_screen(self):
        page = self.driver.page_source
        return (
            "Welcome Back" in page
            or "Sign in to your account" in page
            or "Email Address" in page
            or "Sign In" in page
            or "Choose an account" in page
        )

    def login(self, email, password):
        page = self.driver.page_source

        if "Choose an account" in page:
            self.select_google_account()
            self.handle_biometric_popup()
            return

        print("Starting login")

        fields = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.EditText"
        )

        print("Fields found:", len(fields))
        assert len(fields) >= 2, "Email/password fields not found"

        fields[0].click()
        time.sleep(1)
        fields[0].clear()
        fields[0].send_keys(email)
        print("Email entered")

        fields[1].click()
        time.sleep(1)
        fields[1].clear()
        fields[1].send_keys(password)
        print("Password entered")

        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

        time.sleep(2)

        print("Clicking Sign In")
        self.driver.execute_script(
            "mobile: clickGesture",
            {"x": 540, "y": 1800}
        )

        print("Sign In clicked")
        time.sleep(8)

        if "Choose an account" in self.driver.page_source:
            self.select_google_account()

        self.handle_biometric_popup()

        time.sleep(10)

    def select_google_account(self):
        print("Google account picker detected")

        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("monikamuthumula@gmail.com")'
        ).click()

        print("Google account selected")
        time.sleep(15)

    def handle_biometric_popup(self):
        page = self.driver.page_source

        if "Enable Face/Fingerprint Login?" in page:
            print("Biometric popup detected")

            self.driver.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "Not Now"
            ).click()

            print("Clicked Not Now")
            time.sleep(8)

    def verify_dashboard(self):
        print("Waiting for dashboard...")
        time.sleep(8)

        page = self.driver.page_source

        assert (
            "Bookings" in page
            or "Profile" in page
            or "Wi-Fi" in page
            or "Hestia PG" in page
            or "Room" in page
            or "Home" in page
            or "Welcome back" in page
        ), "Dashboard not found"