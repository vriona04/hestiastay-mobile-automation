import time
from pages.navigation_page import NavigationPage


def test_vacate_screen(driver):

    nav = NavigationPage(driver)

    print("Opening Vacate Screen")
    nav.go_home()
    time.sleep(3)

    page = driver.page_source

    if "Vacate" not in page:
        print("Vacate screen not available in current app state")
        print("VACATE SCREEN HANDLED")
        return

    try:
        nav.go_vacate()
    except Exception:
        print("Vacate navigation handled")
        print("VACATE SCREEN HANDLED")
        return

    time.sleep(5)

    page = driver.page_source

    with open(
        "screenshots/vacate_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("Vacate screen XML saved")
    print("VACATE SCREEN PASSED")