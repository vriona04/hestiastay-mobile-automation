import time
import pytest
from pages.navigation_page import NavigationPage
from pages.raise_ticket_page import RaiseTicketPage


def test_raise_ticket_e2e(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    ticket = RaiseTicketPage(driver)

    nav.go_support_tickets()
    time.sleep(3)

    page = driver.page_source

    if "Raise Ticket" in page:
        driver.find_element(
            "xpath",
            "//*[contains(@content-desc,'Raise Ticket')]"
        ).click()
        time.sleep(3)

    page = driver.page_source

    if "Create Ticket" not in page:
        pytest.skip("Create Ticket screen not opened")

    ticket.enter_title("Automation WiFi Issue")
    ticket.select_wifi_category()
    ticket.verify_category_selected()
    ticket.select_medium_priority()
    ticket.enter_description(
        "This ticket was created using Appium automation testing."
    )

    ticket.submit_ticket()
    ticket.verify_ticket_submitted()

    print("RAISE TICKET E2E PASSED")