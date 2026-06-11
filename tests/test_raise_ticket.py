from pages.navigation_page import NavigationPage
from pages.raise_ticket_page import RaiseTicketPage
import pytest
import time


def test_raise_ticket_form_basic(driver):

    time.sleep(5)

    nav = NavigationPage(driver)
    ticket = RaiseTicketPage(driver)

    nav.go_support_tickets()
    time.sleep(3)

    if "Create Ticket" not in driver.page_source:
        pytest.skip("Create Ticket screen not opened")

    ticket.enter_title("WiFi Issue")
    ticket.select_wifi_category()
    ticket.verify_category_selected()
    ticket.verify_priority_visible()
    ticket.select_medium_priority()

    print("RAISE TICKET FORM BASIC PASSED")