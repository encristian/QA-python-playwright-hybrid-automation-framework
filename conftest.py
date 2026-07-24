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
from typing import Dict, Generator
from api.api_client import ApiClient
from api.endpoints import ApiEndpoints
from api.user_payloads import (
    build_account_payload,
    build_credentials,
)



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

@pytest.fixture
def api_registered_user(
    api_client: ApiClient,
    generated_user: Dict[str, str],
) -> Generator[Dict[str, str], None, None]:
    """Create a user through API and delete it after the test."""

    account_data = build_account_payload(
        generated_user
    )

    credentials = build_credentials(
        generated_user
    )

    account_created = False

    try:
        create_response = api_client.post(
            ApiEndpoints.CREATE_ACCOUNT,
            data=account_data,
        )

        assert create_response.status_code in {
            200,
            201,
        }, (
            "Expected HTTP status 200 or 201 "
            "when creating the account, "
            f"but received "
            f"{create_response.status_code}. "
            f"Response: "
            f"{create_response.text[:300]}"
        )

        create_payload = api_client.json_body(
            create_response
        )

        create_response_code = int(
            create_payload.get(
                "responseCode",
                0,
            )
        )

        account_created = (
            create_response_code == 201
        )

        assert create_response_code == 201, (
            "Expected responseCode 201 "
            "when creating the user, "
            f"but received "
            f"{create_response_code}. "
            f"Payload: {create_payload}"
        )

        assert create_payload.get("message") == (
            "User created!"
        ), (
            "Unexpected account creation message. "
            f"Received: "
            f"{create_payload.get('message')}"
        )

        yield generated_user

    finally:
        if account_created:
            delete_response = api_client.delete(
                ApiEndpoints.DELETE_ACCOUNT,
                data=credentials,
            )

            assert delete_response.status_code in {
                200,
                204,
            }, (
                "Expected HTTP status 200 or 204 "
                "when deleting the account, "
                f"but received "
                f"{delete_response.status_code}. "
                f"Response: "
                f"{delete_response.text[:300]}"
            )

            delete_payload = api_client.json_body(
                delete_response
            )

            delete_response_code = int(
                delete_payload.get(
                    "responseCode",
                    0,
                )
            )

            assert delete_response_code == 200, (
                "Expected responseCode 200 "
                "when deleting the user, "
                f"but received "
                f"{delete_response_code}. "
                f"Payload: {delete_payload}"
            )

            assert delete_payload.get("message") == (
                "Account deleted!"
            ), (
                "Unexpected account deletion message. "
                f"Received: "
                f"{delete_payload.get('message')}"
            )