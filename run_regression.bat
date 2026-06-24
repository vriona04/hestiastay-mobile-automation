@echo off

if not exist reports mkdir reports
if not exist screenshots mkdir screenshots

"C:\Program Files\Python312\python.exe" -m pytest -v -s ^
tests/test_auto_login_fixture.py ^
tests/test_booking_details.py ^
tests/test_food_menu.py ^
tests/test_support_tickets.py ^
tests/test_edit_profile.py ^
tests/test_leave_flow.py ^
tests/test_payment_details.py ^
tests/test_payment_history.py ^
tests/test_vacate_form_basic.py ^
tests/test_vacate_requests.py ^
--html=reports/final_regression.html ^
tests/test_vacate_form_basic.py ^
--self-contained-html

pause