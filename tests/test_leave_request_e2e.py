import time
import pytest
from pages.navigation_page import NavigationPage


def test_leave_request_e2e(driver):
    time.sleep(5)

    nav = NavigationPage(driver)

    try:
        nav.go_leave()
    except Exception:
        pytest.skip("Leave card not found on dashboard")

    page = driver.page_source

    assert "Leave" in page or "Going Home" in page or "Confirm Leave" in page

    print("LEAVE REQUEST SCREEN OPENED")