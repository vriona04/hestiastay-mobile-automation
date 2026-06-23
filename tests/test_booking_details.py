import time
import pytest
from pages.navigation_page import NavigationPage


@pytest.mark.stable
def test_booking_details(logged_in_driver):
    driver = logged_in_driver

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

    # Return to dashboard for next test
    for _ in range(3):
        try:
            driver.back()
            time.sleep(2)
            page = driver.page_source

            if (
                "Welcome back" in page
                or "Hestia PG" in page
                or "Wi-Fi Details" in page
                or "Going on Leave?" in page
                or "Home" in page
            ):
                print("Returned to dashboard")
                break
        except Exception:
            pass