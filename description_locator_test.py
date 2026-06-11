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

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

time.sleep(5)

edits = driver.find_elements(
    AppiumBy.CLASS_NAME,
    "android.widget.EditText"
)

print("EditTexts:", len(edits))

for i, e in enumerate(edits):
    print(f"EditText {i}")
    print("Text:", e.text)
    print("Location:", e.location)
    print("Size:", e.size)
    print("-" * 40)

driver.quit()