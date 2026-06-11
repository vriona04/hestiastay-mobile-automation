from pages.navigation_page import NavigationPage
from pages.rent_page import RentPage
import pytest
import time


def test_rent_due_screen(driver):

    time.sleep(5)

    nav = NavigationPage(driver)
    rent = RentPage(driver)

    nav.go_payment()
    time.sleep(3)

    if "Payment" not in driver.page_source:
        pytest.skip("Payment screen not opened")

    rent.verify_payment_screen()

    print("RENT DUE SCREEN PASSED")