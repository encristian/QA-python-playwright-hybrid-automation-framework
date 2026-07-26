import pytest
from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


pytestmark = [
    pytest.mark.ui,
    pytest.mark.regression,
]

def test_user_can_navigate_to_products_page(
    page: Page,
    home_page: HomePage,
    products_page: ProductsPage,
) -> None:
    """Verify navigation to the products page."""

    home_page.open()

    expect(
        home_page.products_link
    ).to_be_visible()

    home_page.go_to_products()

    expect(page).to_have_url(
        products_page.URL_PATTERN
    )

    expect(
        products_page.all_products_heading
    ).to_be_visible()


def test_user_can_navigate_to_signup_login_page(
    page: Page,
    home_page: HomePage,
    login_page: LoginPage,
) -> None:
    """Verify navigation to the signup and login page."""

    home_page.open()

    expect(
        home_page.signup_login_link
    ).to_be_visible()

    home_page.go_to_signup_login()

    expect(page).to_have_url(
        login_page.URL_PATTERN
    )

    expect(
        login_page.login_heading
    ).to_be_visible()

    expect(
        login_page.signup_heading
    ).to_be_visible()


def test_user_can_navigate_to_contact_page(
    page: Page,
    home_page: HomePage,
    contact_page: ContactPage,
) -> None:
    """Verify navigation to the contact page."""

    home_page.open()

    expect(
        home_page.contact_us_link
    ).to_be_visible()

    home_page.go_to_contact_us()

    expect(page).to_have_url(
        contact_page.URL_PATTERN
    )

    expect(
        contact_page.get_in_touch_heading
    ).to_be_visible()


def test_user_can_navigate_to_empty_cart(
    page: Page,
    home_page: HomePage,
    cart_page: CartPage,
) -> None:
    """Verify navigation to an empty shopping cart."""

    home_page.open()

    expect(
        home_page.cart_link
    ).to_be_visible()

    home_page.go_to_cart()

    expect(page).to_have_url(
        cart_page.URL_PATTERN
    )

    expect(
        cart_page.empty_cart_message
    ).to_be_visible()


def test_login_form_accepts_user_input(
    login_page: LoginPage,
) -> None:
    """Verify that login fields accept user input."""

    login_page.open()

    expect(
        login_page.email_input
    ).to_be_visible()

    expect(
        login_page.email_input
    ).to_be_editable()

    expect(
        login_page.password_input
    ).to_be_visible()

    expect(
        login_page.password_input
    ).to_be_editable()

    login_page.fill_login_form(
        email="qa.test@example.com",
        password="incorrect-password",
    )

    expect(
        login_page.email_input
    ).to_have_value(
        "qa.test@example.com"
    )

    expect(
        login_page.password_input
    ).to_have_value(
        "incorrect-password"
    )

    expect(
        login_page.login_button
    ).to_be_visible()

    expect(
        login_page.login_button
    ).to_be_enabled()


def test_signup_form_accepts_generated_user_data(
    login_page: LoginPage,
    generated_user: dict[str, str],
) -> None:
    """Verify signup fields using generated test data."""

    login_page.open()

    expect(
        login_page.signup_name_input
    ).to_be_visible()

    expect(
        login_page.signup_email_input
    ).to_be_visible()

    login_page.fill_signup_form(
        name=generated_user["name"],
        email=generated_user["email"],
    )

    expect(
        login_page.signup_name_input
    ).to_have_value(
        generated_user["name"]
    )

    expect(
        login_page.signup_email_input
    ).to_have_value(
        generated_user["email"]
    )

    expect(
        login_page.signup_button
    ).to_be_visible()

    expect(
        login_page.signup_button
    ).to_be_enabled()