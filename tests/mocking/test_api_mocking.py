from typing import Any, Dict, List

from playwright.sync_api import (
    Page,
    Route,
    expect,
)

from mocks.product_responses import (
    MOCK_PRODUCTS_RESPONSE,
    MOCK_SERVER_ERROR_RESPONSE,
)
from pages.home_page import HomePage
from pages.products_page import ProductsPage


def fetch_products_from_browser(
    page: Page,
) -> Dict[str, Any]:
    """Request the products API from inside the browser."""

    return page.evaluate(
        """
        async () => {
            const response = await fetch(
                "/api/productsList"
            );

            const body = await response.json();

            return {
                status: response.status,
                body: body
            };
        }
        """
    )


def search_products_from_browser(
    page: Page,
    search_term: str,
) -> Dict[str, Any]:
    """Send a product search request from the browser."""

    return page.evaluate(
        """
        async (searchTerm) => {
            const formData = new URLSearchParams();

            formData.append(
                "search_product",
                searchTerm
            );

            const response = await fetch(
                "/api/searchProduct",
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                            "application/x-www-form-urlencoded"
                    },
                    body: formData.toString()
                }
            );

            const body = await response.json();

            return {
                status: response.status,
                body: body
            };
        }
        """,
        search_term,
    )


def test_browser_receives_mocked_products_response(
    page: Page,
    home_page: HomePage,
) -> None:
    """Verify the products API can be fully mocked."""

    def mock_products_api(
        route: Route,
    ) -> None:
        route.fulfill(
            status=200,
            json=MOCK_PRODUCTS_RESPONSE,
        )

    page.route(
        "**/api/productsList",
        mock_products_api,
    )

    home_page.open()

    result = fetch_products_from_browser(page)

    assert result["status"] == 200

    payload = result["body"]

    assert payload["responseCode"] == 200

    assert "products" in payload

    products = payload["products"]

    assert isinstance(products, list)

    assert len(products) == 2

    assert products[0]["id"] == 9001

    assert products[0]["name"] == (
        "Mocked Blue Hoodie"
    )

    assert products[1]["id"] == 9002

    assert products[1]["name"] == (
        "Mocked Black Jeans"
    )


def test_browser_handles_mocked_server_error(
    page: Page,
    home_page: HomePage,
) -> None:
    """Verify that a server error can be simulated."""

    def mock_server_error(
        route: Route,
    ) -> None:
        route.fulfill(
            status=500,
            json=MOCK_SERVER_ERROR_RESPONSE,
        )

    page.route(
        "**/api/productsList",
        mock_server_error,
    )

    home_page.open()

    result = fetch_products_from_browser(page)

    assert result["status"] == 500

    payload = result["body"]

    assert payload["responseCode"] == 500

    assert payload["message"] == (
        "Mocked internal server error."
    )


def test_search_mock_depends_on_request_data(
    page: Page,
    home_page: HomePage,
) -> None:
    """Return different mock data based on the search term."""

    received_search_terms: List[str] = []

    def mock_search_api(
        route: Route,
    ) -> None:
        submitted_data = (
            route.request.post_data_json
        )

        assert isinstance(
            submitted_data,
            dict,
        )

        search_term = submitted_data.get(
            "search_product",
            "",
        )

        received_search_terms.append(
            search_term
        )

        if search_term.lower() == "hoodie":
            products = [
                {
                    "id": 9001,
                    "name": "Mocked Blue Hoodie",
                    "price": "Rs. 1500",
                    "brand": "Mock Fashion",
                    "category": {
                        "usertype": {
                            "usertype": "Women",
                        },
                        "category": "Tops",
                    },
                }
            ]

        else:
            products = []

        route.fulfill(
            status=200,
            json={
                "responseCode": 200,
                "products": products,
            },
        )

    page.route(
        "**/api/searchProduct",
        mock_search_api,
    )

    home_page.open()

    result = search_products_from_browser(
        page=page,
        search_term="hoodie",
    )

    assert result["status"] == 200

    assert received_search_terms == [
        "hoodie"
    ]

    products = result["body"]["products"]

    assert len(products) == 1

    assert products[0]["name"] == (
        "Mocked Blue Hoodie"
    )


def test_products_page_loads_when_images_are_blocked(
    page: Page,
    products_page: ProductsPage,
) -> None:
    """Verify Products remains usable when images are blocked."""

    blocked_image_urls: List[str] = []

    def block_images(
        route: Route,
    ) -> None:
        if (
            route.request.resource_type
            == "image"
        ):
            blocked_image_urls.append(
                route.request.url
            )

            route.abort(
                error_code="blockedbyclient"
            )

        else:
            route.continue_()

    page.route(
        "**/*",
        block_images,
    )

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

    assert blocked_image_urls, (
        "No image requests were intercepted "
        "and blocked."
    )