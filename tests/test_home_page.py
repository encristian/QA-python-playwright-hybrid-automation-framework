import re

from playwright.sync_api import Page, expect


BASE_URL = "https://automationexercise.com"


def test_home_page_is_displayed(page: Page) -> None:
    """Verify that the Automation Exercise homepage loads correctly."""

    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60_000,
    )

    expect(page).to_have_url(
        re.compile(r"automationexercise\.com/?$")
    )

    expect(
        page.get_by_role("link", name="Home").first
    ).to_be_visible()

    expect(
        page.get_by_role("link", name="Products").first
    ).to_be_visible()

    expect(
        page.get_by_role("link", name="Signup / Login").first
    ).to_be_visible()