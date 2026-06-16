import time


def test_logout(driver):
    time.sleep(5)

    driver.execute_script(
        "mobile: clickGesture",
        {"x": 65, "y": 115}
    )

    time.sleep(2)

    driver.find_element(
        "xpath",
        "//*[@content-desc='Logout\nSign out of your account']"
    ).click()

    time.sleep(5)

    page = driver.page_source

    assert (
        "Sign in to your account" in page
        or "Sign In" in page
        or "Sign Up" in page
    ), "Login screen not shown after logout"

    print("LOGOUT PASSED")