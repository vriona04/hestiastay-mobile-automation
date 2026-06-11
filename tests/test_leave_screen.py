import time


def test_leave_screen(driver):
    time.sleep(5)

    page = driver.page_source

    assert "Set Leave Period" in page
    assert "Start Date" in page
    assert "End Date" in page or "Select return date" in page
    assert "Reason" in page
    assert "Vacation" in page
    assert "Going Home" in page
    assert "Medical" in page

    print("LEAVE SCREEN PASSED")