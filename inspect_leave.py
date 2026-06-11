from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(3)

driver.save_screenshot("leave_screen.png")

with open("leave_screen.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved leave_screen.png")
print("Saved leave_screen.xml")

driver.quit()