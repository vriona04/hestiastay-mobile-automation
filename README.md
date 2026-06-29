# 🏠 HestiaStay Mobile Automation Framework




\

---

## 📌 Overview

A robust and scalable mobile automation framework for the **HestiaStay Android application** built using **Python, Appium, and Pytest** following the **Page Object Model (POM)** design pattern.

The framework supports:

* Real Android device execution
* End-to-End business workflow automation
* Stable regression execution
* HTML reporting
* Failure evidence collection
* Jenkins CI/CD integration

---

## 🚀 Tech Stack

* Python 3.12
* Appium 3.5
* Pytest
* UiAutomator2
* Jenkins CI/CD
* Android Real Device Testing
* Git & GitHub

---

## ⭐ Key Features

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

## 🧪 Test Coverage

### Authentication

* Login
* Invalid Login
* Logout

### Dashboard

* Auto Login Validation
* Smoke Test
* Navigation Test
* Food Menu
* Wi-Fi Details
* Hostel Details
* Rent Due

### Profile

* Profile Details
* Edit Profile
* Emergency Contact

### Booking

* Booking Details

### Leave Module

* Leave Screen
* Leave Flow
* Leave Request End-to-End
* Leave Return

### Payment Module

* Payment Details
* Payment History
* Rent Due Validation

### Support Module

* Support Tickets
* Raise Ticket Form
* Raise Ticket End-to-End

### Vacate Module

* Vacate Screen
* Vacate Form
* Vacate Requests

---

## 📊 Latest Regression Results

| Metric                  | Result |
| ----------------------- | ------ |
| Total Automated Tests   | 26     |
| Stable Regression Tests | 24     |
| Passed                  | 24     |
| Failed                  | 0      |
| Skipped                 | 0      |

**Execution Time:** ~15 Minutes

---

## 🏗 Framework Architecture

```text
hestiastay_automation/
│
├── pages/
│   ├── home_page.py
│   ├── navigation_page.py
│   ├── bookings_page.py
│   ├── profile_page.py
│   ├── leave_page.py
│   └── ...
│
├── tests/
│   ├── test_smoke.py
│   ├── test_booking_details.py
│   ├── test_leave_flow.py
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

## 📂 Project Structure

### pages/

Contains all Page Object classes.

Examples:

* HomePage
* NavigationPage
* BookingsPage
* ProfilePage
* LeavePage
* RaiseTicketPage

Responsibilities:

* UI interactions
* Element locators
* Screen-level actions

---

### tests/

Contains all automated test scenarios.

Examples:

* test_smoke.py
* test_booking_details.py
* test_leave_flow.py
* test_payment_details.py

Responsibilities:

* Functional testing
* Regression testing
* End-to-End testing

---

### utils/

Contains reusable framework utilities.

Examples:

* Driver Factory
* Base Page
* Common Utilities
* Wait Methods

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/vriona04/hestiastay-mobile-automation.git

cd hestiastay-mobile-automation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📱 Device Setup

Connect Android device:

```bash
adb devices
```

Start Appium Server:

```bash
appium
```

Verify connected devices:

```bash
adb devices
```

---

## ▶️ Running Tests

### Run Single Test

```bash
python -m pytest -v -s tests/test_booking_details.py
```

### Run Full Regression

```bash
.\run_regression.bat
```

### Generate HTML Report

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

---

## 📄 Sample Regression Command

```bash
python -m pytest -v -s tests/ ^
--html=reports/final_regression.html ^
--self-contained-html
```

---

## 🔄 Jenkins CI/CD Pipeline

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

## 📊 Reports

HTML reports are automatically generated under:

```text
reports/
```

Failure screenshots and XML dumps are stored under:

```text
screenshots/
```

---

## 🌟 Framework Highlights

✅ Page Object Model Architecture

✅ Reusable Navigation Framework

✅ Stable Regression Execution

✅ Real Device Testing

✅ Jenkins CI/CD Integration

✅ Detailed HTML Reports

✅ Automatic Failure Evidence Collection

✅ GitHub Version Control

---

## 📈 Project Status

✅ Active Development

✅ Stable Regression Suite

✅ Real Device Automation

✅ Jenkins CI/CD Integrated

✅ HTML Reporting

✅ Artifact Archiving

✅ GitHub Version Control

---

## 🔗 Repository

GitHub Repository:

https://github.com/vriona04/hestiastay-mobile-automation

---

## 👨‍💻 Author

**Mounika**

Automation Test Engineer

---

## 📄 License

This project is developed for **HestiaStay internal quality assurance and automation purposes**.
