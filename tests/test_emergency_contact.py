import time
from pages.navigation_page import NavigationPage
from pages.emergency_contact_page import EmergencyContactPage


def test_emergency_contact(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    emergency = EmergencyContactPage(driver)

    nav.go_profile()
    time.sleep(3)

    driver.execute_script(
        "mobile: scrollGesture",
        {
            "left": 100,
            "top": 600,
            "width": 900,
            "height": 1200,
            "direction": "down",
            "percent": 0.9
        }
    )

    time.sleep(2)

    emergency.verify_emergency_contact()

    print("EMERGENCY CONTACT PASSED")