from utils.driver_factory import get_driver
import time

driver = get_driver()

time.sleep(5)

# tap top-left menu / hamburger area
driver.execute_script(
    "mobile: clickGesture",
    {"x": 70, "y": 140}
)

time.sleep(2)

driver.save_screenshot("drawer.png")

with open("drawer.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved drawer.png")
print("Saved drawer.xml")

driver.quit()