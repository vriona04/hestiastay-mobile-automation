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

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(5)

driver.save_screenshot("need_help.png")

with open("need_help.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved need_help.png and need_help.xml")

driver.quit()