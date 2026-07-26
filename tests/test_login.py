import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


pytestmark = [
    pytest.mark.ui,
    pytest.mark.regression,
]

def test_login_with_invalid_credentials_shows_error(
    login_page: LoginPage,
    generated_user: dict[str, str],
) -> None:
    """Verify the error displayed for invalid credentials."""

    login_page.open()

    expect(
        login_page.login_heading
    ).to_be_visible()

    login_page.login(
        email=generated_user["email"],
        password=generated_user["password"],
    )

    expect(
        login_page.invalid_credentials_error
    ).to_be_visible()

    expect(
        login_page.invalid_credentials_error
    ).to_have_text(
        "Your email or password is incorrect!"
    )