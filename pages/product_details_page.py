import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    """Page object for an individual product details page."""

    URL_PATTERN = re.compile(
        r"/product_details/\d+/?$"
    )

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.product_information = page.locator(
            ".product-information"
        )

        self.product_name = (
            self.product_information.locator("h2")
        )

        self.category = (
            self.product_information
            .locator("p")
            .filter(has_text="Category:")
            .first
        )

        self.price = (
            self.product_information
            .locator("span")
            .filter(
                has_text=re.compile(
                    r"Rs\.\s*\d+"
                )
            )
            .first
        )

        self.availability = (
            self.product_information
            .locator("p")
            .filter(has_text="Availability:")
            .first
        )

        self.condition = (
            self.product_information
            .locator("p")
            .filter(has_text="Condition:")
            .first
        )

        self.brand = (
            self.product_information
            .locator("p")
            .filter(has_text="Brand:")
            .first
        )