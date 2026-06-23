import pytest


@pytest.mark.stable
def test_auto_login_fixture(logged_in_driver):
    page = logged_in_driver.page_source

    assert (
        "Welcome back" in page
        or "Hestia PG" in page
        or "Wi-Fi Details" in page
        or "Bookings" in page
        or "Profile" in page
        or "Home" in page
    ), "Auto login fixture did not open app dashboard"

    print("AUTO LOGIN FIXTURE PASSED")