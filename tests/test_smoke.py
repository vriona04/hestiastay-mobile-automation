import time
import pytest

from pages.home_page import HomePage
from pages.bookings_page import BookingsPage
from pages.profile_page import ProfilePage


def go_home(driver):
    for _ in range(5):
        page = driver.page_source

        if (
            "Welcome back" in page
            or "Hestia PG" in page
            or "Wi-Fi Details" in page
            or "Going on Leave" in page
            or "Home" in page
        ):
            print("Dashboard detected")
            return

        try:
            driver.back()
        except Exception:
            pass

        time.sleep(2)

    print("Could not confirm dashboard")


def test_smoke(logged_in_driver):
    driver = logged_in_driver

    go_home(driver)

    home = HomePage(driver)
    bookings = BookingsPage(driver)
    profile = ProfilePage(driver)

    print("Verifying Dashboard")
    home.verify_dashboard()

    print("Opening Bookings")
    home.open_bookings()
    time.sleep(3)
    bookings.verify()

    try:
        bookings.back()
    except Exception:
        driver.back()

    time.sleep(2)

    go_home(driver)

    print("Opening Profile")
    home.open_profile()
    time.sleep(3)
    profile.verify()

    try:
        profile.back()
    except Exception:
        driver.back()

    time.sleep(2)

    print("SMOKE TEST PASSED")