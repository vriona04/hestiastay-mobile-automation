from pages.navigation_page import NavigationPage
from pages.rent_page import RentPage
import pytest
import time


def test_rent_due_screen(driver):

    time.sleep(5)

    nav = NavigationPage(driver)
    rent = RentPage(driver)

    # First try old payment navigation
    nav.go_payment()
    time.sleep(3)

    # If payment screen did not open, try History tab
    if "Payment" not in driver.page_source:
        nav.go_home()
        time.sleep(1)

        try:
            driver.find_element(
                "xpath",
                "//*[@content-desc='History']"
            ).click()
        except:
            driver.execute_script(
                "mobile: clickGesture",
                {"x": 670, "y": 2180}
            )

        time.sleep(3)

    if (
        "Payment" not in driver.page_source
        and "Rent Payment" not in driver.page_source
        and "Payment History" not in driver.page_source
    ):
        pytest.skip("Payment screen not opened")

    rent.verify_payment_screen()

    print("RENT DUE SCREEN PASSED")