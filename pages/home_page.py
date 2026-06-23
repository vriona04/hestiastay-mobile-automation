from utils.base_page import BasePage


class HomePage(BasePage):

    LEAVE_CARD = (
        "Going on Leave?\n"
        "Let your hostel know when you'll be away"
    )

    def verify_dashboard(self):
        dashboard_checks = [
            "Welcome back",
            "Hestia",
            "Hestia PG",
            "Your Hostel",
            "Room",
            "Wi-Fi",
            "Wi-Fi Details",
            "Bookings",
            "Profile",
            "Home"
        ]

        assert any(
            self.page_contains(item)
            for item in dashboard_checks
        ), "Dashboard content not found"

    def open_bookings(self):
        try:
            self.click_a11y("Bookings")
        except Exception:
            print("Bookings locator failed, tapping bottom navigation")
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 2220}
            )

    def open_profile(self):
        try:
            self.click_a11y("Profile")
        except Exception:
            print("Profile locator failed, tapping bottom navigation")
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 900, "y": 2220}
            )

    def open_leave(self):
        try:
            self.click_a11y(self.LEAVE_CARD)
        except Exception:
            print("Leave card locator failed, tapping by coordinates")
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 1400}
            )