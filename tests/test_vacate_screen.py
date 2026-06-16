import time
import pytest


def test_vacate_screen(driver):
    time.sleep(5)

    # Open drawer manually before running this test if needed
    page = driver.page_source

    if "Vacate" not in page:
        pytest.skip("Drawer not open or Vacate option not visible")

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'Vacate')]"
    ).click()

    time.sleep(3)

    driver.find_element(
        "xpath",
        "//*[contains(@content-desc,'New Request')]"
    ).click()

    time.sleep(3)

    page = driver.page_source

    assert "Vacating Requests" in page
    assert "Create Vacating Request" in page
    assert "Vacate Date" in page
    assert "Preferred Checkout Time" in page
    assert "Reason for Vacating" in page
    assert "Select reason" in page

    print("VACATE SCREEN PASSED")