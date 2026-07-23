import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class AccountDeletedPage(BasePage):
    """Page object displayed after account deletion."""

    URL_PATTERN = re.compile(
        r"/(?:delete_account|account_deleted)/?$"
    )

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.account_deleted_heading = (
            page.get_by_role(
                "heading",
                name=re.compile(
                    "Account Deleted",
                    re.IGNORECASE,
                ),
            )
        )

        self.continue_button = (
            page.get_by_role(
                "link",
                name="Continue",
            ).first
        )

    def continue_to_home_page(self) -> None:
        """Continue after deleting the account."""

        self.continue_button.click()