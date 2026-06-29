import os
import time
import pytest
from pages.login_page import LoginPage
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.auth
def test_invalid_login_wrong_password(driver):
    login = LoginPage(driver)

    email = os.getenv("HESTIA_EMAIL")
    assert email, "HESTIA_EMAIL environment variable not set"

    if not login.is_login_screen():
        pytest.skip("Already logged in")

    fields = driver.find_elements(
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    if len(fields) < 2:
        pytest.skip("Login fields not available")

    login.login(email, "WrongPassword@123")
    time.sleep(3)

    page = driver.page_source

    assert (
        "Welcome back" not in page
        and "Bookings" not in page
        and "Profile" not in page
    ), "User logged in with wrong password"

    print("INVALID LOGIN WRONG PASSWORD PASSED")


@pytest.mark.auth
def test_invalid_login_empty_fields(driver):
    login = LoginPage(driver)

    if not login.is_login_screen():
        pytest.skip("Already logged in")

    fields = driver.find_elements(
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    if len(fields) < 2:
        pytest.skip("Login fields not available")

    login.login("", "")
    time.sleep(3)

    page = driver.page_source

    assert (
        "Welcome back" not in page
        and "Bookings" not in page
        and "Profile" not in page
    ), "User logged in with empty credentials"

    print("INVALID LOGIN EMPTY FIELDS PASSED")