import time
import pytest
from pages.navigation_page import NavigationPage


def test_food_menu(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    nav.go_home()
    time.sleep(2)

    search_terms = [
        "BREAKFAST",
        "LUNCH",
        "DINNER",
        "Today's Breakfast",
        "Today's Lunch",
        "Today's Dinner",
        "Menu Items",
        "No items available",
        "Updated by",
        "NOW",
        "UPCOMING",
    ]

    found = False

    for direction in ["up", "up", "down", "down", "down", "up"]:
        page = driver.page_source

        if any(term in page for term in search_terms):
            found = True
            break

        try:
            driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 100,
                    "top": 500,
                    "width": 900,
                    "height": 1300,
                    "direction": direction,
                    "percent": 0.9,
                },
            )
        except Exception:
            pass

        time.sleep(2)

    page = driver.page_source

    assert (
        found or any(term in page for term in search_terms)
    ), "Food menu card not visible"

    print("FOOD MENU PASSED")