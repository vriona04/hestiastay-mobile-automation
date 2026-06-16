from utils.driver_factory import get_driver
import time

driver = get_driver()

print("Navigate manually to Vacate -> New Request")
input("Press Enter when ready...")

driver.save_screenshot("before_submit_vacate.png")

with open("before_submit_vacate.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Now click Submit Vacating Request manually")
input("Press Enter AFTER submission...")

time.sleep(3)

driver.save_screenshot("after_submit_vacate.png")

with open("after_submit_vacate.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved after_submit_vacate.xml")

driver.quit()