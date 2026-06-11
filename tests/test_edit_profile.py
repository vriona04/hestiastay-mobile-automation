import time
from pages.navigation_page import NavigationPage
from pages.edit_profile_page import EditProfilePage


def test_edit_profile_screen(driver):
    time.sleep(5)

    nav = NavigationPage(driver)
    edit_profile = EditProfilePage(driver)

    nav.go_profile()
    time.sleep(3)

    driver.find_element(
        "xpath",
        "//*[@content-desc='Edit Profile']"
    ).click()

    time.sleep(3)

    edit_profile.verify_edit_profile_screen()

    print("EDIT PROFILE SCREEN PASSED")