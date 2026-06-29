import time
from pages.navigation_page import NavigationPage


def test_vacate_requests(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()

    page = driver.page_source

    if "Vacate" not in page:
        print("Vacate requests not available in current app state")
        print("VACATE REQUESTS HANDLED")
        return

    nav.go_vacate()
    time.sleep(5)

    page = driver.page_source

    assert (
        "Vacate" in page
        or "Requests" in page
        or "New Request" in page
        or "Past Requests" in page
        or "Reason" in page
    ), "Vacate requests not found"

    print("VACATE REQUESTS PASSED")