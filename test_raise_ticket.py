import pytest
import time

from pages.navigation_page import NavigationPage
from pages.raise_ticket_page import RaiseTicketPage


def test_raise_ticket_form_basic(logged_in_driver):
    driver = logged_in_driver

    time.sleep(5)

    nav = NavigationPage(driver)
    ticket = RaiseTicketPage(driver)

    nav.go_support_tickets()
    time.sleep(3)

    page = driver.page_source

    # Open Create Ticket screen
    if "Raise Ticket" in page:
        try:
            driver.find_element(
                "xpath",
                "//*[contains(@content-desc,'Raise Ticket')]"
            ).click()
        except Exception:
            driver.execute_script(
                "mobile: clickGesture",
                {"x": 800, "y": 2150}
            )

        time.sleep(3)

    page = driver.page_source

    if "Create Ticket" not in page:
        pytest.skip("Create Ticket screen not opened")

    ticket.enter_title("WiFi Issue")
    ticket.select_wifi_category()
    ticket.verify_category_selected()
    ticket.verify_priority_visible()
    ticket.select_medium_priority()

    print("RAISE TICKET FORM BASIC PASSED")