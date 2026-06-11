import time
from pages.navigation_page import NavigationPage
from pages.profile_details_page import ProfileDetailsPage


def test_profile_details(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    profile = ProfileDetailsPage(driver)

    nav.go_profile()
    time.sleep(3)

    profile.verify_profile_screen()

    print("PROFILE DETAILS PASSED")