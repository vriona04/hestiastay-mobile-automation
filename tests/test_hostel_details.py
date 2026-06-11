import time
from pages.navigation_page import NavigationPage
from pages.hostel_page import HostelPage


def test_hostel_details(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    hostel = HostelPage(driver)

    nav.go_home()
    time.sleep(2)

    # Try to move dashboard to useful home content
    for _ in range(2):
        page = driver.page_source

        if (
            "Your Hostel" in page
            or "Hestia PG" in page
            or "Room 105" in page
            or "RENT OVERDUE" in page
            or "Need Help?" in page
        ):
            break

        driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 100,
                "top": 600,
                "width": 900,
                "height": 1200,
                "direction": "up",
                "percent": 0.6
            }
        )

        time.sleep(2)

    hostel.verify_hostel_details()

    print("HOSTEL DETAILS PASSED")