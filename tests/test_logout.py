import time
from appium.webdriver.common.appiumby import AppiumBy


def test_logout(driver):

    time.sleep(5)

    page = driver.page_source

    # Open side/profile menu if Logout is not already visible
    if "Logout" not in page:
        try:
            driver.find_element(
                AppiumBy.XPATH,
                "//*[contains(@content-desc,'Profile')]"
            ).click()
            print("Profile menu clicked")
        except Exception:
            driver.execute_script(
                "mobile: clickGesture",
                {"x": 90, "y": 170}
            )
            print("Profile menu tapped by coordinates")

        time.sleep(3)
        page = driver.page_source

    assert "Logout" in page, "Logout option not visible"

    # Click Logout
    driver.find_element(
        AppiumBy.XPATH,
        "//*[contains(@content-desc,'Logout')]"
    ).click()

    time.sleep(3)

    # Save confirmation dialog XML
    with open(
        "screenshots/logout_confirmation.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(driver.page_source)

    print("Logout confirmation XML saved")

    # Stop here intentionally so we can inspect confirmation popup
    assert False, "Debug stop: inspect logout_confirmation.xml"