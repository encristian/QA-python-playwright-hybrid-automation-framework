from typing import Any, Dict

import pytest

from api.api_client import ApiClient
from api.endpoints import ApiEndpoints


@pytest.fixture(scope="module")
def products_payload(
    api_client: ApiClient,
) -> Dict[str, Any]:
    """Fetch the products response once for this module."""

    response = api_client.get(
        ApiEndpoints.PRODUCTS_LIST
    )

    assert response.status_code == 200, (
        "Expected HTTP status 200 for products, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    return api_client.json_body(response)


@pytest.fixture(scope="module")
def brands_payload(
    api_client: ApiClient,
) -> Dict[str, Any]:
    """Fetch the brands response once for this module."""

    response = api_client.get(
        ApiEndpoints.BRANDS_LIST
    )

    assert response.status_code == 200, (
        "Expected HTTP status 200 for brands, "
        f"but received {response.status_code}. "
        f"Response: {response.text[:300]}"
    )

    return api_client.json_body(response)


def test_get_all_products_returns_non_empty_list(
    products_payload: Dict[str, Any],
) -> None:
    """Verify the products API returns a product list."""

    assert products_payload[
        "responseCode"
    ] == 200

    assert "products" in products_payload

    products = products_payload["products"]

    assert isinstance(products, list)

    assert len(products) > 0


def test_each_product_has_required_structure(
    products_payload: Dict[str, Any],
) -> None:
    """Verify every product contains required fields."""

    required_product_fields = {
        "id",
        "name",
        "price",
        "brand",
        "category",
    }

    products = products_payload["products"]

    for product in products:
        assert isinstance(product, dict)

        missing_fields = (
            required_product_fields
            - product.keys()
        )

        assert not missing_fields, (
            f"Product is missing fields: "
            f"{missing_fields}. "
            f"Product data: {product}"
        )

        assert isinstance(
            product["id"],
            int,
        )

        assert isinstance(
            product["name"],
            str,
        )

        assert product["name"].strip()

        assert isinstance(
            product["price"],
            str,
        )

        assert product["price"].startswith(
            "Rs."
        )

        assert isinstance(
            product["brand"],
            str,
        )

        assert product["brand"].strip()

        category = product["category"]

        assert isinstance(category, dict)

        assert "category" in category
        assert "usertype" in category

        assert isinstance(
            category["category"],
            str,
        )

        assert isinstance(
            category["usertype"],
            dict,
        )

        assert "usertype" in (
            category["usertype"]
        )


@pytest.mark.parametrize(
    "product_name",
    [
        "Blue Top",
        "Winter Top",
    ],
    ids=[
        "blue-top",
        "winter-top",
    ],
)
def test_known_product_exists_in_api_response(
    products_payload: Dict[str, Any],
    product_name: str,
) -> None:
    """Verify known products exist in the API response."""

    product_names = {
        product["name"]
        for product
        in products_payload["products"]
    }

    assert product_name in product_names


def test_get_all_brands_returns_non_empty_list(
    brands_payload: Dict[str, Any],
) -> None:
    """Verify the brands API returns a brand list."""

    assert brands_payload[
        "responseCode"
    ] == 200

    assert "brands" in brands_payload

    brands = brands_payload["brands"]

    assert isinstance(brands, list)

    assert len(brands) > 0


def test_each_brand_has_required_structure(
    brands_payload: Dict[str, Any],
) -> None:
    """Verify every brand contains required fields."""

    required_brand_fields = {
        "id",
        "brand",
    }

    brands = brands_payload["brands"]

    for brand in brands:
        assert isinstance(brand, dict)

        missing_fields = (
            required_brand_fields
            - brand.keys()
        )

        assert not missing_fields, (
            f"Brand is missing fields: "
            f"{missing_fields}. "
            f"Brand data: {brand}"
        )

        assert isinstance(
            brand["id"],
            int,
        )

        assert isinstance(
            brand["brand"],
            str,
        )

        assert brand["brand"].strip()