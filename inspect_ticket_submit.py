from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "RZCY8011AKW"
options.app_package = "com.hostelrs.guest"
options.app_activity = "com.hostelrs.MainActivity"
options.no_reset = True

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

try:
    time.sleep(5)

    driver.execute_script(
        "mobile: scrollGesture",
        {
            "left": 100,
            "top": 500,
            "width": 800,
            "height": 1400,
            "direction": "down",
            "percent": 0.9
        }
    )

    time.sleep(2)

    driver.save_screenshot("ticket_bottom.png")

    with open("ticket_bottom.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved ticket_bottom.xml")

finally:
    driver.quit()