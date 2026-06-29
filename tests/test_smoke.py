import time

from pages.home_page import HomePage
from pages.bookings_page import BookingsPage
from pages.profile_page import ProfilePage


def test_smoke(driver):

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
        driver.back()
    except Exception:
        pass

    time.sleep(2)

    print("Opening Profile")

    try:
        driver.find_element(
            "xpath",
            "//*[@content-desc='Profile']"
        ).click()
    except Exception:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 900, "y": 2160}
        )

    time.sleep(3)

    profile.verify()

    print("SMOKE TEST PASSED")