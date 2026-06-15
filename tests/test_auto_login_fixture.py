def test_auto_login_fixture(logged_in_driver):
    page = logged_in_driver.page_source

    assert (
        "Welcome back" in page
        or "Bookings" in page
        or "Profile" in page
        or "Hestia" in page
    )

    print("AUTO LOGIN FIXTURE PASSED")