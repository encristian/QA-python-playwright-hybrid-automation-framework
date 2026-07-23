import re
from typing import Any, Dict

import pytest

from api.api_client import ApiClient
from api.endpoints import ApiEndpoints


def normalize_text(value: str) -> str:
    """Normalize text for case-insensitive search comparison."""

    return re.sub(
        pattern=r"[^a-z0-9]",
        repl="",
        string=value.lower(),
    )


@pytest.mark.parametrize(
    "search_term",
    [
        "top",
        "tshirt",
        "jean",
    ],
    ids=[
        "top",
        "tshirt",
        "jean",
    ],
)
def test_search_product_returns_matching_products(
    api_client: ApiClient,
    search_term: str,
) -> None:
    """Verify product search returns relevant products."""

    response = api_client.post(
        ApiEndpoints.SEARCH_PRODUCT,
        data={
            "search_product": search_term,
        },
    )

    assert response.status_code == 200, (
        "Expected HTTP status 200 for product search, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    payload = api_client.json_body(response)

    assert payload.get("responseCode") == 200, (
        "Expected responseCode 200, "
        f"but received {payload.get('responseCode')}. "
        f"Payload: {payload}"
    )

    assert "products" in payload, (
        "The response does not contain "
        "the 'products' field."
    )

    products = payload["products"]

    assert isinstance(products, list), (
        "Expected 'products' to be a list, "
        f"but received {type(products).__name__}."
    )

    assert products, (
        f"No products were returned for "
        f"search term: {search_term}"
    )

    required_fields = {
        "id",
        "name",
        "price",
        "brand",
        "category",
    }

    for product in products:
        assert isinstance(product, dict), (
            "Expected every product to be "
            f"a dictionary, but received: {product}"
        )

        missing_fields = (
            required_fields
            - product.keys()
        )

        assert not missing_fields, (
            f"Product is missing required fields: "
            f"{missing_fields}. "
            f"Product data: {product}"
        )

    normalized_search_term = normalize_text(
        search_term
    )

    matching_products = [
        product
        for product in products
        if normalized_search_term
        in normalize_text(product["name"])
    ]

    assert matching_products, (
        f"The API returned products, but none of "
        f"their names matched '{search_term}'. "
        f"Returned names: "
        f"{[product['name'] for product in products]}"
    )


def test_search_product_without_parameter_returns_bad_request(
    api_client: ApiClient,
) -> None:
    """Verify the error returned when search_product is missing."""

    response = api_client.post(
        ApiEndpoints.SEARCH_PRODUCT,
        data={},
    )

    assert response.status_code in {
        200,
        400,
    }, (
        "Expected HTTP status 200 or 400, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    payload: Dict[str, Any] = (
        api_client.json_body(response)
    )

    assert payload.get("responseCode") == 400, (
        "Expected responseCode 400, "
        f"but received {payload.get('responseCode')}. "
        f"Payload: {payload}"
    )

    assert payload.get("message") == (
        "Bad request, search_product parameter "
        "is missing in POST request."
    ), (
        "Unexpected error message. "
        f"Received: {payload.get('message')}"
    )