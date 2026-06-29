import time
from pages.navigation_page import NavigationPage


def test_payment_details(driver):

    nav = NavigationPage(driver)

    print("Opening Payment Screen")
    nav.go_payment()

    time.sleep(5)

    page = driver.page_source

    with open(
        "screenshots/payment_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("Payment screen XML saved")

    search_terms = [
        "Payment",
        "Rent",
        "Receipt",
        "History",
        "Amount",
        "Due",
        "Paid",
        "Download Official Receipt"
    ]

    found = any(term in page for term in search_terms)

    assert found, "Payment details screen not opened"

    print("PAYMENT DETAILS PASSED")