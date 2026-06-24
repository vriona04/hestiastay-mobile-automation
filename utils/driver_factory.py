from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "Android"

    options.app_package = "com.hostelrs.guest"
    options.app_activity = "com.hostelrs.MainActivity"

    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("noReset", True)
    options.set_capability("fullReset", False)
    options.set_capability("dontStopAppOnReset", True)
    options.set_capability("autoGrantPermissions", True)

    # Stability settings
    options.set_capability("newCommandTimeout", 600)
    options.set_capability(
        "uiautomator2ServerLaunchTimeout",
        120000
    )
    options.set_capability(
        "uiautomator2ServerInstallTimeout",
        120000
    )
    options.set_capability(
        "adbExecTimeout",
        120000
    )
    options.set_capability(
        "androidInstallTimeout",
        120000
    )

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.implicitly_wait(10)

    return driver