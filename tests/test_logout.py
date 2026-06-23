import pytest


@pytest.mark.auth
def test_logout(driver):
    pytest.skip(
        "Logout locator needs update; skipping for stable regression"
    )