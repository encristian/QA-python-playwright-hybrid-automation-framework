import re
from typing import Dict

from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest

pytestmark = [
    pytest.mark.integration,
    pytest.mark.regression,
]

@pytest.mark.smoke
def test_user_created_by_api_can_login_through_ui(
    page: Page,
    home_page: HomePage,
    login_page: LoginPage,
    api_registered_user: Dict[str, str],
) -> None:
    """Verify that an API-created user can log in through the UI."""

    # Step 1: Open the UI login page
    login_page.open()

    expect(
        login_page.login_heading
    ).to_be_visible()

    expect(
        login_page.email_input
    ).to_be_editable()

    expect(
        login_page.password_input
    ).to_be_editable()

    # Step 2: Log in with the account created through API
    login_page.login(
        email=api_registered_user["email"],
        password=api_registered_user["password"],
    )

    # Step 3: Verify successful navigation
    expect(page).to_have_url(
        re.compile(
            r"https://(?:www\.)?"
            r"automationexercise\.com/?$"
        )
    )

    # Step 4: Verify the correct user is logged in
    expect(
        home_page.logged_in_as(
            api_registered_user["name"]
        )
    ).to_be_visible()

    # Step 5: Verify authenticated navigation options
    expect(
        home_page.logout_link
    ).to_be_visible()

    expect(
        home_page.delete_account_link
    ).to_be_visible()