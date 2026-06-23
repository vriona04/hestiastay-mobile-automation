import time
import pytest
from pages.navigation_page import NavigationPage


def test_vacate_requests(logged_in_driver):
    driver = logged_in_driver

    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_vacate()

    page = driver.page_source

    assert (
        "Vacate" in page
        or "Requests" in page
        or "New Request" in page
        or "Past Requests" in page
    ), "Vacate requests not found"

    print("VACATE REQUESTS PASSED")