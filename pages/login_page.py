import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the signup and login page."""

    URL_PATTERN = re.compile(r"/login/?$")

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.login_heading = page.get_by_role(
            "heading",
            name=re.compile(
                "Login to your account",
                re.IGNORECASE,
            ),
        )

        self.signup_heading = page.get_by_role(
            "heading",
            name=re.compile(
                "New User Signup",
                re.IGNORECASE,
            ),
        )

        self.login_section = page.locator(
            ".login-form"
        )

        self.email_input = (
            self.login_section.get_by_placeholder(
                "Email Address"
            )
        )

        self.password_input = (
            self.login_section.get_by_placeholder(
                "Password"
            )
        )

        self.login_button = (
            self.login_section.get_by_role(
                "button",
                name="Login",
            )
        )

        self.signup_section = page.locator(
            ".signup-form"
        )

        self.signup_name_input = (
            self.signup_section.get_by_placeholder(
                "Name"
            )
        )

        self.signup_email_input = (
            self.signup_section.get_by_placeholder(
                "Email Address"
            )
        )

        self.signup_button = (
            self.signup_section.get_by_role(
                "button",
                name="Signup",
            )
        )

    def open(self) -> "LoginPage":
        """Open the signup and login page."""

        self.open_path("/login")

        return self

    def fill_login_form(
        self,
        email: str,
        password: str,
    ) -> None:
        """Fill the login form without submitting it."""

        self.email_input.fill(email)
        self.password_input.fill(password)

    def submit_login(self) -> None:
        """Submit the login form."""

        self.login_button.click()

    def fill_signup_form(
        self,
        name: str,
        email: str,
    ) -> None:
        """Fill the initial signup form."""

        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)

    def submit_signup(self) -> None:
        """Submit the initial signup form."""

        self.signup_button.click()