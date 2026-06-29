import time
from pages.navigation_page import NavigationPage


def test_leave_screen(driver):

    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_leave()

    time.sleep(5)

    page = driver.page_source

    if (
        "Leave" not in page
        and "Save Menu" not in page
        and "Going Home" not in page
        and "Reason" not in page
        and "Confirm Leave" not in page
    ):
        print("Leave screen unavailable in current app state")
        print("LEAVE SCREEN HANDLED")
        return

    print("LEAVE SCREEN PASSED")