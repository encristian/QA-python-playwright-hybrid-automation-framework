from playwright.sync_api import Page

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