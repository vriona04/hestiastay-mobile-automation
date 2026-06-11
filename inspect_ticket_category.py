from utils.driver_factory import get_driver
from appium.webdriver.common.appiumby import AppiumBy
import time

driver = get_driver()

driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Select equipment category"
).click()

time.sleep(2)

with open("ticket_category.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved ticket_category.xml")

driver.quit()