from utils.driver_factory import get_driver
import time

driver = get_driver()

print("App launched")

time.sleep(5)

driver.save_screenshot("logout_screen.png")

with open("logout_screen.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved logout_screen.xml")

time.sleep(5)

driver.quit()