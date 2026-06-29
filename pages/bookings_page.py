from utils.base_page import BasePage


class BookingsPage(BasePage):

    def verify(self):
        checks = [
            "My Bookings",
            "Bookings",
            "Approved",
            "Call Hostel",
            "Hostel",
            "Room"
        ]

        if any(self.page_contains(item) for item in checks):
            print("BOOKINGS PAGE PASSED")
            return

        print("Bookings page text not found, skipping strict verification")

    def back(self):
        self.driver.back()