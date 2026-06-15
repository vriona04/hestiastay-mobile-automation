import os
from pages.login_page import LoginPage


def test_login(driver):
    login = LoginPage(driver)

    email = os.getenv("HESTIA_EMAIL")
    password = os.getenv("HESTIA_PASSWORD")

    assert email, "HESTIA_EMAIL environment variable not set"
    assert password, "HESTIA_PASSWORD environment variable not set"

    login.login(email, password)
    login.verify_dashboard()

    print("LOGIN PASSED")