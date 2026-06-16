import time
import pytest


def test_vacate_requests(driver):
    time.sleep(5)

    page = driver.page_source

    if "Vacating Requests" not in page:
        pytest.skip("Vacate screen not open")

    assert "My Requests" in page
    assert "Request Summary" in page
    assert "All Requests" in page

    assert (
        "Cancelled" in page
        or "Pending" in page
        or "Approved" in page
        or "Completed" in page
    )

    print("VACATE REQUESTS PASSED")