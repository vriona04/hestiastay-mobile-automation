from pages.home_page import HomePage
from pages.leave_page import LeavePage
import pytest
import time


def test_leave_flow(driver):
    time.sleep(5)

    home = HomePage(driver)
    leave = LeavePage(driver)

    if "You are on Leave" in driver.page_source:
        pytest.skip("Leave already active")

    print("Opening Leave Screen")
    home.open_leave()

    time.sleep(3)

    if "Going Home" not in driver.page_source:
        pytest.skip("Leave form not available")

    print("Selecting Reason")
    leave.select_reason()

    print("Confirming Leave")
    leave.confirm_leave()

    print("Verifying Active Leave")
    leave.verify_active_leave()

    print("LEAVE FLOW PASSED")