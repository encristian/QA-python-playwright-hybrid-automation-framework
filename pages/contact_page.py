import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class ContactPage(BasePage):
    """Page object for the contact page."""

    URL_PATTERN = re.compile(r"/contact_us/?$")

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.get_in_touch_heading = page.get_by_role(
            "heading",
            name=re.compile(
                "Get In Touch",
                re.IGNORECASE,
            ),
        )