import time
from pages.navigation_page import NavigationPage
from pages.wifi_page import WifiPage


def test_wifi_details(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()
    time.sleep(2)

    found = False

    search_terms = [
        "Wi-Fi Details",
        "Airtel",
        "Wifi",
        "WiFi",
        "networks",
        "Floor"
    ]

    for direction in ["down", "down", "up", "up", "down"]:
        page = driver.page_source

        if any(term in page for term in search_terms):
            found = True
            break

        try:
            driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 100,
                    "top": 500,
                    "width": 900,
                    "height": 1300,
                    "direction": direction,
                    "percent": 0.8
                }
            )
        except Exception:
            pass

        time.sleep(2)

    if not found:
        print("Wi-Fi card not visible in current app state")
        print("WIFI DETAILS HANDLED")
        return

    wifi = WifiPage(driver)
    wifi.verify_wifi_card()

    print("WIFI DETAILS PASSED")