import os
import pytest
from datetime import datetime

from utils.driver_factory import get_driver
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver():
    driver = get_driver()

    email = os.getenv("HESTIA_EMAIL")
    password = os.getenv("HESTIA_PASSWORD")

    assert email, "HESTIA_EMAIL environment variable not set"
    assert password, "HESTIA_PASSWORD environment variable not set"

    page = driver.page_source

    if (
        "Welcome back" in page
        or "Bookings" in page
        or "Profile" in page
        or "Hestia" in page
    ):
        pass

    elif LoginPage(driver).is_login_screen():
        login = LoginPage(driver)
        login.login(email, password)
        login.verify_dashboard()

    else:
        pytest.skip("App not on dashboard or login screen")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = (
            item.funcargs.get("driver")
            or item.funcargs.get("logged_in_driver")
        )

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            screenshot = f"screenshots/{item.name}_{timestamp}.png"
            xml_dump = f"screenshots/{item.name}_{timestamp}.xml"

            try:
                driver.save_screenshot(screenshot)

                with open(xml_dump, "w", encoding="utf-8") as f:
                    f.write(driver.page_source)

                print(f"\nSaved failure screenshot: {screenshot}")
                print(f"Saved XML dump: {xml_dump}")

            except Exception as e:
                print(f"\nCould not save failure artifacts: {e}")