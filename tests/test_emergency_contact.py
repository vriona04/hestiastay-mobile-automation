import time
from pages.navigation_page import NavigationPage


def test_emergency_contact(driver):

    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_profile()

    page = driver.page_source

    for _ in range(4):

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

    assert "Emergency Contact" in page
    assert "Contact Name" in page or "To be updated" in page
    assert "Contact Phone" in page or "Phone Number" in page or "9606289728" in page
    assert "Relationship" in page or "Other" in page

    print("EMERGENCY CONTACT PASSED")