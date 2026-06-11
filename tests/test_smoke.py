from pages.navigation_page import NavigationPage
from pages.home_page import HomePage
from pages.bookings_page import BookingsPage
from pages.profile_page import ProfilePage
import time


def test_smoke(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    home = HomePage(driver)
    bookings = BookingsPage(driver)
    profile = ProfilePage(driver)

    nav.go_home()

    print("Verifying Dashboard")
    home.verify_dashboard()

    print("Opening Bookings")
    nav.go_bookings()
    bookings.verify()
    bookings.back()

    time.sleep(2)

    print("Opening Profile")
    nav.go_profile()
    profile.verify()
    profile.back()

    print("SMOKE TEST PASSED")