from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(3)

# Tap reason dropdown
driver.find_element(
    "xpath",
    "//*[contains(@content-desc,'Select reason')]"
).click()

time.sleep(3)

driver.save_screenshot("vacate_reason.png")

with open("vacate_reason.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved vacate_reason.xml")

driver.quit()