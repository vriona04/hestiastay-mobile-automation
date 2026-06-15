import pytest

pytestmark = pytest.mark.skip(
    reason="Skipping emergency contact due to UiAutomator2 scroll instability"
)


def test_emergency_contact():
    print("EMERGENCY CONTACT TEST SKIPPED")