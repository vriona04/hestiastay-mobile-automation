from utils.base_page import BasePage
import time


class NavigationPage(BasePage):

    def go_home(self):
        for _ in range(8):
            page = self.driver.page_source

            if "Welcome back" in page:
                return

            try:
                self.driver.back()
            except Exception:
                pass

            time.sleep(1)

    def go_bookings(self):
        self.go_home()

        try:
            self.click_a11y("Bookings")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 280, "y": 2160}
            )

        time.sleep(2)

    def go_profile(self):
        self.go_home()

        try:
            self.click_a11y("Profile")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 900, "y": 2160}
            )

        time.sleep(2)

    def go_leave(self):
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
                    "percent": 0.6
                }
            )
        except Exception:
            pass

        time.sleep(2)

        try:
            self.click_a11y(
                "Going on Leave?\nLet your hostel know when you'll be away"
            )
        except Exception:
            try:
                self.click_a11y("Going on Leave?")
            except Exception:
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 540, "y": 1500}
                )

        time.sleep(3)

    def go_support_tickets(self):
        self.go_home()

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

        self.driver.execute_script(
            "mobile: clickGesture",
            {"x": 540, "y": 1650}
        )

        time.sleep(3)

    def go_payment(self):
        self.go_home()

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
            self.click_a11y("View Details")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 800}
            )

        time.sleep(3)

    def go_vacate(self):
        self.go_home()

        # Open drawer/menu from top-right button
        self.driver.execute_script(
            "mobile: clickGesture",
            {"x": 1010, "y": 175}
        )

        time.sleep(2)

        try:
            self.click_a11y("Vacate\nVacate hostel room")
        except Exception:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 450, "y": 1400}
            )

        time.sleep(3)