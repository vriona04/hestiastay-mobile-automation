from utils.base_page import BasePage


class BookingsPage(BasePage):

    def verify(self):

        assert self.page_contains("My Bookings")

        booking_checks = [
            "Approved",
            "Room",
            "Booking",
            "Hostel",
            "Check In",
            "Check Out",
            "Status"
        ]

        assert any(
            self.page_contains(item)
            for item in booking_checks
        ), "Booking details not found"

    def back(self):

        try:
            self.click_a11y("Back")

        except:
            self.driver.back()