import time
from pages.navigation_page import NavigationPage


def test_vacate_form_basic(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_vacate()

    time.sleep(5)
    page = driver.page_source

    assert (
        "Vacate" in page
        or "New Request" in page
        or "Reason" in page
        or "Request" in page
    ), "Vacate form not found"

    print("VACATE FORM BASIC PASSED")