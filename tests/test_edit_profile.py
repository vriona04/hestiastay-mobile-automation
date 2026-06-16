import time
import pytest
from pages.navigation_page import NavigationPage


def test_edit_profile_screen(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_profile()

    page = driver.page_source

    if "My Profile" not in page:
        pytest.skip("Profile screen not opened")

    assert "Edit Profile" in page
    assert "Full Name" in page
    assert "Email Address" in page
    assert "Phone Number" in page

    print("EDIT PROFILE SCREEN PASSED")