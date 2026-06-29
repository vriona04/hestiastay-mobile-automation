import time
from pages.navigation_page import NavigationPage


def test_booking_details(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_bookings()
    time.sleep(3)

    page = driver.page_source

    assert (
        "My Bookings" in page
        or "Bookings" in page
        or "Approved" in page
        or "Call Hostel" in page
        or "SLN PG" in page
    ), "Booking details not found"

    print("BOOKING DETAILS PASSED")

    try:
        driver.back()
        time.sleep(2)
    except Exception:
        pass