import time
import pytest
from pages.navigation_page import NavigationPage
from pages.payment_history_page import PaymentHistoryPage


def test_payment_history(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()

    time.sleep(2)

    if "History" not in driver.page_source:
        pytest.skip("History tab not visible")

    driver.find_element(
        "xpath",
        "//*[@content-desc='History']"
    ).click()

    time.sleep(3)

    history = PaymentHistoryPage(driver)
    history.verify_payment_history()

    print("PAYMENT HISTORY PASSED")
