from utils.driver_factory import get_driver

driver = get_driver()

with open("leave_form.xml", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("Saved leave_form.xml")

driver.quit()