from appium import webdriver
from appium.options.android import UiAutomator2Options

def get_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "RZCY8011AKW"
    options.app_package = "com.hostelrs.guest"
    options.app_activity = "com.hostelrs.MainActivity"
    options.no_reset = True

    return webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )