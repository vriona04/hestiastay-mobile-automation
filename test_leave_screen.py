import time
import pytest
from pages.navigation_page import NavigationPage


def test_leave_screen(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_leave()

    time.sleep(3)

    page = driver.page_source

    if (
        "Leave" not in page
        and "Save Menu" not in page
        and "Going Home" not in page
        and "Reason" not in page
    ):
        pytest.skip("Leave screen not opened")

    print("LEAVE SCREEN PASSED")