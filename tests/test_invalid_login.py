import os
import time
from pages.login_page import LoginPage


def test_invalid_login_wrong_password(driver):
    login = LoginPage(driver)

    email = os.getenv("HESTIA_EMAIL")
    assert email, "HESTIA_EMAIL environment variable not set"

    login.login(email, "WrongPassword@123")

    page = driver.page_source

    assert (
        "Welcome back" not in page
        and "Bookings" not in page
        and "Profile" not in page
    ), "User logged in with wrong password"

    print("INVALID LOGIN WRONG PASSWORD PASSED")


def test_invalid_login_empty_fields(driver):
    login = LoginPage(driver)

    login.login("", "")

    time.sleep(3)

    page = driver.page_source

    assert (
        "Welcome back" not in page
        and "Bookings" not in page
        and "Profile" not in page
    ), "User logged in with empty credentials"

    print("INVALID LOGIN EMPTY FIELDS PASSED")