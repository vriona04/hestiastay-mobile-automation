import time
import pytest
from pages.navigation_page import NavigationPage


@pytest.mark.auth
def test_logout(driver):

    time.sleep(5)
    nav = NavigationPage(driver)

    # Tap hamburger/menu icon
    driver.execute_script(
        "mobile: clickGesture",
        {"x": 65, "y": 115}
    )

    time.sleep(3)

    page = driver.page_source

    # If logout is not visible, try profile fallback
    if "Logout" not in page:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 900, "y": 2160}
        )
        time.sleep(2)

    # Tap logout menu item
    try:
        nav.click_a11y("Logout\nSign out of your account")
    except Exception:
        try:
            nav.click_a11y("Logout")
        except Exception:
            driver.execute_script(
                "mobile: clickGesture",
                {"x": 250, "y": 1980}
            )

    time.sleep(2)

    # Confirm logout popup
    try:
        nav.click_a11y("Logout")
    except Exception:
        driver.execute_script(
            "mobile: clickGesture",
            {"x": 750, "y": 1330}
        )

    time.sleep(5)

    page = driver.page_source

    assert (
        "Sign In" in page
        or "Login" in page
        or "Email" in page
        or "Password" in page
        or "Welcome Back" in page
    )

    print("LOGOUT PASSED")