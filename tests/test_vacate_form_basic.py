import time
from appium.webdriver.common.appiumby import AppiumBy


def test_vacate_form_basic(driver):
    time.sleep(5)

    page = driver.page_source

    assert "Vacating Requests" in page
    assert "New Request" in page
    assert "Submit Vacating Request" in page

    fields = driver.find_elements(
        AppiumBy.CLASS_NAME,
        "android.widget.EditText"
    )

    fields[-1].clear()
    fields[-1].send_keys("Automation test vacate request note.")

    time.sleep(1)

    page = driver.page_source

    assert "Submit Vacating Request" in page

    print("VACATE FORM BASIC PASSED")