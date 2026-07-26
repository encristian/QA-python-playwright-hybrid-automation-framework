import re

import pytest
from playwright.sync_api import Page, expect

from pages.product_details_page import (
    ProductDetailsPage,
)
from pages.products_page import ProductsPage


pytestmark = [
    pytest.mark.ui,
    pytest.mark.regression,
]

@pytest.mark.parametrize(
    ("search_term", "expected_product"),
    [
        ("Blue Top", "Blue Top"),
        ("Winter Top", "Winter Top"),
    ],
    ids=[
        "blue-top",
        "winter-top",
    ],
)
def test_user_can_search_for_product(
    products_page: ProductsPage,
    search_term: str,
    expected_product: str,
) -> None:
    """Verify products can be found using search."""

    products_page.open()

    expect(
        products_page.all_products_heading
    ).to_be_visible()

    expect(
        products_page.search_input
    ).to_be_visible()

    expect(
        products_page.search_button
    ).to_be_enabled()

    products_page.search_for(search_term)

    expect(
        products_page.searched_products_heading
    ).to_be_visible()

    matching_product = (
        products_page.get_product_card(
            expected_product
        )
    )

    expect(
        matching_product
    ).to_be_visible()

    expect(
        matching_product
    ).to_contain_text(
        expected_product
    )


def test_user_can_open_first_product_details(
    page: Page,
    products_page: ProductsPage,
    product_details_page: ProductDetailsPage,
) -> None:
    """Verify the first product details are displayed."""

    products_page.open()

    expect(
        products_page.all_products_heading
    ).to_be_visible()

    expect(
        products_page.view_product_links.first
    ).to_be_visible()

    products_page.open_first_product()

    expect(page).to_have_url(
        product_details_page.URL_PATTERN
    )

    expect(
        product_details_page.product_information
    ).to_be_visible()

    expect(
        product_details_page.product_name
    ).to_have_text(
        re.compile(r"\S+")
    )

    expect(
        product_details_page.category
    ).to_contain_text(
        "Category:"
    )

    expect(
        product_details_page.price
    ).to_contain_text(
        "Rs."
    )

    expect(
        product_details_page.availability
    ).to_contain_text(
        "Availability:"
    )

    expect(
        product_details_page.condition
    ).to_contain_text(
        "Condition:"
    )

    expect(
        product_details_page.brand
    ).to_contain_text(
        "Brand:"
    )