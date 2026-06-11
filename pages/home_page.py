from utils.base_page import BasePage


class HomePage(BasePage):

    LEAVE_CARD = (
        "Going on Leave?\n"
        "Let your hostel know when you'll be away"
    )

    def verify_dashboard(self):

        assert self.page_contains("Welcome back")

        dashboard_checks = [
            "Hestia PG",
            "Your Hostel",
            "Room",
            "Wi-Fi Details",
            "Bookings",
            "Profile"
        ]

        assert any(
            self.page_contains(item)
            for item in dashboard_checks
        ), "Dashboard content not found"

    def open_bookings(self):
        self.click_a11y("Bookings")

    def open_profile(self):
        self.click_a11y("Profile")

    def open_leave(self):

        try:
            self.click_a11y(self.LEAVE_CARD)

        except Exception:

            print(
                "Leave card locator failed, tapping by coordinates"
            )

            self.driver.execute_script(
                "mobile: clickGesture",
                {
                    "x": 540,
                    "y": 1400
                }
            )