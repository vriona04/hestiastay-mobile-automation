from utils.driver_factory import get_driver
from pages.navigation_page import NavigationPage
import time

driver = get_driver()

try:
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()

    time.sleep(2)

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

    driver.save_screenshot("dashboard_bottom.png")

    with open("dashboard_bottom.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved dashboard_bottom.png and dashboard_bottom.xml")

finally:
    driver.quit()