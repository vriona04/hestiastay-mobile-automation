import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

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

def save_debug(name):
    driver.save_screenshot(f"{name}.png")

    with open(f"{name}.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print(f"Saved {name}.xml")

try:
    time.sleep(5)

    save_debug("ticket_start")

    # -------------------------
    # TITLE
    # -------------------------
    fields = driver.find_elements(
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    print("Fields found:", len(fields))

    fields[0].clear()
    fields[0].send_keys("WiFi Issue")

    print("Title entered")

    # -------------------------
    # CATEGORY
    # -------------------------
    driver.execute_script(
        "mobile: clickGesture",
        {
            "x": 540,
            "y": 1340
        }
    )

    time.sleep(2)

    driver.execute_script(
        "mobile: clickGesture",
        {
            "x": 550,
            "y": 815
        }
    )

    print("WiFi selected")

    time.sleep(2)

    # -------------------------
    # PRIORITY
    # -------------------------
    driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Medium"
    ).click()

    print("Medium priority selected")

    time.sleep(1)

    # -------------------------
    # DESCRIPTION
    # -------------------------
    driver.execute_script(
        "mobile: clickGesture",
        {
            "x": 540,
            "y": 1120
        }
    )

    time.sleep(1)

    driver.switch_to.active_element.send_keys(
        "WiFi is not working properly in my room."
    )

    print("Description entered")

    time.sleep(2)

    try:
        driver.hide_keyboard()
    except:
        pass

    time.sleep(1)

    save_debug("before_create_click")

    # -------------------------
    # SCROLL TO BUTTON
    # -------------------------
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

    # -------------------------
    # CREATE TICKET
    # -------------------------
    try:
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "Create Ticket"
        ).click()

        print("Create Ticket clicked by locator")

    except:

        driver.execute_script(
            "mobile: clickGesture",
            {
                "x": 540,
                "y": 2110
            }
        )

        print("Create Ticket clicked by coordinates")

    time.sleep(8)

    save_debug("after_create_click")

    page = driver.page_source

    if "Support Tickets" in page:
        print("PASS: Ticket created successfully")

    elif "Open" in page and "Created" in page:
        print("PASS: Ticket appears in ticket list")

    else:
        print("CHECK: Still on Create Ticket screen")

except Exception as e:

    print("FAILED")
    print(e)

    save_debug("ticket_submit_error")

finally:
    driver.quit()