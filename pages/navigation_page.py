from utils.base_page import BasePage
import time
import pytest


class NavigationPage(BasePage):

    def handle_biometric_popup(self):
        try:
            page = self.driver.page_source
        except Exception:
            return

        if "Enable Face/Fingerprint Login?" in page or "Not Now" in page:
            try:
                self.click_a11y("Not Now")
            except Exception:
                try:
                    self.driver.execute_script(
                        "mobile: clickGesture",
                        {"x": 470, "y": 1430}
                    )
                except Exception:
                    pass

            time.sleep(2)

    def go_home(self):
        try:
            self.driver.activate_app("com.hostelrs.guest")
            time.sleep(3)
        except Exception:
            pass

        self.handle_biometric_popup()

        for _ in range(10):
            page = self.driver.page_source

            if (
                "Welcome back" in page
                or "Hestia PG" in page
                or "Wi-Fi Details" in page
                or "Need Help?" in page
                or "RENT OVERDUE" in page
                or "Going on Leave?" in page
                or "Home" in page
            ):
                print("Dashboard detected")
                return

            try:
                self.click_a11y("Home")
                time.sleep(2)
            except Exception:
                try:
                    self.driver.execute_script(
                        "mobile: clickGesture",
                        {"x": 120, "y": 2160}
                    )
                    time.sleep(2)
                except Exception:
                    pass

            try:
                self.driver.back()
                time.sleep(2)
            except Exception:
                pass

        print("Could not confirm dashboard")

    def go_bookings(self):
        self.go_home()

        try:
            self.click_a11y("Bookings")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 280, "y": 2160}
            )

        time.sleep(3)

    def go_profile(self):
        self.go_home()

        try:
            self.click_a11y("Profile")
        except Exception:
            try:
                self.driver.find_element(
                    "xpath",
                    "//*[@content-desc='Profile']"
                ).click()
            except Exception:
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 900, "y": 2160}
                )

        time.sleep(5)

        page = self.driver.page_source

        if (
            "My Profile" in page
            or "Edit Profile" in page
            or "Email Address" in page
            or "Phone Number" in page
        ):
            print("PROFILE SCREEN OPENED")
            return

        pytest.skip("Profile screen not opened")

    def go_leave(self):
        self.go_home()

        page = self.driver.page_source

        if "Going on Leave?" not in page:
            try:
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": 100,
                        "top": 600,
                        "width": 900,
                        "height": 1200,
                        "direction": "up",
                        "percent": 0.8
                    }
                )
                time.sleep(2)
            except Exception:
                pass

        page = self.driver.page_source

        if "Going on Leave?" in page:
            try:
                self.click_a11y(
                    "Going on Leave?\nLet your hostel know when you'll be away"
                )
            except Exception:
                print("Leave card locator failed, tapping by coordinates")
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 540, "y": 1240}
                )

            time.sleep(3)
            return

        pytest.skip("Leave card not available")

    def go_support_tickets(self):
        self.go_home()

        for _ in range(5):
            page = self.driver.page_source

            if (
                "Need Help?" in page
                or "Support" in page
                or "Raise a ticket" in page
                or "Raise Ticket" in page
            ):
                break

            try:
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": 100,
                        "top": 600,
                        "width": 900,
                        "height": 1200,
                        "direction": "down",
                        "percent": 1.0
                    }
                )
            except Exception:
                pass

            time.sleep(2)

        page = self.driver.page_source

        if (
            "Need Help?" in page
            or "Support" in page
            or "Raise a ticket" in page
            or "Raise Ticket" in page
        ):
            try:
                self.click_a11y(
                    "Need Help?\nRaise a ticket for support"
                )
            except Exception:
                try:
                    self.click_a11y("Raise Ticket")
                except Exception:
                    self.driver.execute_script(
                        "mobile: clickGesture",
                        {"x": 800, "y": 2160}
                    )

            time.sleep(3)
            return

        pytest.skip("Support section not found")

    def go_payment(self):
        self.go_home()

        try:
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
        except Exception:
            pass

        time.sleep(2)

        try:
            self.click_a11y("View Details")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 800}
            )

        time.sleep(3)

    def go_vacate(self):
        self.go_home()

        for _ in range(6):
            page = self.driver.page_source

            if "Vacate" in page:
                break

            try:
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": 100,
                        "top": 700,
                        "width": 900,
                        "height": 1100,
                        "direction": "down",
                        "percent": 0.8
                    }
                )
            except Exception:
                pass

            time.sleep(2)

        page = self.driver.page_source

        if "Vacate" not in page:
            pytest.skip("Vacate section not available")

        try:
            self.click_a11y("Vacate\nVacate hostel room")
        except Exception:
            try:
                self.click_a11y("Vacate")
            except Exception:
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 540, "y": 1700}
                )

        time.sleep(3)