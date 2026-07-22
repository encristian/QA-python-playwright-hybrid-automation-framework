import pytest
from faker import Faker
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture(scope="session")
def fake() -> Faker:
    """Provide one Faker instance for the test session."""

    return Faker("en_US")


@pytest.fixture
def generated_user(
    fake: Faker,
) -> dict[str, str]:
    """Generate unique test data for one user."""

    first_name = fake.first_name()
    last_name = fake.last_name()

    return {
        "name": f"{first_name} {last_name}",
        "first_name": first_name,
        "last_name": last_name,
        "email": (
            f"qa.{fake.uuid4()}@example.com"
        ),
        "password": fake.password(
            length=14,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ),
    }


@pytest.fixture
def home_page(
    page: Page,
) -> HomePage:
    """Provide the homepage object."""

    return HomePage(page)


@pytest.fixture
def products_page(
    page: Page,
) -> ProductsPage:
    """Provide the products page object."""

    return ProductsPage(page)


@pytest.fixture
def login_page(
    page: Page,
) -> LoginPage:
    """Provide the login page object."""

    return LoginPage(page)


@pytest.fixture
def contact_page(
    page: Page,
) -> ContactPage:
    """Provide the contact page object."""

    return ContactPage(page)


@pytest.fixture
def cart_page(
    page: Page,
) -> CartPage:
    """Provide the cart page object."""

    return CartPage(page)