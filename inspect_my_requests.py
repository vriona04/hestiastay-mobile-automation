from utils.driver_factory import get_driver

driver = get_driver()

driver.save_screenshot("my_requests.png")

with open("my_requests.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved my_requests.xml")

driver.quit()