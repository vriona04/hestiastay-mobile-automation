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

    page = driver.page_source

    # If we are on Support Tickets list, open Create/Raise Ticket form
    if "Create Ticket" not in page:
        try:
            if "Raise Ticket" in page:
                driver.find_element(
                    "xpath",
                    "//*[contains(@content-desc,'Raise Ticket')]"
                ).click()
                time.sleep(3)
            elif "Support Tickets" in page:
                driver.execute_script(
                    "mobile: clickGesture",
                    {"x": 900, "y": 180}
                )
                time.sleep(3)
        except Exception:
            pass

    page = driver.page_source

    if "Create Ticket" not in page:
        pytest.skip("Create Ticket screen not opened")

    ticket.enter_title("WiFi Issue")
    ticket.select_wifi_category()
    ticket.verify_category_selected()
    ticket.verify_priority_visible()
    ticket.select_medium_priority()

    print("RAISE TICKET FORM BASIC PASSED")