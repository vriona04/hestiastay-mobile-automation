from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(3)

# Tap New Request tab
driver.find_element(
    "xpath",
    "//*[contains(@content-desc,'New Request')]"
).click()

time.sleep(3)

driver.save_screenshot("vacate_new_request.png")

with open("vacate_new_request.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved vacate_new_request.xml")

driver.quit()