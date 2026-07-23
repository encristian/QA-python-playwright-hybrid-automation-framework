import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class SignupPage(BasePage):
    """Page object for the full account registration form."""

    URL_PATTERN = re.compile(r"/signup/?$")

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.account_information_heading = (
            page.get_by_text(
                re.compile(
                    "Enter Account Information",
                    re.IGNORECASE,
                )
            ).first
        )

        # Title
        self.mr_title_radio = page.locator(
            "#id_gender1"
        )

        self.mrs_title_radio = page.locator(
            "#id_gender2"
        )

        # Account information
        self.name_input = page.locator(
            "#name"
        )

        self.email_input = page.locator(
            "#email"
        )

        self.password_input = page.locator(
            "#password"
        )

        self.day_select = page.locator(
            "#days"
        )

        self.month_select = page.locator(
            "#months"
        )

        self.year_select = page.locator(
            "#years"
        )

        self.newsletter_checkbox = page.locator(
            "#newsletter"
        )

        self.special_offers_checkbox = page.locator(
            "#optin"
        )

        # Address information
        self.first_name_input = page.locator(
            "#first_name"
        )

        self.last_name_input = page.locator(
            "#last_name"
        )

        self.company_input = page.locator(
            "#company"
        )

        self.address_input = page.locator(
            "#address1"
        )

        self.address2_input = page.locator(
            "#address2"
        )

        self.country_select = page.locator(
            "#country"
        )

        self.state_input = page.locator(
            "#state"
        )

        self.city_input = page.locator(
            "#city"
        )

        self.zipcode_input = page.locator(
            "#zipcode"
        )

        self.mobile_number_input = page.locator(
            "#mobile_number"
        )

        self.create_account_button = (
            page.get_by_role(
                "button",
                name="Create Account",
            )
        )

    def select_title(
        self,
        title: str,
    ) -> None:
        """Select the user's title."""

        title_options = {
            "Mr": self.mr_title_radio,
            "Mrs": self.mrs_title_radio,
        }

        if title not in title_options:
            raise ValueError(
                f"Unsupported title: {title}"
            )

        title_options[title].check()

    def fill_account_information(
        self,
        user: dict[str, str],
    ) -> None:
        """Fill the account information section."""

        self.select_title(
            user["title"]
        )

        self.password_input.fill(
            user["password"]
        )

        self.day_select.select_option(
            value=user["birth_day"]
        )

        self.month_select.select_option(
            value=user["birth_month"]
        )

        self.year_select.select_option(
            value=user["birth_year"]
        )

        self.newsletter_checkbox.check()
        self.special_offers_checkbox.check()

    def fill_address_information(
        self,
        user: dict[str, str],
    ) -> None:
        """Fill the address information section."""

        self.first_name_input.fill(
            user["first_name"]
        )

        self.last_name_input.fill(
            user["last_name"]
        )

        self.company_input.fill(
            user["company"]
        )

        self.address_input.fill(
            user["address"]
        )

        self.address2_input.fill(
            user["address2"]
        )

        self.country_select.select_option(
            label=user["country"]
        )

        self.state_input.fill(
            user["state"]
        )

        self.city_input.fill(
            user["city"]
        )

        self.zipcode_input.fill(
            user["zipcode"]
        )

        self.mobile_number_input.fill(
            user["mobile_number"]
        )

    def complete_registration_form(
        self,
        user: dict[str, str],
    ) -> None:
        """Fill all required registration information."""

        self.fill_account_information(user)
        self.fill_address_information(user)

    def submit_registration(self) -> None:
        """Create the user account."""

        self.create_account_button.click()