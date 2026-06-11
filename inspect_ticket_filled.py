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

    fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
    print("Fields found:", len(fields))

    fields[0].clear()
    fields[0].send_keys("WiFi issue")
    print("Title entered")

    # Tap category box by coordinates
    driver.execute_script("mobile: clickGesture", {"x": 540, "y": 1340})
    time.sleep(2)

    # Select WiFi from popup
    driver.execute_script("mobile: clickGesture", {"x": 550, "y": 815})
    time.sleep(2)
    print("WiFi selected")

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Medium").click()
    print("Medium priority selected")

    fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
    fields[-1].clear()
    fields[-1].send_keys("WiFi is not working properly in my room.")
    print("Description entered")

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

    driver.save_screenshot("ticket_filled.png")

    with open("ticket_filled.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved ticket_filled.xml")

except Exception as e:
    print("FAILED")
    print(e)

    driver.save_screenshot("ticket_filled_error.png")
    with open("ticket_filled_error.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

finally:
    driver.quit()