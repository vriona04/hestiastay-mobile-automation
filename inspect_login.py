from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(5)

driver.save_screenshot("login_screen.png")

with open("login_screen.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print(driver.page_source[:8000])

time.sleep(5)
driver.quit()