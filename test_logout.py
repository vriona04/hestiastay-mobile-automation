import time
from pages.navigation_page import NavigationPage


def test_logout(driver):

    time.sleep(5)

    nav = NavigationPage(driver)

    # Open drawer
    driver.execute_script(
        "mobile: clickGesture",
        {"x": 70, "y": 140}
    )

    time.sleep(2)

    # Click Logout
    nav.click_a11y(
        "Logout\nSign out of your account"
    )

    time.sleep(5)

    page = driver.page_source

    assert (
        "Sign In" in page
        or "Login" in page
        or "Email" in page
        or "Password" in page
    )

    print("LOGOUT PASSED")