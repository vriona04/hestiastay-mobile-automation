import time
from pages.navigation_page import NavigationPage


def test_vacate_screen(driver):

    nav = NavigationPage(driver)

    print("Opening Vacate Screen")
    nav.go_vacate()

    time.sleep(5)

    page = driver.page_source

    with open(
        "screenshots/vacate_screen.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    print("Vacate screen XML saved")

    assert True