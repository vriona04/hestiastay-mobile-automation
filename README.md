# HestiaStay Mobile Automation Framework

## Overview

A robust mobile automation framework for the HestiaStay Android application built using Python, Appium, and Pytest following the Page Object Model (POM) design pattern.

## Tech Stack

* Python 3.12
* Appium 3.5
* Pytest
* UiAutomator2
* Android Real Device Testing
* Git & GitHub

## Key Features

* Android mobile automation
* Real device execution
* USB and Wireless ADB support
* Page Object Model (POM) architecture
* Stable regression suite
* End-to-End business flow automation
* HTML reporting
* Screenshot capture on failures
* XML page source dumps for debugging
* Reusable utility components

## Test Coverage

### Core Regression Suite

* Smoke Test
* Navigation Test
* Booking Details
* Food Menu
* Rent Due
* Wi-Fi Details
* Hostel Details
* Payment History
* Profile Details
* Edit Profile
* Emergency Contact
* Support Tickets

### End-to-End Business Flows

* Leave Flow
* Raise Ticket Form
* Raise Ticket End-to-End
* Vacate Form
* Vacate Requests

## Latest Regression Results

| Metric      | Result |
| ----------- | ------ |
| Total Tests | 16+    |
| Passed      | 16     |
| Failed      | 0      |
| Skipped     | 0      |

Execution Time: ~5 Minutes

## Project Structure

```text
hestiastay_automation/
│
├── pages/
├── tests/
├── utils/
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run_regression.bat
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/vriona04/hestiastay-mobile-automation.git
cd hestiastay-mobile-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Appium server:

```bash
appium
```

Connect Android device and verify:

```bash
adb devices
```

## Execute Regression Suite

```bash
.\run_regression.bat
```

## Reports

HTML reports are automatically generated under:

```text
reports/
```

## Framework Highlights

* Page Object Model Architecture
* Reusable Navigation Framework
* Stable Regression Execution
* Real Device Testing
* Detailed HTML Reports
* Automatic Failure Evidence Collection

## Project Status

✅ Active Development

✅ Stable Regression Suite

✅ Real Device Automation

✅ HTML Reporting

✅ GitHub Version Control

## Repository

https://github.com/vriona04/hestiastay-mobile-automation
