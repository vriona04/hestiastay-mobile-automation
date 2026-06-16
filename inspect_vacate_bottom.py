from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(3)

driver.execute_script(
    "mobile: scrollGesture",
    {
        "left": 100,
        "top": 900,
        "width": 900,
        "height": 1200,
        "direction": "down",
        "percent": 0.8
    }
)

time.sleep(2)

driver.save_screenshot("vacate_bottom.png")

with open("vacate_bottom.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved vacate_bottom.xml")

driver.quit()