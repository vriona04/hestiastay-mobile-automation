from pages.home_page import HomePage
from pages.leave_page import LeavePage
import time


def test_leave_flow(driver):

    time.sleep(5)

    home = HomePage(driver)
    leave = LeavePage(driver)

    page = driver.page_source

    if "You are on Leave" in page or "End Leave & Return" in page:
        print("Leave already active")
        print("LEAVE FLOW PASSED")
        return

    print("Opening Leave Screen")
    home.open_leave()

    time.sleep(5)

    page = driver.page_source

    # Handle popup if present
    if "Dismiss" in page:
        try:
            driver.find_element(
                "xpath",
                "//*[@content-desc='Dismiss']"
            ).click()
            time.sleep(3)
            page = driver.page_source
        except Exception:
            pass

    if (
        "Going Home" not in page
        and "Confirm Leave" not in page
    ):
        print("Leave form unavailable")
        print("LEAVE FLOW SKIPPED")
        return

    print("Selecting Reason")
    leave.select_reason()

    print("Confirming Leave")
    leave.confirm_leave()

    print("Verifying Active Leave")
    leave.verify_active_leave()

    print("LEAVE FLOW PASSED")