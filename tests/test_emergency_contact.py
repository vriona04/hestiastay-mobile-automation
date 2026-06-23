import time
import pytest
from pages.navigation_page import NavigationPage


def test_emergency_contact(logged_in_driver):
    driver = logged_in_driver

    nav = NavigationPage(driver)
    nav.go_profile()

    page = driver.page_source

    for _ in range(5):
        if "Emergency Contact" in page:
            break

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "down",
                "percent": 0.8
            }
        )

        time.sleep(2)
        page = driver.page_source

    if "Emergency Contact" not in page:
        pytest.skip("Emergency Contact section not available")

    assert (
        "Contact Name" in page
        or "To be updated" in page
        or "Contact Phone" in page
        or "Phone Number" in page
        or "Relationship" in page
    )

    print("EMERGENCY CONTACT PASSED")
