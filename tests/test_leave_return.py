from pages.leave_page import LeavePage
import pytest
import time


def test_leave_return(driver):
    time.sleep(5)

    leave = LeavePage(driver)

    print("Verifying Active Leave")

    if "You are on Leave" not in driver.page_source:
        pytest.skip("No active leave available to return")

    leave.verify_active_leave()

    print("Ending Leave")
    leave.end_leave()

    time.sleep(3)

    assert "Welcome back" in driver.page_source

    print("LEAVE RETURN PASSED")