from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(5)

driver.find_element(
    "xpath",
    "//*[@content-desc='History']"
).click()

time.sleep(3)

with open("history.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved history.xml")

driver.quit()