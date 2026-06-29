import time
from pages.navigation_page import NavigationPage


def test_navigation(driver):

    nav = NavigationPage(driver)

    # Verify Dashboard
    nav.go_home()
    time.sleep(2)

    page = driver.page_source

    assert (
        "Welcome back" in page
        or "Hestia PG" in page
        or "Wi-Fi Details" in page
        or "Need Help?" in page
        or "RENT OVERDUE" in page
        or "Going on Leave?" in page
    ), "Dashboard not found"

    print("Dashboard navigation verified")

    # Verify Bookings
    nav.go_bookings()
    time.sleep(3)

    page = driver.page_source

    assert (
        "My Bookings" in page
        or "Bookings" in page
        or "Approved" in page
        or "Call Hostel" in page
        or "SLN PG" in page
    ), "Bookings screen not found"

    print("Bookings navigation verified")

    # Return to Dashboard first
    try:
        driver.back()
        time.sleep(2)
    except Exception:
        pass

    nav.go_home()
    time.sleep(2)

    # Open Profile directly from Dashboard
    nav.go_profile()
    time.sleep(5)

    page = driver.page_source

    assert (
        "My Profile" in page
        or "Edit Profile" in page
        or "Email Address" in page
        or "Phone Number" in page
        or "Personal Information" in page
    ), "Profile screen not found"

    print("Profile navigation verified")
    print("NAVIGATION PASSED")