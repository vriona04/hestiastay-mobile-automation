import os
import pytest
from datetime import datetime
from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

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