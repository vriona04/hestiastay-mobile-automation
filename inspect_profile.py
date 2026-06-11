import time
from utils.driver_factory import get_driver
from pages.navigation_page import NavigationPage

driver = get_driver()

try:
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_profile()

    time.sleep(3)

    driver.save_screenshot("profile.png")

    with open("profile.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved profile.png")
    print("Saved profile.xml")

finally:
    driver.quit()