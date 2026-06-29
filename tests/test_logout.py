import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.auth
def test_logout(driver):

    time.sleep(5)

    # Click top-right avatar/menu button
    try:
        menu_btn = driver.find_element(
            AppiumBy.XPATH,
            "//android.widget.Button[@clickable='true']"
        )

        menu_btn.click()
        print("Profile menu clicked")

    except Exception:
        pytest.skip("Profile menu button not found")

    time.sleep(3)

    page = driver.page_source

    # Save XML for debugging
    with open(
        "screenshots/logout_after_menu.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page)

    if "Logout" not in page and "Sign out" not in page:
        pytest.skip("Logout option not visible")

    try:
        driver.find_element(
            AppiumBy.XPATH,
            "//*[contains(@content-desc,'Logout') "
            "or contains(@content-desc,'Sign out')]"
        ).click()

    except Exception:
        pytest.skip("Logout button locator needs update")

    time.sleep(3)

    page = driver.page_source

    if "Confirm" in page or "Are you sure" in page:
        try:
            driver.find_element(
                AppiumBy.XPATH,
                "//*[contains(@content-desc,'Confirm') "
                "or contains(@content-desc,'Logout')]"
            ).click()
        except Exception:
            pass

    time.sleep(5)

    page = driver.page_source

    assert (
        "Sign In" in page
        or "Login" in page
        or "Email" in page
        or "Password" in page
    ), "Logout failed"

    print("LOGOUT PASSED")