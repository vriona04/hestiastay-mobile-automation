from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(3)

# Drawer is already open OR open it manually before running this script.
page = driver.page_source

if "Vacate" not in page:
    print("Vacate not visible. Open drawer manually first.")
    driver.save_screenshot("vacate_debug.png")

    with open("vacate_debug.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    driver.quit()
    exit()

driver.find_element(
    "xpath",
    "//*[contains(@content-desc,'Vacate')]"
).click()

time.sleep(3)

driver.save_screenshot("vacate.png")

with open("vacate.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved vacate.png")
print("Saved vacate.xml")

driver.quit()