import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    """Page object displayed after account creation."""

    URL_PATTERN = re.compile(
        r"/account_created/?$"
    )

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.account_created_heading = (
            page.get_by_role(
                "heading",
                name=re.compile(
                    "Account Created",
                    re.IGNORECASE,
                ),
            )
        )

        self.success_message = page.get_by_text(
            re.compile(
                (
                    "Your new account has been "
                    "successfully created"
                ),
                re.IGNORECASE,
            )
        )

        self.continue_button = (
            page.get_by_role(
                "link",
                name="Continue",
            ).first
        )

    def continue_to_home_page(self) -> None:
        """Continue to the homepage after registration."""

        self.continue_button.click()