# HestiaStay Mobile Automation Framework

## Overview

Mobile automation framework for the HestiaStay Android application built using:

* Python
* Appium
* Pytest
* Page Object Model (POM)

## Features

* Automated Android testing
* Real device execution
* USB and Wireless ADB support
* HTML reporting
* Screenshot capture on failures
* XML page source dumps for debugging
* Stable regression suite
* End-to-end workflow automation

## Automated Test Coverage

### Core Regression Suite

* Smoke Test
* Navigation Test
* Booking Details
* Payment History
* Profile Details
* Edit Profile
* Emergency Contact
* Rent Due
* Hostel Details
* Wi-Fi Details
* Food Menu

### End-to-End Business Flows

* Support Ticket Navigation
* Raise Ticket End-to-End

## Latest Regression Result

| Metric      | Result |
| ----------- | ------ |
| Total Tests | 12     |
| Passed      | 12     |
| Failed      | 0      |
| Skipped     | 0      |

Execution Time: ~3 Minutes

## Execute Regression Suite

```bash
.\run_regression.bat
```

## Reports

HTML reports are generated automatically in:

```text
reports/report.html
```

## Framework Structure

```text
hestiastay_automation/
│
├── pages/
│   ├── home_page.py
│   ├── navigation_page.py
│   ├── bookings_page.py
│   ├── profile_page.py
│   ├── rent_page.py
│   ├── wifi_page.py
│   └── raise_ticket_page.py
│
├── tests/
│   ├── test_smoke.py
│   ├── test_navigation.py
│   ├── test_booking_details.py
│   ├── test_payment_history.py
│   ├── test_profile_details.py
│   ├── test_edit_profile.py
│   ├── test_emergency_contact.py
│   ├── test_rent_due.py
│   ├── test_hostel_details.py
│   ├── test_wifi_details.py
│   ├── test_food_menu.py
│   └── test_raise_ticket_e2e.py
│
├── utils/
├── reports/
├── screenshots/
├── conftest.py
├── run_regression.bat
└── README.md
```

## Technology Stack

* Python 3.12
* Appium 3.5
* Pytest
* UiAutomator2
* Android Real Device Testing
* Git & GitHub

## Project Status

✅ Active Development

✅ Stable Regression Suite

✅ Real Device Automation

✅ HTML Reporting

✅ GitHub Version Control

## Repository

GitHub Repository:

https://github.com/vriona04/hestiastay-mobile-automation
