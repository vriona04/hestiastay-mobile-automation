from pathlib import Path

stable_files = [
    "tests/test_smoke.py",
    "tests/test_edit_profile.py",
    "tests/test_profile_details.py",
    "tests/test_emergency_contact.py",
    "tests/test_food_menu.py",
    "tests/test_hostel_details.py",
    "tests/test_payment_history.py",
    "tests/test_rent_due.py",
    "tests/test_support_tickets.py",
    "tests/test_wifi_details.py",
]

for file in stable_files:
    path = Path(file)

    if not path.exists():
        print(f"Missing: {file}")
        continue

    text = path.read_text(encoding="utf-8")

    if "import pytest" not in text:
        lines = text.splitlines()
        insert_at = 0

        while insert_at < len(lines) and lines[insert_at].startswith("import "):
            insert_at += 1

        lines.insert(insert_at, "import pytest")
        text = "\n".join(lines) + "\n"

    if "@pytest.mark.stable" not in text:
        lines = text.splitlines()
        new_lines = []

        for line in lines:
            if line.startswith("def test_"):
                new_lines.append("@pytest.mark.stable")
            new_lines.append(line)

        text = "\n".join(new_lines) + "\n"

    path.write_text(text, encoding="utf-8")
    print(f"Updated: {file}")

print("Stable markers added")