from utils.base_page import BasePage
import time


class NavigationPage(BasePage):

    def go_home(self):
        for _ in range(8):
            page = self.driver.page_source

            if "Welcome back" in page:
                return

            if "Back" in page:
                try:
                    self.click_a11y("Back")
                except:
                    self.driver.back()
            else:
                self.driver.back()

            time.sleep(1)

    def go_bookings(self):
        self.go_home()
        self.click_a11y("Bookings")
        time.sleep(2)

    def go_profile(self):
        self.go_home()
        self.click_a11y("Profile")
        time.sleep(2)

    def go_leave(self):
        self.go_home()

        try:
            self.click_a11y(
                "Going on Leave?\nLet your hostel know when you'll be away"
            )
        except:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 1180}
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

        if "Support Tickets" in self.driver.page_source:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 820, "y": 2160}
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
        except:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 800}
            )

        time.sleep(3)