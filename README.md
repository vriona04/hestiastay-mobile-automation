# HestiaStay Mobile Automation Framework

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Appium](https://img.shields.io/badge/Appium-3.5-green)
![Pytest](https://img.shields.io/badge/Pytest-Automation-orange)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)
![Platform](https://img.shields.io/badge/Platform-Android-success)

## Overview

A robust and scalable mobile automation framework for the HestiaStay Android application built using Python, Appium, and Pytest following the Page Object Model (POM) design pattern.

The framework supports real Android device execution, end-to-end business workflow automation, HTML reporting, failure evidence collection, and Jenkins CI/CD integration.

---

## Tech Stack

* Python 3.12
* Appium 3.5
* Pytest
* UiAutomator2
* Jenkins CI/CD
* Android Real Device Testing
* Git & GitHub

---

## Key Features

* Android mobile automation
* Real device execution
* USB and Wireless ADB support
* Page Object Model (POM) architecture
* Stable regression suite
* End-to-End business flow automation
* Jenkins Pipeline Integration
* HTML reporting
* Screenshot capture on failures
* XML page source dumps for debugging
* Reusable utility components
* Automatic artifact archiving

---

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

---

## Latest Regression Results

| Metric      | Result |
| ----------- | ------ |
| Total Tests | 16+    |
| Passed      | 16     |
| Failed      | 0      |
| Skipped     | 0      |

**Execution Time:** ~5 Minutes

---

## Framework Architecture

```text
hestiastay_automation/
│
├── pages/
│   ├── home_page.py
│   ├── navigation_page.py
│   ├── bookings_page.py
│   ├── profile_page.py
│   └── ...
│
├── tests/
│   ├── test_smoke.py
│   ├── test_booking_details.py
│   ├── test_food_menu.py
│   └── ...
│
├── utils/
│   ├── driver_factory.py
│   ├── base_page.py
│   └── logger.py
│
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Jenkinsfile
├── run_regression.bat
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/vriona04/hestiastay-mobile-automation.git

cd hestiastay-mobile-automation
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Appium Server

```bash
appium
```

### Verify Connected Device

```bash
adb devices
```

---

## Execute Regression Suite

```bash
python -m pytest -m stable \
--html=reports/report.html \
--self-contained-html
```

or

```bash
.\run_regression.bat
```

---

## Jenkins CI/CD Pipeline

The framework is integrated with Jenkins for Continuous Integration.

### Pipeline Workflow

```text
GitHub
   ↓
Jenkins Pipeline
   ↓
Prepare Android Device
   ↓
Execute Appium Tests
   ↓
Generate HTML Reports
   ↓
Archive Artifacts
```

### Jenkins Features

* Pipeline as Code using Jenkinsfile
* Automatic GitHub checkout
* Device preparation before execution
* HTML report publishing
* Screenshot artifact archiving
* Stable regression execution

---

## Reports

HTML reports are automatically generated under:

```text
reports/
```

Failure screenshots and XML dumps are stored under:

```text
screenshots/
```

---

## Framework Highlights

* Page Object Model Architecture
* Reusable Navigation Framework
* Stable Regression Execution
* Real Device Testing
* Jenkins CI/CD Integration
* Detailed HTML Reports
* Automatic Failure Evidence Collection
* GitHub Version Control

---

## Project Status

✅ Active Development

✅ Stable Regression Suite

✅ Real Device Automation

✅ Jenkins CI/CD Integrated

✅ HTML Reporting

✅ Artifact Archiving

✅ GitHub Version Control

---

## Repository

GitHub Repository:

https://github.com/vriona04/hestiastay-mobile-automation

Last CI/CD update: Jenkins pipeline auto-trigger configured.
