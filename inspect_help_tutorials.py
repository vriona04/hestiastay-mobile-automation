from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(5)

# Open drawer/menu
driver.execute_script(
    "mobile: clickGesture",
    {"x": 65, "y": 115}
)

time.sleep(2)

driver.save_screenshot("drawer_before_help.png")

with open("drawer_before_help.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved drawer_before_help.xml")

# Click Help & Tutorials row by coordinate from drawer
driver.execute_script(
    "mobile: clickGesture",
    {"x": 350, "y": 1650}
)

time.sleep(3)

driver.save_screenshot("help_tutorials.png")

with open("help_tutorials.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved help_tutorials.xml")

driver.quit()