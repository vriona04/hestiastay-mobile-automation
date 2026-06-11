from utils.driver_factory import get_driver
import time

driver = get_driver()

driver.execute_script(
    "mobile: scrollGesture",
    {
        "left": 100,
        "top": 500,
        "width": 800,
        "height": 1400,
        "direction": "down",
        "percent": 0.8
    }
)

time.sleep(2)

with open("ticket_bottom.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved ticket_bottom.xml")

driver.quit()