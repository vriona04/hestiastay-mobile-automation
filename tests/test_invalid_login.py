import os
import time
import pytest
from pages.login_page import LoginPage


@pytest.mark.auth
def test_invalid_login_wrong_password(driver):
    login = LoginPage(driver)

    email = os.getenv("HESTIA_EMAIL")
    assert email, "HESTIA_EMAIL environment variable not set"

    assert login.is_login_screen(), "App is not on login screen. Logout first."

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

    assert login.is_login_screen(), "App is not on login screen. Logout first."

    login.login("", "")

    time.sleep(3)

    page = driver.page_source

    assert (
        "Welcome back" not in page
        and "Bookings" not in page
        and "Profile" not in page
    ), "User logged in with empty credentials"

    print("INVALID LOGIN EMPTY FIELDS PASSED")