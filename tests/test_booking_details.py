from pages.navigation_page import NavigationPage
from pages.booking_details_page import BookingDetailsPage
import time


def test_booking_details(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    booking = BookingDetailsPage(driver)

    nav.go_bookings()
    time.sleep(3)

    booking.verify_bookings_screen()
    booking.verify_booking_card()
    booking.verify_call_hostel_button()

    print("BOOKING DETAILS PASSED")