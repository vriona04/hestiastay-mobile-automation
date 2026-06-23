import time
import pytest
from pages.navigation_page import NavigationPage


@pytest.mark.stable
def test_edit_profile_screen(logged_in_driver):
    driver = logged_in_driver

    time.sleep(5)

    nav = NavigationPage(driver)

    # Go to dashboard first
    nav.go_home()
    time.sleep(2)

    # Open profile
    nav.go_profile()
    time.sleep(3)

    page = driver.page_source

    # Verify Edit Profile screen
    assert (
        "My Profile" in page
        or "Edit Profile" in page
        or "Personal Information" in page
        or "Email Address" in page
        or "Phone Number" in page
        or "Profile" in page
    ), "Edit Profile screen not found"

    print("EDIT PROFILE SCREEN PASSED")

    # Return to dashboard for next test
    try:
        driver.back()
        time.sleep(2)
    except Exception:
        pass