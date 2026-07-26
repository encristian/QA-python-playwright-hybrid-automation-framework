from playwright.sync_api import (
    Page,
    TimeoutError as PlaywrightTimeoutError,
)

from utils.config import BASE_URL, DEFAULT_TIMEOUT


class BasePage:
    """Base class shared by all page objects."""

    def __init__(self, page: Page) -> None:
        self.page = page

    def open_path(self, path: str = "") -> None:
        """Open a path relative to the configured base URL."""

        normalized_path = (
            f"/{path.lstrip('/')}"
            if path
            else ""
        )

        self.page.goto(
            f"{BASE_URL}{normalized_path}",
            wait_until="domcontentloaded",
            timeout=DEFAULT_TIMEOUT,
        )

        self.dismiss_cookie_consent()

    def dismiss_cookie_consent(self) -> None:
        """Accept the cookie consent popup when it is displayed."""

        consent_button = self.page.locator(
            "button.fc-cta-consent"
        ).first

        try:
            consent_button.wait_for(
                state="visible",
                timeout=3000,
            )

            consent_button.click()

            self.page.locator(
                ".fc-dialog-overlay"
            ).wait_for(
                state="hidden",
                timeout=5000,
            )

        except PlaywrightTimeoutError:
            # The popup did not appear, so the test continues normally.
            pass