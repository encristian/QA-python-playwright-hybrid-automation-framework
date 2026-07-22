import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class HomePage(BasePage):
    """Page object for the Automation Exercise homepage."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.home_link = page.get_by_role(
            "link",
            name="Home",
        ).first

        self.products_link = page.get_by_role(
            "link",
            name="Products",
        ).first

        self.signup_login_link = page.get_by_role(
            "link",
            name="Signup / Login",
        ).first

        self.contact_us_link = page.get_by_role(
            "link",
            name=re.compile(
                "Contact us",
                re.IGNORECASE,
            ),
        ).first

        self.cart_link = page.get_by_role(
            "link",
            name="Cart",
        ).first

    def open(self) -> "HomePage":
        """Open the homepage."""

        self.open_path()

        return self

    def go_to_products(self) -> None:
        """Open the products page."""

        self.products_link.click()

    def go_to_signup_login(self) -> None:
        """Open the signup and login page."""

        self.signup_login_link.click()

    def go_to_contact_us(self) -> None:
        """Open the contact page."""

        self.contact_us_link.click()

    def go_to_cart(self) -> None:
        """Open the shopping cart."""

        self.cart_link.click()