import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page object for the products page."""

    URL_PATTERN = re.compile(r"/products/?$")

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.all_products_heading = page.get_by_role(
            "heading",
            name=re.compile(
                "All Products",
                re.IGNORECASE,
            ),
        )