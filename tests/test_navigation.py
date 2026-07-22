from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_user_can_navigate_to_products_page(
    page: Page,
) -> None:
    """Verify navigation to the products page."""

    home_page = HomePage(page).open()
    products_page = ProductsPage(page)

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
) -> None:
    """Verify navigation to the signup and login page."""

    home_page = HomePage(page).open()
    login_page = LoginPage(page)

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
) -> None:
    """Verify navigation to the contact page."""

    home_page = HomePage(page).open()
    contact_page = ContactPage(page)

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
) -> None:
    """Verify navigation to an empty shopping cart."""

    home_page = HomePage(page).open()
    cart_page = CartPage(page)

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
    page: Page,
) -> None:
    """Verify that login fields accept user input."""

    login_page = LoginPage(page).open()

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