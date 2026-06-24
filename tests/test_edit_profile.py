import time
from pages.navigation_page import NavigationPage


def test_edit_profile_screen(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_profile()
    time.sleep(3)

    page = driver.page_source

    assert (
        "My Profile" in page
        or "Edit Profile" in page
        or "Personal Information" in page
        or "Email Address" in page
        or "Phone Number" in page
    ), "Edit Profile screen not found"

    print("EDIT PROFILE SCREEN PASSED")

    try:
        driver.back()
        time.sleep(2)
    except Exception:
        pass