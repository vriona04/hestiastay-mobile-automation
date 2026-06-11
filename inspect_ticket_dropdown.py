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

try:
    time.sleep(5)

    # Click category dropdown
    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Select equipment category"
    ).click()

    time.sleep(3)

    driver.save_screenshot("ticket_category_popup.png")

    with open("ticket_category_popup.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved ticket_category_popup.xml")

finally:
    driver.quit()