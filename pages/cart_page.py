import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page object for the shopping cart page."""

    URL_PATTERN = re.compile(r"/view_cart/?$")

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.empty_cart_message = page.get_by_text(
            re.compile(
                "Cart is empty",
                re.IGNORECASE,
            )
        )