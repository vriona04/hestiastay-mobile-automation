from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "RZCY8011AKW"
options.app_package = "com.hostelrs.guest"
options.app_activity = "com.hostelrs.MainActivity"
options.no_reset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

def save(name):
    driver.save_screenshot(f"{name}.png")
    with open(f"{name}.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"Saved {name}.xml")

try:
    time.sleep(5)
    save("ticket_start_debug")

    page = driver.page_source

    if "Select equipment category" in page:
        print("Clicking category dropdown")
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Select equipment category"
        ).click()
        time.sleep(2)
        save("ticket_category_opened")

    page = driver.page_source

    if "WiFi" in page:
        print("Selecting WiFi by coordinates")
        driver.execute_script(
            "mobile: clickGesture",
            {
                "x": 550,
                "y": 815
            }
        )
        time.sleep(2)
        save("ticket_after_category")
    else:
        print("WiFi option not found")
        save("ticket_wifi_not_found")

finally:
    driver.quit()