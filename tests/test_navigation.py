import re

from playwright.sync_api import Page, expect


BASE_URL = "https://automationexercise.com"


def open_home_page(page: Page) -> None:
    """Open the Automation Exercise homepage."""

    page.goto(
        BASE_URL,
        wait_until="domcontentloaded",
        timeout=60_000,
    )


def test_user_can_navigate_to_products_page(
    page: Page,
) -> None:
    """Verify navigation from the homepage to the products page."""

    open_home_page(page)

    products_link = page.get_by_role(
        "link",
        name="Products",
    )

    expect(products_link).to_be_visible()

    products_link.click()

    expect(page).to_have_url(
        re.compile(r"/products/?$")
    )

    expect(
        page.get_by_role(
            "heading",
            name=re.compile(
                "All Products",
                re.IGNORECASE,
            ),
        )
    ).to_be_visible()


def test_user_can_navigate_to_signup_login_page(
    page: Page,
) -> None:
    """Verify navigation to the signup and login page."""

    open_home_page(page)

    signup_login_link = page.get_by_role(
    "link",
    name="Signup / Login",
)

    expect(signup_login_link).to_be_visible()

    signup_login_link.click()

    expect(page).to_have_url(
        re.compile(r"/login/?$")
    )

    expect(
        page.get_by_role(
            "heading",
            name=re.compile(
                "Login to your account",
                re.IGNORECASE,
            ),
        )
    ).to_be_visible()

    expect(
        page.get_by_role(
            "heading",
            name=re.compile(
                "New User Signup",
                re.IGNORECASE,
            ),
        )
    ).to_be_visible()


def test_user_can_navigate_to_contact_page(
    page: Page,
) -> None:
    """Verify navigation to the contact page."""

    open_home_page(page)

    contact_link = page.get_by_role(
        "link",
        name=re.compile(
            "Contact us",
            re.IGNORECASE,
        ),
    )

    expect(contact_link).to_be_visible()

    contact_link.click()

    expect(page).to_have_url(
        re.compile(r"/contact_us/?$")
    )

    expect(
        page.get_by_role(
            "heading",
            name=re.compile(
                "Get In Touch",
                re.IGNORECASE,
            ),
        )
    ).to_be_visible()


def test_user_can_navigate_to_empty_cart(
    page: Page,
) -> None:
    """Verify that a new user can open an empty cart."""

    open_home_page(page)

    cart_link = page.get_by_role(
        "link",
        name="Cart",
    )

    expect(cart_link).to_be_visible()

    cart_link.click()

    expect(page).to_have_url(
        re.compile(r"/view_cart/?$")
    )

    expect(
        page.get_by_text(
            re.compile(
                "Cart is empty",
                re.IGNORECASE,
            )
        )
    ).to_be_visible()


def test_login_form_accepts_user_input(
    page: Page,
) -> None:
    """Verify that the login fields accept user input."""

    page.goto(
        f"{BASE_URL}/login",
        wait_until="domcontentloaded",
        timeout=60_000,
    )

    login_section = page.locator(".login-form")

    email_input = login_section.get_by_placeholder(
        "Email Address"
    )

    password_input = login_section.get_by_placeholder(
        "Password"
    )

    login_button = login_section.get_by_role(
        "button",
        name="Login",
    )

    expect(email_input).to_be_visible()
    expect(email_input).to_be_editable()

    expect(password_input).to_be_visible()
    expect(password_input).to_be_editable()

    email_input.fill("qa.test@example.com")
    password_input.fill("incorrect-password")

    expect(email_input).to_have_value(
        "qa.test@example.com"
    )

    expect(password_input).to_have_value(
        "incorrect-password"
    )

    expect(login_button).to_be_visible()
    expect(login_button).to_be_enabled()