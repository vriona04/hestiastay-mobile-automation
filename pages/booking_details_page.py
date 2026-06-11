from utils.base_page import BasePage


class BookingDetailsPage(BasePage):

    def verify_bookings_screen(self):
        page = self.driver.page_source

        assert (
            "My Bookings" in page
            or "Bookings" in page
            or "Pending" in page
            or "Approved" in page
        ), "Bookings screen not found"

    def verify_booking_card(self):
        page = self.driver.page_source

        booking_checks = [
            "Hestia PG",
            "SLN PG",
            "Approved",
            "Check-in",
            "Booked on",
            "Call Hostel",
            "Pending"
        ]

        assert any(
            item in page for item in booking_checks
        ), "Booking card not found"

    def verify_call_hostel_button(self):
        page = self.driver.page_source

        assert (
            "Call Hostel" in page
            or "Approved" in page
            or "Booked on" in page
        ), "Booking action/details not found"