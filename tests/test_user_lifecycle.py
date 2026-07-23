import re

from playwright.sync_api import Page, expect

from pages.account_created_page import (
    AccountCreatedPage,
)
from pages.account_deleted_page import (
    AccountDeletedPage,
)
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage


def test_user_can_register_login_and_delete_account(
    page: Page,
    home_page: HomePage,
    login_page: LoginPage,
    signup_page: SignupPage,
    account_created_page: AccountCreatedPage,
    account_deleted_page: AccountDeletedPage,
    generated_user: dict[str, str],
) -> None:
    """Verify the complete lifecycle of a user account."""

    # Step 1: Open the signup and login page
    login_page.open()

    expect(
        login_page.signup_heading
    ).to_be_visible()

    # Step 2: Complete the initial signup form
    login_page.fill_signup_form(
        name=generated_user["name"],
        email=generated_user["email"],
    )

    login_page.submit_signup()

    # Step 3: Verify navigation to the full signup form
    expect(page).to_have_url(
        signup_page.URL_PATTERN
    )

    expect(
        signup_page.account_information_heading
    ).to_be_visible()

    # Step 4: Verify prefilled name and email
    expect(
        signup_page.name_input
    ).to_have_value(
        generated_user["name"]
    )

    expect(
        signup_page.email_input
    ).to_have_value(
        generated_user["email"]
    )

    # Step 5: Complete and submit registration
    signup_page.complete_registration_form(
        generated_user
    )

    signup_page.submit_registration()

    # Step 6: Verify successful account creation
    expect(page).to_have_url(
        account_created_page.URL_PATTERN
    )

    expect(
        account_created_page.account_created_heading
    ).to_be_visible()

    expect(
        account_created_page.success_message
    ).to_be_visible()

    # Step 7: Continue to the homepage
    account_created_page.continue_to_home_page()

    expect(
        home_page.logged_in_as(
            generated_user["name"]
        )
    ).to_be_visible()

    # Step 8: Log out
    expect(
        home_page.logout_link
    ).to_be_visible()

    home_page.logout()

    expect(page).to_have_url(
        login_page.URL_PATTERN
    )

    expect(
        login_page.login_heading
    ).to_be_visible()

    # Step 9: Log in again with the created account
    login_page.login(
        email=generated_user["email"],
        password=generated_user["password"],
    )

    expect(
        home_page.logged_in_as(
            generated_user["name"]
        )
    ).to_be_visible()

    # Step 10: Delete the account
    expect(
        home_page.delete_account_link
    ).to_be_visible()

    home_page.delete_account()

    expect(
        account_deleted_page.account_deleted_heading
    ).to_be_visible()

    # Step 11: Continue after account deletion
    account_deleted_page.continue_to_home_page()

    expect(page).to_have_url(
        re.compile(
            r"automationexercise\.com/?$"
        )
    )