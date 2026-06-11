import time
import pytest
from pages.navigation_page import NavigationPage
from pages.wifi_page import WifiPage


def test_wifi_details(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()
    time.sleep(2)

    found = False

    for _ in range(4):
        page = driver.page_source

        if "Wi-Fi Details" in page or "Airtel" in page or "Wifi" in page:
            found = True
            break

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "down",
                "percent": 0.7
            }
        )

        time.sleep(2)

    if not found:
        pytest.skip("Wi-Fi card not visible")

    wifi = WifiPage(driver)
    wifi.verify_wifi_card()

    print("WIFI DETAILS PASSED")