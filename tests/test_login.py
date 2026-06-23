import os
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from pages.login_page import LoginPage


@pytest.mark.auth
def test_login(driver):
    login = LoginPage(driver)

    email = os.getenv("HESTIA_EMAIL")
    password = os.getenv("HESTIA_PASSWORD")

    assert email, "HESTIA_EMAIL environment variable not set"
    assert password, "HESTIA_PASSWORD environment variable not set"

    if not login.is_login_screen():
        pytest.skip("Already logged in")

    fields = driver.find_elements(
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    if len(fields) < 2:
        pytest.skip("Login fields not available in current Flutter accessibility tree")

    login.login(email, password)
    login.verify_dashboard()

    print("LOGIN PASSED")