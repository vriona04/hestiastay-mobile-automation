from pages.home_page import HomePage
from pages.bookings_page import BookingsPage
from pages.profile_page import ProfilePage


def test_smoke(logged_in_driver):
    driver = logged_in_driver

    home = HomePage(driver)
    bookings = BookingsPage(driver)
    profile = ProfilePage(driver)

    print("Verifying Dashboard")
    home.verify_dashboard()

    print("Opening Bookings")
    home.open_bookings()
    bookings.verify()
    bookings.back()

    print("Opening Profile")
    home.open_profile()
    profile.verify()
    profile.back()

    print("SMOKE TEST PASSED")