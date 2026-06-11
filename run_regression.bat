@echo off

python -m pytest -v ^
tests/test_smoke.py ^
tests/test_navigation.py ^
tests/test_booking_details.py ^
tests/test_payment_history.py ^
tests/test_profile_details.py ^
tests/test_edit_profile.py ^
tests/test_emergency_contact.py ^
tests/test_rent_due.py ^
tests/test_hostel_details.py ^
tests/test_raise_ticket_e2e.py ^
tests/test_wifi_details.py ^
tests/test_food_menu.py ^
--html=reports\report.html --self-contained-html

pause