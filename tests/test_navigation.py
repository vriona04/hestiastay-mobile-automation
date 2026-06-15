from pages.navigation_page import NavigationPage
import time


def test_navigation(logged_in_driver):
    driver = logged_in_driver

    time.sleep(5)

    nav = NavigationPage(driver)

    nav.go_home()

    assert "Welcome back" in driver.page_source

    print("NAVIGATION PASSED")