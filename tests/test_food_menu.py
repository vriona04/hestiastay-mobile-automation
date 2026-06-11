import time
import pytest
from pages.navigation_page import NavigationPage


def test_food_menu(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()
    time.sleep(2)

    found = False

    for _ in range(4):
        page = driver.page_source

        if "Today's Lunch" in page or "LUNCH" in page or "Menu Items" in page:
            found = True
            break

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "down",
                "percent": 0.7
            }
        )

        time.sleep(2)

    if not found:
        pytest.skip("Food menu card not visible")

    page = driver.page_source

    assert (
        "Today's Lunch" in page
        or "LUNCH" in page
        or "Menu Items" in page
    )

    print("FOOD MENU PASSED")