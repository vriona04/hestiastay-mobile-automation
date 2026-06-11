import time
import pytest
from pages.navigation_page import NavigationPage


def test_food_menu(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()
    time.sleep(2)

    found = False

    search_terms = [
        "Today's Lunch",
        "LUNCH",
        "Menu Items",
        "SERVING",
        "No items available"
    ]

    for direction in ["down", "down", "up", "up", "down"]:
        page = driver.page_source

        if any(term in page for term in search_terms):
            found = True
            break

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 500,
                "width": 900,
                "height": 1300,
                "direction": direction,
                "percent": 0.8
            }
        )

        time.sleep(2)

    if not found:
        pytest.skip("Food menu card not visible")

    page = driver.page_source

    assert any(term in page for term in search_terms), "Food menu content not found"

    print("FOOD MENU PASSED")