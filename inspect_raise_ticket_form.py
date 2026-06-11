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

    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Raise Ticket"
    ).click()

    time.sleep(3)

    driver.save_screenshot("raise_ticket_form.png")

    with open("raise_ticket_form.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved raise_ticket_form.xml")

finally:
    driver.quit()