import re

from playwright.sync_api import Locator, Page

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

        self.search_input = page.locator(
            "#search_product"
        )

        self.search_button = page.locator(
            "#submit_search"
        )

        self.searched_products_heading = (
            page.get_by_role(
                "heading",
                name=re.compile(
                    "Searched Products",
                    re.IGNORECASE,
                ),
            )
        )

        self.product_cards = page.locator(
            ".features_items "
            ".product-image-wrapper"
        )

        self.view_product_links = (
            page.get_by_role(
                "link",
                name="View Product",
            )
        )

    def open(self) -> "ProductsPage":
        """Open the products page."""

        self.open_path("/products")

        return self

    def search_for(
        self,
        product_name: str,
    ) -> None:
        """Search for a product by name."""

        self.search_input.fill(product_name)
        self.search_button.click()

    def get_product_card(
        self,
        product_name: str,
    ) -> Locator:
        """Return a product card matching the name."""

        return self.product_cards.filter(
            has_text=product_name
        ).first

    def open_first_product(self) -> None:
        """Open the details page of the first product."""

        self.view_product_links.first.click()