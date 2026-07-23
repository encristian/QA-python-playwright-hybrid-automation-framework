import re

from playwright.sync_api import Locator, Page

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

        self.logout_link = page.get_by_role(
            "link",
            name="Logout",
        ).first

        self.delete_account_link = (
            page.get_by_role(
                "link",
                name="Delete Account",
            ).first
        )

    def open(self) -> "HomePage":
        """Open the homepage."""

        self.open_path()

        return self

    def logged_in_as(
        self,
        user_name: str,
    ) -> Locator:
        """Return the logged-in user indicator."""

        return (
            self.page.locator("a")
            .filter(
                has_text=re.compile(
                    (
                        rf"Logged in as\s*"
                        rf"{re.escape(user_name)}"
                    ),
                    re.IGNORECASE,
                )
            )
            .first
        )

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

    def logout(self) -> None:
        """Log out the current user."""

        self.logout_link.click()

    def delete_account(self) -> None:
        """Delete the current user account."""

        self.delete_account_link.click()