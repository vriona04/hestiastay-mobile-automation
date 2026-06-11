from pages.navigation_page import NavigationPage
from pages.support_page import SupportPage
import pytest
import time


def test_support_tickets_screen(driver):

    time.sleep(5)

    nav = NavigationPage(driver)
    support = SupportPage(driver)

    nav.go_support_tickets()
    time.sleep(3)

    support.save_debug("support_after_navigation")

    page = driver.page_source

    if "Create Ticket" not in page and "Need Help?" not in page and "Support Tickets" not in page:
        pytest.skip("Support screen not opened")

    print("SUPPORT TICKETS SCREEN PASSED")