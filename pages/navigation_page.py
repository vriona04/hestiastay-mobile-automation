from utils.base_page import BasePage
import time


class NavigationPage(BasePage):

    def go_home(self):
        for _ in range(10):
            page = self.driver.page_source

            if "Welcome back" in page:
                return

            try:
                self.driver.back()
                time.sleep(1)
            except Exception:
                pass

            page = self.driver.page_source

            if "Welcome back" in page:
                return

            try:
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 70, "y": 170}
                )
                time.sleep(1)
            except Exception:
                pass

        raise Exception("Home screen not reached")

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

        for _ in range(5):

            page = self.driver.page_source

            if "Going on Leave?" in page:
                try:
                    self.click_a11y(
                        "Going on Leave?\nLet your hostel know when you'll be away"
                    )
                except Exception:
                    try:
                        self.click_a11y("Going on Leave?")
                    except Exception:
                        pass

                time.sleep(3)
                return

            try:
                self.driver.execute_script(
                    "mobile: scrollGesture",
                    {
                        "left": 100,
                        "top": 600,
                        "width": 900,
                        "height": 1200,
                        "direction": "down",
                        "percent": 0.5
                    }
                )
            except Exception:
                pass

            time.sleep(2)

        raise Exception("Leave card not found")

    def go_support_tickets(self):
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
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 540, "y": 1650}
            )
        except Exception:
            pass

        time.sleep(3)

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

        try:
            self.driver.execute_script(
                "mobile: clickGesture",
                {"x": 1010, "y": 175}
            )
        except Exception:
            pass

        time.sleep(2)

        try:
            self.click_a11y("Vacate\nVacate hostel room")
        except Exception:
            try:
                self.driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 450, "y": 1400}
                )
            except Exception:
                pass

        time.sleep(3)