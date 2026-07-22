import re

from playwright.sync_api import Page, expect

from pages.home_page import HomePage


def test_home_page_is_displayed(page: Page) -> None:
    """Verify that the homepage loads correctly."""

    home_page = HomePage(page).open()

    expect(page).to_have_url(
        re.compile(r"automationexercise\.com/?$")
    )

    expect(
        home_page.home_link
    ).to_be_visible()

    expect(
        home_page.products_link
    ).to_be_visible()

    expect(
        home_page.signup_login_link
    ).to_be_visible()