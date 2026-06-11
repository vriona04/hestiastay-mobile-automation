from utils.driver_factory import get_driver
from pages.navigation_page import NavigationPage
import time

driver = get_driver()

try:
    time.sleep(5)

    nav = NavigationPage(driver)

    nav.go_leave()

    time.sleep(5)

    with open("leave_navigation.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved leave_navigation.xml")

finally:
    driver.quit()