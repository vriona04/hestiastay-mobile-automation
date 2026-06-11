from utils.driver_factory import get_driver
from pages.navigation_page import NavigationPage
import time

driver = get_driver()

try:
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_bookings()

    time.sleep(3)

    driver.save_screenshot("bookings_screen.png")

    with open("bookings_screen.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print("Saved bookings_screen.xml")

finally:
    driver.quit()s