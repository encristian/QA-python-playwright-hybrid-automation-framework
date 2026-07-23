import pytest
from faker import Faker
from playwright.sync_api import Page

from pages.account_created_page import (
    AccountCreatedPage,
)
from pages.account_deleted_page import (
    AccountDeletedPage,
)
from pages.cart_page import CartPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_details_page import (
    ProductDetailsPage,
)
from pages.products_page import ProductsPage
from pages.signup_page import SignupPage

from typing import Generator
from api.api_client import ApiClient


@pytest.fixture(scope="session")
def fake() -> Faker:
    """Provide one Faker instance for the test session."""

    return Faker("en_US")


@pytest.fixture
def generated_user(
    fake: Faker,
) -> dict[str, str]:
    """Generate unique data for one test user."""

    first_name = fake.first_name()
    last_name = fake.last_name()

    mobile_number = (
        "07"
        + str(
            fake.random_number(
                digits=8,
                fix_len=True,
            )
        )
    )

    return {
        "title": "Mr",
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
        "birth_day": "15",
        "birth_month": "5",
        "birth_year": "1995",
        "company": fake.company(),
        "address": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": "United States",
        "state": fake.state(),
        "city": fake.city(),
        "zipcode": fake.postcode(),
        "mobile_number": mobile_number,
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
def product_details_page(
    page: Page,
) -> ProductDetailsPage:
    """Provide the product details page object."""

    return ProductDetailsPage(page)


@pytest.fixture
def login_page(
    page: Page,
) -> LoginPage:
    """Provide the login page object."""

    return LoginPage(page)


@pytest.fixture
def signup_page(
    page: Page,
) -> SignupPage:
    """Provide the full signup page object."""

    return SignupPage(page)


@pytest.fixture
def account_created_page(
    page: Page,
) -> AccountCreatedPage:
    """Provide the account created page object."""

    return AccountCreatedPage(page)


@pytest.fixture
def account_deleted_page(
    page: Page,
) -> AccountDeletedPage:
    """Provide the account deleted page object."""

    return AccountDeletedPage(page)


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

@pytest.fixture(scope="session")
def api_client(
) -> Generator[ApiClient, None, None]:
    """Provide one reusable API client per test session."""

    client = ApiClient()

    yield client

    client.close()