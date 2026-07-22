from playwright.sync_api import Page


class BasePage:
    """Base class shared by all page objects."""

    BASE_URL = "https://automationexercise.com"

    def __init__(self, page: Page) -> None:
        self.page = page

    def open_path(self, path: str = "") -> None:
        """Open a page using a path relative to the base URL."""

        self.page.goto(
            f"{self.BASE_URL}{path}",
            wait_until="domcontentloaded",
            timeout=60_000,
        )