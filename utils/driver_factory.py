from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver():
    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    options.set_capability(
        "appPackage",
        "com.hostelrs.guest"
    )

    options.set_capability(
        "appActivity",
        "com.hostelrs.MainActivity"
    )

    options.set_capability(
        "noReset",
        True
    )

    options.set_capability(
        "newCommandTimeout",
        600
    )

    options.set_capability(
        "uiautomator2ServerLaunchTimeout",
        120000
    )

    options.set_capability(
        "adbExecTimeout",
        120000
    )

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    return driver